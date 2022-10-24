from tradssat.tmpl.var import CharacterVar, FloatVar
from tradssat.format.utils import SOL_INST_SECTION

header_vars = [
    CharacterVar('SLSOURCE', 11, spc=2, sect=SOL_INST_SECTION, info='Source', right_align=False),
    CharacterVar('SLTX', 5, sect=SOL_INST_SECTION, info='Texture, code', right_align=False),
    FloatVar('SLDP', 5, 0, sect=SOL_INST_SECTION, info='Depth, cm'),
    CharacterVar('SLDESCRIP', 50, sect=SOL_INST_SECTION, info='Description or local classification', right_align=False)
]

main_vars = {
    CharacterVar('SITE', 11, sect=SOL_INST_SECTION, info='Site name', right_align=False),
    CharacterVar('COUNTRY', 12, sect=SOL_INST_SECTION, info='Country name', right_align=False),
    FloatVar('LAT', 8, 3, sect=SOL_INST_SECTION, info='Latitude'),
    FloatVar('LONG', 7, 3, sect=SOL_INST_SECTION, info='Longitude'),
    CharacterVar('SCS FAMILY', 50, sect=SOL_INST_SECTION, info='Family, SCS system', right_align=False),

    CharacterVar('SCOM', 5, sect=SOL_INST_SECTION, info='Color, moist, Munsell hue'),
    FloatVar('SALB', 5, 2, sect=SOL_INST_SECTION, info='Albedo, fraction '),
    FloatVar('SLU1', 5, 1, sect=SOL_INST_SECTION, info='Evaporation limit, cm'),
    FloatVar('SLDR', 5, 2, sect=SOL_INST_SECTION, info='Drainage rate, fraction day-1'),
    FloatVar('SLRO', 5, 1, sect=SOL_INST_SECTION, info='Runoff curve number (Soil Conservation Service)'),
    FloatVar('SLNF', 5, 2, sect=SOL_INST_SECTION, info='Mineralization factor, 0 to 1 scale'),
    FloatVar('SLPF', 5, 2, sect=SOL_INST_SECTION, info='Photosynthesis factor, 0 to 1 scale'),
    CharacterVar('SMHB', 5, sect=SOL_INST_SECTION, info='pH in buffer determination method, code'),
    CharacterVar('SMPX', 5, sect=SOL_INST_SECTION, info='Phosphorus, extractable, determination code'),
    CharacterVar('SMKE', 5, sect=SOL_INST_SECTION, info='Potassium determination method, code'),
    CharacterVar('SGRP', 5, sect=SOL_INST_SECTION, info='Probably soil group'),

    FloatVar('SLB', 5, 0, sect=SOL_INST_SECTION, info='Depth, base of layer, cm'),
    CharacterVar('SLMH', 5, sect=SOL_INST_SECTION, info='Master horizon'),
    FloatVar('SLLL', 5, 3, sect=SOL_INST_SECTION, info='Lower limit, cm3 cm-3'),
    FloatVar('SDUL', 5, 3, sect=SOL_INST_SECTION, info='Upper limit, drained, cm3 cm-3'),
    FloatVar('SSAT', 5, 3, sect=SOL_INST_SECTION, info='Upper limit, saturated, cm3 cm-3'),
    FloatVar('SRGF', 5, 3, sect=SOL_INST_SECTION, info='Root growth factor, 0.0 to 1.0 '),
    FloatVar('SSKS', 5, 3, sect=SOL_INST_SECTION, info='Sat. hydraulic conductivity, macropore, cm h-1'),
    FloatVar('SBDM', 5, 2, sect=SOL_INST_SECTION, info='Bulk density, moist, g cm-3'),
    FloatVar('SLOC', 5, 3, sect=SOL_INST_SECTION, info='Organic carbon, %'),
    FloatVar('SLCL', 5, 1, sect=SOL_INST_SECTION, info='Clay (<0.002 mm), %'),
    FloatVar('SLSI', 5, 1, sect=SOL_INST_SECTION, info='Silt (0.05 to 0.002 mm), %'),
    FloatVar('SLCF', 5, 1, sect=SOL_INST_SECTION, info='Coarse fraction (>2 mm), %'),
    # SLNI is float number with 5 width and 2 decimals. But
    FloatVar('SLNI', 5, 1, sect=SOL_INST_SECTION, info='Total nitrogen, %'),
    FloatVar('SLHW', 5, 1, sect=SOL_INST_SECTION, info='pH in water'),
    FloatVar('SLHB', 5, 2, sect=SOL_INST_SECTION, info='pH in buffer'),
    FloatVar('SCEC', 5, 1, sect=SOL_INST_SECTION, info='Cation exchange capacity, cmol kg-1'),
    FloatVar('SADC', 5, 1, sect=SOL_INST_SECTION, info=''),

    FloatVar('SLPX', 5, 1, sect=SOL_INST_SECTION, info='Phosphorus, extractable, mg kg-1'),
    FloatVar('SLPT', 5, 1, sect=SOL_INST_SECTION, info='Phosphorus, total, mg kg-1'),
    FloatVar('SLPO', 5, 1, sect=SOL_INST_SECTION, info='Phosphorus, total, mg kg-1'),
    FloatVar('CACO3', 5, 1, sect=SOL_INST_SECTION, info='CaCO3 content, g kg-1'),
    FloatVar('SLAL', 5, 1, sect=SOL_INST_SECTION, info='Aluminum'),
    FloatVar('SLFE', 5, 1, sect=SOL_INST_SECTION, info='Iron'),
    FloatVar('SLMN', 5, 1, sect=SOL_INST_SECTION, info='Manganese'),
    FloatVar('SLBS', 5, 1, sect=SOL_INST_SECTION, info='Base saturation, cmol kg-1'),
    FloatVar('SLPA', 5, 1, sect=SOL_INST_SECTION, info='Phosphorus isotherm A, mmol kg-1'),
    FloatVar('SLPB', 5, 1, sect=SOL_INST_SECTION, info='Phosphorus iostherm B, mmol kg-1'),
    FloatVar('SLKE', 5, 1, sect=SOL_INST_SECTION, info='Potassium, exchangeable, cmol kg-1'),
    FloatVar('SLMG', 5, 1, sect=SOL_INST_SECTION, info='Magnesium, cmol kg-1'),
    FloatVar('SLNA', 5, 1, sect=SOL_INST_SECTION, info='Sodium, cmol kg-1'),
    FloatVar('SLSU', 5, 1, sect=SOL_INST_SECTION, info='Sulfur'),
    FloatVar('SLEC', 5, 1, sect=SOL_INST_SECTION, info='Electric conductivity, seimen'),
    FloatVar('SLCA', 5, 1, sect=SOL_INST_SECTION, info='Ca level?'),

    FloatVar('ALFVG', 5, 3, sect=SOL_INST_SECTION, info='Who knows?'),
    FloatVar('MVG', 5, 3, sect=SOL_INST_SECTION),
    FloatVar('NVG', 5, 3, sect=SOL_INST_SECTION),
    FloatVar('WCRES', 5, 3, sect=SOL_INST_SECTION )

}
