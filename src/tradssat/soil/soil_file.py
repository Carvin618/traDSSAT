import re

from tradssat.tmpl import InpFile
from .soil_vars import main_vars, header_vars
from tradssat.format.utils import SOL_INST_SECTION


class SoilFile(InpFile):
    """
    File reader for soil (.SOL) DSSAT files.
    """
    ext = '.SOL'

    def _get_var_info(self):
        return main_vars

    def _get_header_vars(self):
        return {SOL_INST_SECTION: header_vars}
