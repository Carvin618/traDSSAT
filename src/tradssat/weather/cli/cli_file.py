import re

from tradssat.tmpl import InpFile
from .cli_vars import main_vars, header_vars


class CLIFile(InpFile):
    """
    Reader for DSSAT climate (.CLI) files.
    """

    ext = ['.CLI']

    def _get_var_info(self):
        return main_vars

    def _get_header_vars(self):
        # Both 'WEATHER :' and  'WEATHER DATA :' section name exists in WTH file.
        return {re.compile(r'^CLIMATE\s?:'): header_vars}
