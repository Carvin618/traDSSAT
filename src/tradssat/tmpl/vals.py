import re

import numpy as np
import fortranformat as ff

from .var import CharacterVar, IntegerVar, FloatVar
from tradssat.error import *


class FileValueSet(object):
    """
    Represents the set of values in a DSSAT file.
    """

    def __init__(self):
        self._sections = {}

    def add_section(self, name, fmt):
        """
        Adds a section to the file.
        
        Parameters
        ----------
        name: str
            Name of the new section.
        fmt: str
            The Fortran format expression for the section line.
        """
        self._sections[name] = ValueSection(name, fmt)

    def write(self, lines):
        """
        Writes the file.
        
        Parameters
        ----------
        lines: list[str]
            List to which to write output lines.

        Returns
        -------
        list
            The modified list.
        """

        for s in self:
            s.write(lines)

        lines.append('')

        return lines

    def to_dict(self):
        """
        Converts the file to a dictionnary.
        
        Returns
        -------
        dict

        """
        return {name: sect.to_dict() for name, sect in self._sections.items()}

    def get_value(self, var, sect=None, subsect=None, cond=None):
        if isinstance(sect, str):
            return self[sect].get_value(var, subsect, cond)
        else:
            if isinstance(sect, dict):
                sects = [
                    s for s in self if all(vr in s and np.all(s.get_header_var(vr) == vl) for vr, vl in sect.items())
                ]
            else:
                sects = self._sections.values()

            try:
                value = next(s.get_value(var, subsect, cond=cond) for s in sects if var in s)
            except StopIteration:
                raise ValueError(f'Variable "{var}" value not found.')

            return value

    def set_value(self, var, val, sect=None, subsect=None, cond=None, header=False):
        if sect is not None:
            self[sect].set_value(var, val, subsect, cond=cond, header=header)
        else:
            for s in self:
                if var in s:
                    s.set_value(var, val, subsect, cond=cond, header=header)

    def add_var(self, var, values, header, sect=None, subsect=None):
        if sect:
            if sect not in self._sections:
                raise ValueError(f'Section {sect} does not exists.')

            self._sections[sect].add_var(var, values, header, subsect)

        elif var.sect:
            self._sections[var.sect].add_var(var, values, header, subsect)
        else:
            raise ValueError(f'Parameter "section" should be provided.')

    def add_row(self, sect, subsect=None, vals=None):
        """
        Adds a row to the file.
        
        Parameters
        ----------
        sect: str
            Name of section.
        subsect: int
            Subsection number. If ``None``, will add row to all subsections.
        vals: dict
            Dictionnary of new row variable values.

        """
        self[sect].add_row(subsect, vals)

    def remove_row(self, sect, subsect=None, cond=None):
        self[sect].remove_row(subsect, cond)

    def find_var_sect(self, var):
        """
        Finds the section in which a variable appears.
        
        Parameters
        ----------
        var: str
            The name of the variable

        Returns
        -------
        str
            The file section name.
        """
        return next(s.name for s in self if var in s)

    def changed(self):
        """
        Detects if any variable values have been changed.
        
        Returns
        -------
        bool
        """
        return any(s.changed() for s in self)

    def __iter__(self):
        for s in self._sections.values():
            yield s

    def __contains__(self, item):
        return item in self._sections

    def __getitem__(self, item):
        if isinstance(item, str):
            return self._sections[item]
        else:
            return next(s for s in self._sections.values() if re.match(item, s.name))


