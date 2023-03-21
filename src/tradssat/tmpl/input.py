import os
import fortranformat as ff

from .file import File
from .vals import ValueSubSection
from .var import HeaderVariableSet
from tradssat.format.utils import get_section_fmt
from tradssat.error import *


class InpFile(File):
    """
    Parent class for all input files, as well as for `Summary.OUT`.
    """

    ext = None  # type: str

    def __init__(self, file):
        self._header_vars = HeaderVariableSet(self._get_header_vars())
        super().__init__(file)

    def write(self, file, force=False):
        lines = []

        write = force or file != self.file or self.changed()

        if write:
            self._values.write(lines)

            with open(file, 'w', encoding=self.encoding) as f:
                f.writelines(l + "\n" for l in lines)

    def set_value(self, var, val, sect=None, subsect=None, cond=None):
        header = self.is_header_var(var)
        if header:
            self._values.set_value(var, val, header=header, sect=sect)
        else:
            self._values.set_value(var, val, sect=sect, subsect=subsect, cond=cond)

    def add_var(self, var, vals, header=False, sect=None, subsect=None):
        """
            Create a variable with values in current file.

            Parameters
            ----------
            var: str
                The name of variable would be created.
            vals: str, int, float, list, dict
                The values of the variable var.
                If vals is a dict, the dict keys are line numbers and values are the variable values.
                If vals is a dict, partial lines are allowed and the other line would be set to the
                missing value of the variable.
            sect: str
                The section name that the var belong to.
            subsect: int or list
                The subsection index(s) that the var belong to.
            header: bool
                Indicate the variable is a header variable.

            Returns
            -------
            None

            Example:
            ----------
                # Add FMOPT variable with value 'Y' in its section and all subsection.
                add_var('FMOPT', 'C')

                # Add FMOPT variable with value 'Y' in its section and subsection 4.
                add_var('FMOPT', 'C', subsect=4)

                # add 'IRVAL' variable with partial lines in its section and subsection 1.
                # The other lines will be set to miss value.
                add_var('IRVAL', {0: 29, 1: 28, 2: 27, 3: 28, 4: 27, 5: 28,...}, subsect=1)

                # add 'IRVAL' variable with all values in its section and subsection 1.
                add_var('IRVAL' [29, 28, 27, 28, 27, 28, 31, 28, 32, 34, 28, 28, 33, 34, 29, 29, 33, 35, 36], subsect=1)
            """

        if not self.exists(var, sect):
            raise VariableNotFoundError(f'Variable {var} does not exists. Please check the name.')

        if not header and self._header_vars.exists(var):
            header = True

        self._values.add_var(self._var_info.get_var(var, sect), vals, header=header, sect=sect, subsect=subsect)

    def exists(self, var, sect=None):
        return self._header_vars.exists(var) or self._var_info.exists(var, sect)

    def changed(self):
        """
        Checks whether the file has been edited and needs to be rewritten.

        Returns
        -------
        bool
            Whether the file has been edited or not.
        """
        return self._values.changed()

    def get_var(self, var, sect=None):
        try:
            return super().get_var(var, sect=sect)
        except ValueError:
            return self._header_vars.get_var(var, sect=sect)

    def _process_section_header(self, lines):

        if lines[0][0] == '@':  # In case a section header is missing
            self._values.add_section('', fmt=get_section_fmt(''))
            return '', lines

        header_text = lines[0][1:].strip()  # Skip initial "*"

        match = self._header_vars.matches(header_text)
        if match:

            section_name = match
            self._values.add_section(section_name, get_section_fmt(section_name))
            header_text = header_text[len(match):]

            h_vars = self._header_vars.get_vars(match)

            l_vals = []

            reader = ff.FortranRecordReader(get_section_fmt(section_name))
            # print('[DEBUG] ::', section_name, ' ', get_section_fmt(section_name))
            try:
                # print("[DEBUG] :: ", section_name, ' ',get_section_fmt(section_name))
                vals = reader.read(header_text)
                # print("[DEBUG] :: ", vals)
            except ValueError as ve:
                raise ve
            for vr, val in zip(h_vars, vals):
                #size = vr.size + vr.spc
                #val = header_text[:size].strip()

                matr = self._gen_empty_mtrx(str(vr), size=1)
                try:
                    matr[:] = val
                except ValueError as ve:
                    print(val)
                    raise ve

                l_vals.append(matr)

                #header_text = header_text[size:]

            header_vars_subsect = ValueSubSection(h_vars, l_vals=l_vals)
            self._values[section_name].set_header_vars(header_vars_subsect)

            return match, lines[1:]

        self._values.add_section(header_text, get_section_fmt(header_text))
        return header_text, lines[1:]

    def _get_header_vars(self):
        return {}

    def is_header_var(self, var):
        header_vars = [str(v) for val in self._get_header_vars().values() for v in val]
        if var in header_vars:
            return True
        return False

    @classmethod
    def matches_file(cls, file):
        """
        Checks whether a given file can be read by this class.

        Parameters
        ----------
        file: str
           The filename or full path to be read.

        Returns
        -------
        bool
           ``True`` if the file matches; ``False`` otherwise.
        """

        ext = os.path.splitext(file)[1]
        if isinstance(cls.ext, str):
            return ext.lower() == cls.ext.lower()
        return ext.lower() in [x.lower() for x in cls.ext]

    def _get_var_info(self):
        raise NotImplementedError
