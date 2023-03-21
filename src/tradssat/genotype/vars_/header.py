from tradssat.tmpl.var import CharacterVar
from tradssat.format.utils import CULTINAR_SECTION

cul_header_vars = {
    CharacterVar(name='CULNAME', size=75, spc=1, sect=CULTINAR_SECTION,
                 info='Name of the cultivar files', right_align=False),
}

eco_header_vars = {
    CharacterVar(name='ECONAME', size=75, spc=1, sect=CULTINAR_SECTION,
                 info='Name of the ecotype files', right_align=False),
}