class ValueSection(object):
    """
    Represents the structure and variable values in a DSSAT file section.
    """

    def __init__(self, name, fmt):
        """

        Parameters
        ----------
        name: str
            The name of the section.
        """

        self.name = name
        self._subsections = []
        self._header_vars = HeaderValues(fmt=fmt)

    def add_subsection(self, subsect):
        """
        Add a subsection to the section.

        Parameters
        ----------
        subsect: ValueSubSection
            The new subsection.

        """
        self._subsections.append(subsect)

    def set_header_vars(self, h_vars):
        """
        Sets the section's header variables.

        Parameters
        ----------
        h_vars: ValueSubSection
            The subsection representing the header variables.

        """
        self._header_vars.set_vars(h_vars)

    def get_header_var(self, var):
        """
        Obtain the value of a header variable.

        Parameters
        ----------
        var: str
            The name of the variable

        Returns
        -------
        np.ndarray
            The value of the header variable.
        """
        return self._header_vars.get_value(var)

    def write(self, lines):
        """
        Writes the section to a list of lines.

        Parameters
        ----------
        lines: list[str]
            The list of lines to which to append this section.

        """
        lines.append(self._write_header())
        for s in self:
            s.write(lines)

        lines.append('')

    def to_dict(self):
        """
        Converts the section to a dictionnary.

        Returns
        -------
        dict
        """
        return {
            'header vars': self._header_vars.to_dict(),
            'main vars': [subsect.to_dict() for subsect in self]
        }

    def get_value(self, var, subsect=None, cond=None):
        if var in self._header_vars:
            return self.get_header_value(var)

        subsect = self._valid_subsects(subsect)

        if cond is None:
            cond = {}
        req_vars = {var, *cond}

        val = []
        for s in subsect:
            sub = self[s]
            if all(vr in sub for vr in req_vars):
                filter_ = sub.filter_cond(cond) if cond else slice(None)
                val.append(sub[var].val[filter_])

        return np.concatenate(val)

    def set_value(self, var, val, subsect=None, cond=None, header=False):
        if header:
            self.set_header_value(var, val)
            return

        subsect = self._valid_subsects(subsect)

        if cond is None:
            cond = {}
        req_vars = {var, *cond}

        success = False
        for s in subsect:
            sub = self[s]
            if all(vr in sub for vr in req_vars):
                success = True
                sub.set_value(var, val, cond=cond)

        if not success:
            raise ValueError('Variable "{}" not found.'.format(var))

    def get_header_value(self, var):
        return self._header_vars.get_value(var)

    def set_header_value(self, var, val):
        if var not in self._header_vars:
            raise ValueError(f'Variable "{var}" not found in "{self.name}" section header')

        self._header_vars.set_value(var, val)

    def add_var(self, var, vals, header=False, subsect=None):
        if (not header) and (subsect == 0):
            raise ValueError(f'Parameter "header" or "subsect" must be provided.')

        if header:
            self._header_vars.add_var(var, vals)
        else:
            subsect = self._valid_subsects(subsect)
            for s in subsect:
                self._subsections[s].add_var(var, vals)

    def add_row(self, subsect=None, vals=None):
        subsect = self._valid_subsects(subsect)
        for s in subsect:
            self[s].add_row(vals)

    def remove_row(self, subsect=None, cond=None):
        subsect = self._valid_subsects(subsect)
        for s in subsect:
            self[s].remove_row(cond)

    def changed(self):
        """
        Checks whether any value has changed in the section.

        Returns
        -------
        bool
        """
        return any(s.changed() for s in self) or self._header_vars.changed()

    def _write_header(self):
        return '*' + self.name + self._header_vars.write()

    def _valid_subsects(self, subsects):
        if subsects is None:
            subsects = range(len(self._subsections))
        elif isinstance(subsects, int):
            subsects = [subsects]
        for s in subsects:
            if s >= len(self._subsections):
                raise ValueError(f'Subsection :{s}" does not exist. '
                                 f'Only {len(self._subsections)} subsections exist.')
        return subsects

    def __iter__(self):
        for s in self._subsections:
            yield s

    def __contains__(self, item):
        return any(item in s for s in self._subsections) or item in self._header_vars

    def __getitem__(self, item):
        return self._subsections[item]

    def __setitem__(self, key, value):
        for subsect in self:
            if key in subsect:
                subsect[key] = value


