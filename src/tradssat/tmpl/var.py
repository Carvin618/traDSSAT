import numpy as np

from .utils import _name_matches

CODE_MISS = -99


class Variable(object):
    """
    Parent class for all variable types.
    """
    type_ = None

    def __init__(self, name, size, spc, float_r, miss, sect, info, fmt, hidden):
        self.name = name
        self.size = size
        self.spc = spc

        self.float_r = float_r
        self.miss = miss

        self.info = info
        self.sect = sect

        self.fmt = fmt              # fmt is the fortran format output expression for variable value.
        self.hidden = hidden

    def write(self, val=None):
        # fill = self.fill if val is None else ' '
        if val is None:
            if self.hidden:
                txt = ''
            else:
                txt = self._write(self.name)
        else:
            if val == CODE_MISS:
                val = self.miss
            txt = self._write(val)

        # if self.float_r:
        #     return ' ' * self.spc + txt.ljust(self.size, fill)

        return txt

    def check_val(self, val):
        raise NotImplementedError

    def _write(self, val):
        raise NotImplementedError

    def __str__(self):
        return str(self.name)


class CharacterVar(Variable):
    """
    Character (string) variable.
    """
    type_ = str

    def __init__(self, name, size, spc=1, sect=None, fill=' ', miss='-99', info='', fmt='', right_align=True,
                 hidden=False, default=''):

        self.right_align = right_align
        self.fill = fill
        self.default = default
        super().__init__(name, size, spc, float_r=False, miss=miss, sect=sect, info=info, fmt=fmt, hidden=hidden)

    def check_val(self, val):
        if isinstance(val, str):
            if len(val) > self.size:
                raise ValueError(
                    'Value "{val}" is longer than {sz} characters for variable {name}.'.format(
                        val=val, sz=self.size, name=self
                    )
                )

    def _write(self, val):
        # FortranFormat write strings right aligned and cannot modify.
        # But some variables are left aligned. For these variables, it is needed to pad spaces
        # at tail until matching the variable size.
        if self.hidden:
            return self.default

        if self.right_align:
            return val
        else:
            return val + (self.size - len(val)) * self.fill


class NumericVar(Variable):
    """
    Parent class for numeric variable types.
    """

    def __init__(self, name, size, lims, spc, miss, sect, info, hidden, default, fmt=''):
        super().__init__(name, size, spc, sect=sect, float_r=True, miss=miss, info=info, fmt=fmt, hidden=hidden)

        if lims is None:
            lims = (-np.inf, np.inf)
        lims = (-np.inf if lims[0] is None else lims[0], np.inf if lims[1] is None else lims[1])

        self.lims = lims

        self.default = default

    def check_val(self, val):
        val = np.array(val)
        out = np.where(np.logical_or(np.less(val, self.lims[0]), np.greater(val, self.lims[1])))
        if out[0].size > 0:
            vals_out = val[out]
            raise ValueError(
                'Value {val} is not in range {rng} for variable {name}.'.format(val=vals_out, name=self, rng=self.lims)
            )

    def _write(self, val):
        raise NotImplementedError


class FloatVar(NumericVar):
    """
    Floating point (decimal) variable.
    """
    type_ = float

    def __init__(self, name, size, dec, lims=None, spc=1, sect=None, miss=-99, info='', fmt='',
                 hidden=False, default=0):
        super().__init__(name, size, lims, spc, miss=miss, sect=sect, info=info, fmt=fmt,
                         hidden=hidden, default=default)
        self.dec = dec

    def _write(self, val):
        if self.hidden:
            return self.default

        if val == self.miss:
            # return '-99'  # to avoid size overflow on small-sized variables with decimals
            return self.miss
        # todo: clean
        # txt_0 = str(val)
        # space_req = len(txt_0.split('.')[0]) + 1
        # if txt_0.startswith('0') or txt_0.startswith('-0'):
        #     space_req -= 1
        #
        # dec = min(self.dec, max(0, self.size - space_req))
        #
        # txt = '{:{sz}.{dec}f}'.format(val, sz=self.size, dec=dec)
        # if txt[0] == '0':
        #     txt = txt[1:]
        # elif txt[:2] == '-0':
        #     txt = '-{}'.format(txt[2:])
        # return txt
        return val


class IntegerVar(NumericVar):
    """
    Integer (whole number) variable.
    """
    type_ = int

    def __init__(self, name, size, lims=None, spc=1, sect=None, miss=-99, info='', fmt='', hidden=False, default=0):
        super().__init__(name, size, lims, spc, miss=miss, sect=sect, info=info, fmt=fmt,
                         hidden=hidden, default=default)

    def _write(self, val):
        # if val == self.miss:
        #     return '{:{sz}}'.format(val, sz=self.size)  # to avoid problems with non-numeric missing value codes
        # return '{:{sz}d}'.format(val, sz=self.size)
        if self.hidden:
            return self.default

        if val == self.miss:
            return self.miss
        return val


class VariableSet(object):
    """
    Organiser for the allowed variables of a DSSAT file type.
    """

    def __init__(self, l_vars):
        self._vars = l_vars

    def get_var(self, var, sect=None):

        try:
            return next(
                vr for vr in self._vars if str(vr) == var and _name_matches(vr.sect, sect, full=True)
            )
        except StopIteration:
            if sect is None:
                msg = 'Variable {var} does not exist.'.format(var=var)
            else:
                msg = 'Variable {var} does not exist in section {sect}.'.format(var=var, sect=sect)
            raise ValueError(msg)

    def exists(self, var, sect=None):
        for vr in self._vars:
            if str(vr) == var and _name_matches(vr.sect, sect, full=True):
                return True
        return False

    def variables(self):
        return self._vars

    def __contains__(self, item):
        return any(str(vr) == str(item) for vr in self._vars)

    def __iter__(self):
        for vr in self._vars:
            yield vr


class HeaderVariableSet(object):
    """
    Organiser for the allowed header variables of a DSSAT file type.
    """

    def __init__(self, d_vars):
        self._vars = d_vars

    def matches(self, header):
        for hd in self._vars:
            match = _name_matches(hd, header)
            if match is not None:
                return match

    def get_vars(self, header):
        return next(self._vars[hd] for hd in self._vars if _name_matches(hd, header))

    def get_var(self, var, sect=None):
        try:
            return next(
                vr for hd, vrs in self._vars.items() for vr in vrs if _name_matches(hd, sect) and var == str(vr)
            )
        except StopIteration:
            raise ValueError('Variable {var} does not exist.'.format(var=var))

    def exists(self, var):
        if var in self._vars.keys():
            return True
        return False

