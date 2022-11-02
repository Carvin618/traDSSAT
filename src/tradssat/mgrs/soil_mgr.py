import os

from tradssat import SoilFile
from .mgr import get_dssat_subdir


class PeriphSoilMgr(object):

    def __init__(self, soils, levels):
        self.files = {lvls: SoilMgr(sl) for sl, lvls in zip(soils, levels)}

    def get_value(self, var, level):
        return self.files[level].get_value(var)

    def set_value(self, var, val, level, subsect=None, cond=None):
        return self.files[level].set_value(var, val, subsect=subsect, cond=cond)

    def variables(self):
        return list({v for f in self.files.values() for v in f.variables()})

    def write(self, force=False):
        for soil in self.files.values():
            soil.write(force)


class SoilMgr(object):
    def __init__(self, code):

        soils_dir = get_dssat_subdir('Soil')

        self.file = None
        self.path = None
        for f in os.listdir(soils_dir):
            if SoilFile.matches_file(f):
                file = SoilFile(os.path.join(soils_dir, f))

                if code in file:
                    self.file = file
                    self.code = code
                    self.path = os.path.join(soils_dir, f)
                    break

        if self.file is None:
            raise ValueError('No soil file found for soil "{}".'.format(code))

    def get_value(self, var):
        return self.file.get_value(var, sect=self.code)

    def set_value(self, var, val, subsect=None, cond=None):
        self.file.set_value(var, val, sect=self.code, subsect=subsect, cond=cond)

    def variables(self):
        return self.file.variables()

    def write(self, force=False):
        self.file.write(file=self.path, force=force)