class ValueSubSection(object):
    """
    Represents the variables and values in a DSSAT file subsection.
    """

    def __init__(self, l_vars, l_vals, fmt=None):
        self._vars = {str(vr): VariableValue(vr, vl) for vr, vl in zip(l_vars, l_vals)}

        if fmt:
            self.var_fmt = fmt[0]  # variable name format expression for a line
            self.val_fmt = fmt[1]  # variable value format expression for a line
        else:
            # '0' is expression to read and write empty string.
            self.var_fmt = '0'
            self.val_fmt = '0'

    def set_value(self, var, val, cond=None):
        filter_ = self.filter_cond(cond)
        self._vars[str(var)].set_value(val, i=filter_)

    def add_var(self, var, vals):
        # Multi-line variables.
        if isinstance(vals, list):
            if len(vals) != self.n_data():
                raise ValueError(f'Variable {var} accept {self.n_data()} values, but {len(vals)} is given.')

            for v in vals:
                var.check_val(v)

            self._vars[str(var)] = VariableValue(var, np.array([var.miss for _ in vals]))
            self._vars[str(var)].set_value(vals)

        elif isinstance(vals, dict):
            if len(vals) > self.n_data():
                raise ValueError(f'Variable {var} accept {self.n_data()} values, but {len(vals)} is given.')

            for v in vals.values():
                var.check_val(v)

            self._vars[str(var)] = VariableValue(var, np.array([var.miss for _ in range(self.n_data())]))
            self._vars[str(var)].set_value([vals[i] if i in vals else var.miss for i in range(self.n_data())])

        # Single-line variable.
        elif isinstance(vals, str) or isinstance(vals, int) or isinstance(vals, float):
            var.check_val(vals)
            self._vars[str(var)] = VariableValue(var, np.array([var.miss]))
            self._vars[str(var)].set_value(vals)

        else:
            raise ValueError(f'vals parameter only accept "list", "dict", "str", "int" and "float" value.')

        self.check_dims()

    def add_row(self, vals=None):
        """
        Adds a row to the subsection.

        Parameters
        ----------
        vals: dict
            The values for the new row. Any missing value will be assigned the corresponding missing code for that
            variable (usually -99).
        """
        if vals is None:
            vals = {}
        for nm, vr in self._vars.items():
            val = vals[nm] if nm in vals else vr.var.miss
            vr.add_value(val)

    def remove_row(self, cond=None):
        filter_ = self.filter_cond(cond)
        for vr in self._vars.values():
            vr.remove_value(filter_)

    def filter_cond(self, cond):
        if cond is None:
            cond = {}
        return np.all(
            [self[vr] == vl for vr, vl in cond.items()], axis=0
        )

    def check_dims(self):
        """
        Checks that all variables in the subsection have the same size. (If not, the subsection cannot write to disk.)

        Raises
        -------
        ValueError
            If not all variables have the same size.
        """
        if not len(np.unique([v.size() for v in self._vars.values()])) == 1:
            raise ValueError(f'Not all variables in this subsection have the same size. {self}')

    def check_vals(self):
        for vr in self:
            vr.check_val()

    def exists(self, var):
        if str(var) in self._vars.keys():
            return True
        return False

    def n_data(self):
        """
        Obtain the size of variables. Will fail if not all variables have the same size.

        Returns
        -------
        int
            The size of all variables in the subsection.

        Raises
        ------
        ValueError
            If not all variables have the same size.
        """

        self.check_dims()
        return self[list(self._vars)[0]].size()

    def write(self, lines):
        """
        Writes the subsection.

        Parameters
        ----------
        lines: list[str]
            The list of lines to which to append this subsection.

        """
        # print(self._vars)
        self.check_dims()
        self.check_vals()

        var_writer = ff.FortranRecordWriter(self.var_fmt)
        val_writer = ff.FortranRecordWriter(self.val_fmt)
        line = var_writer.write([vr.write() for vr in self])

        # There is a space line at the end of each Automatic management subsection.
        if line.startswith('   AUTOMATIC'):
            lines.append('')

        if line .startswith(' '):
            lines.append(line.replace(' ', '@', 1))
        else:
            lines.append('@' + line)

        for i in range(self.n_data()):
            written = [vr.write(i) for vr in self]
            # for i, (x, vr) in enumerate(zip(list(written), self)):
            #     extra = len(x) - (vr.var.size + vr.var.spc)
            #     if i < len(written) - 1 and extra:
            #         written[i + 1] = written[i + 1][extra:]

            line = val_writer.write(written)
            lines.append(line)

    def to_dict(self):
        """
        Converts the subsection to a dictionnary.

        Returns
        -------
        dict
        """
        return {nm: vr.val for nm, vr in self._vars.items()}

    def changed(self):
        """
        Checks whether any variable in the subsection has been changed.

        Returns
        -------
        bool

        """
        return any(v.changed for v in self)

    def __iter__(self):
        for vr in self._vars.values():
            yield vr

    def __contains__(self, item):
        return str(item) in self._vars

    def __getitem__(self, item):
        return self._vars[str(item)]

    def __setitem__(self, key, value):
        self.set_value(key, value)


