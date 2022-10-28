import re

from tradssat.tmpl import InpFile
from .wth_vars import main_vars, header_vars
from tradssat.format.utils import WEATHER_SECTION


class WTHFile(InpFile):
    """
    Reader for DSSAT weather (.WTH and .WTG) files.
    """

    ext = ['.WTH', '.WTG']

    def _get_var_info(self):
        return main_vars

    def _get_header_vars(self):
        # Both 'WEATHER :' and  'WEATHER DATA :' section name exists in WTH file.
        return {WEATHER_SECTION: header_vars}
