import re

from tradssat.tmpl import InpFile
from .wth_vars import main_vars, header_vars


class WTHFile(InpFile):
    """
    Reader for DSSAT weather (.WTH and .WTG) files.
    """

    ext = ['.WTH', '.WTG']

    def _get_var_info(self):
        return main_vars

    def _get_header_vars(self):
        # Both 'WEATHER :' and  'WEATHER DATA :' section name exists in WTH file.
        return {re.compile(r'^WEATHER\s(DATA\s)?:'): header_vars}