class VariableValue(object):
    """
    Represents a DSSAT file variable.
    """

    def __init__(self, var, val):

        self.changed = False

        self.name = str(var)

        self.var = var
        self.val = val

    def set_value(self, val, i=None):
        """
        Changes the value of the variable.

        Parameters
        ----------
        val: float | int | np.ndarray
            The new value.
        i: int | np.ndarray
            Índices at which to change the value. If ``None``, all values of the variable will be changed.

        """
        if i is None:
            i = True

        if isinstance(val, np.ndarray) and (val.shape != self.val[i].shape):
            if not i:
                raise ValueError('Cannot set value by index when shapes do not match.')
            self.val = np.array(val)
            self.changed = True

        else:
            if np.any(val != self.val[i]):
                self.val[i] = val
                self.changed = True

    def add_value(self, val):
        """
        Adds a value to the variable's matrix.

        Parameters
        ----------
        val: int | float
            The new value.

        """
        self.val = np.append(self.val, val).astype(self.val.dtype)
        self.changed = True

    def remove_value(self, i):
        """
        Removes a value from the variable's matrix.

        Parameters
        ----------
        i: np.ndarray
            The indices of the value(s) to remove. May be a list of indices, or else a boolean mask of the same
            size as the variable.

        """
        if i.dtype == bool:
            filter_ = i
        else:
            filter_ = np.isin(np.arange(self.size()), i)
        self.val = self.val[~filter_]

    def size(self):
        """
        Returns the size of the variable.

        Returns
        -------
        int
        """
        return self.val.size

    def check_val(self):
        self.var.check_val(self.val)

    def write(self, i=None):
        """
        Converts the variable to a string.

        Parameters
        ----------
        i: int
            The index of the value to write. If ``None``, the name of the variable will be written instead.

        Returns
        -------
        str
            The properly written and formatted variable.

        """
        if i is None:
            return self.var.write()
        else:
            self.changed = False
            return self.var.write(self.val[i])

    def __eq__(self, other):
        return other == self.val


class HeaderValues(object):
    """
    Represents DSSAT file header variables and their values.
    """

    def __init__(self, fmt):
        self._subsect = None
        self.fmt = fmt

    def set_vars(self, subsect):
        """
        Sets the variables of the header.

        Parameters
        ----------
        subsect: ValueSubSection
            The subsection with variables and their values already specified.
        """

        self._subsect = subsect

    def get_value(self, var):
        """
        Obtain the value of a header variable.

        Parameters
        ----------
        var: str
            The variable of interest.

        Returns
        -------
        np.ndarray
            The value of the variable.

        """
        return self._subsect[var].val

    def set_value(self, var, val):
        if var not in self._subsect:
            raise ValueError(f'Variable "{var}" not in section header. Please create.')
        self._subsect.set_value(var, val)

    def create_value(self, var, val):
        self._subsect.create_value(var, val)

    def exists(self, var):
        return self._subsect.exists(var)

    def to_dict(self):
        """
        Convert to dictionnary (json) format.

        Returns
        -------
        list
            The (mostly) jsonified version of the header's variables.
        """
        if self._subsect is None:
            return {}
        else:
            return self._subsect.to_dict()

    def write(self):
        """
        Writes the header values to a string.

        Returns
        -------
        str
        """
        writer = ff.FortranRecordWriter(self.fmt)
        if self._subsect is None:
            return ''
        else:
            try:
                return writer.write([vr.write(0) for vr in self._subsect])
            except TypeError as err:
                print([vr.write(0) for vr in self._subsect])
                raise err

    def changed(self):
        """
        Checks if the header variables values have been changed.

        Returns
        -------
        bool
        """
        if self._subsect is None:
            return False
        return self._subsect.changed()

    def __contains__(self, item):
        if self._subsect is None:
            return False
        else:
            return item in self._subsect
