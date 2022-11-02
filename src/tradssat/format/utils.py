import re

from .exper_fmt import *
from .wth_fmt import *
from .cli_fmt import *
from .sol_fmt import *
from .geno_fmt import *

EXP_SECTION = 'EXP.DETAILS:'
TRT_SECTION = re.compile(r'TREATMENTS(\W+[-]+FACTOR LEVELS[-]+)?')
GENERAL_SECTION = 'GENERAL'
SOL_INST_SECTION = re.compile(r'^[A-Za-z_0-9]{8}[A-Za-z_0-9]{0,2}')
WEATHER_SECTION = re.compile(r'^WEATHER\s?(DATA\s)?:')
CLIMATE_SECTION = re.compile(r'^CLIMATE\s?:(.)*')
CULTINAR_SECTION = re.compile(r'^(.)+:(.)*')

DEFAULT_FMT = '0'

SECTION_LINE_FORMAT_SET = {
    # EXPER FILEX
    'EXP.DET': EXP_S,
    'GENERAL': GENERAL_S,
    'TREATME': TREATMENTS_S,
    'CULTIVA': CULTIVARS_S,
    'FIELDS': FIELDS_S,
    'SOIL AN': SOIL_ANALYSIS_S,
    'INITIAL': INITIAL_CONDITION_S,
    'PLANTIN': PLANTING_S,
    'IRRIGAT': IRRIGATION_S,
    'FERTILI': FERTILIZERS_S,
    'RESIDUE': RESIDUES,
    'CHEMICA': CHEMICAL_S,
    'TILLAGE': TILLAGE_S,
    'ENVIRON': ENVIRONMENT_S,
    'HARVEST': HARVEST_S,
    'SIMULAT': SIMULATION_S,

    # WEATHER FILEW
    'WEATHER': WEATHER_S,

    # CLIMATE CLI
    'CLIMATE': CLIMATE_S,
    'MONTHLY': MTH_AVG_S,
    'WGEN PA': WGEN_PARAMS_S,
    'RANGE C': RANGE_CHECK_S,
    'FLAGGED': FLAGGED_DATA_S,

    # SOIL FILES
    'SOILS: ': SOIL_S,
    'SLSOURCE': SOIL_SITE_S,

    # GENOTYPE FILES
    'GENOTYPE': CULTIVAR_S,
    'ECOTYPE': ECOTYPE_S,
}

LINE_FORMAT_SET = {
    # EXPER FILEX:
    # Experiment Details
    '@PEOPLE': (PEOPLE_V, PEOPLE_L),
    '@ADDRESS': (ADDRESS_V, ADDRESS_L),
    '@SITE': (SITE_V, SITE_L),
    '@NOTES': (NOTES_V, NOTES_L),
    '@ PAREA': (PLOT_INFO_V, PLOT_INFO_L),
    # Treatments
    '@N R O C': (TREATMENTS_V, TREATMENTS_L),
    # Cultivar
    '@C CR IN': (CULTIVARS_V, CULTIVARS_L),
    # Fields
    '@L ID_FI': (FIELDS_FIRST_LINE_V, FIELDS_FIRST_LINE_L),
    '@L .....': (FIELDS_OTHER_LINES_V, FIELDS_OTHER_LINES_L),
    '@L      ': (FIELDS_OTHER_LINES_V, FIELDS_OTHER_LINES_L),  # both '.' and ' ' exist in FILEX.
    # Soil Analysis
    '@A SADAT': (SOIL_ANALYSIS_FIRST_LINE_V, SOIL_ANALYSIS_OTHER_LINES_V),
    '@A  SABL': (SOIL_ANALYSIS_OTHER_LINES_V, SOIL_ANALYSIS_OTHER_LINES_L),
    # Initial Condition
    '@C   PCR': (INITIAL_CONDITION_FIRST_LINE_V, INITIAL_CONDITION_FIRST_LINE_L),
    '@C  ICBL': (INITIAL_CONDITION_OTHER_LINES_V, INITIAL_CONDITION_OTHER_LINES_L),
    # Planting
    '@P PDATE': (PLANTING_DETAILS_V, PLANTING_DETAILS_L),
    # Irrigation
    '@I  EFIR': (IRRIGATION_FIRST_LINE_V, IRRIGATION_FIRST_LINE_L),
    '@I IDATE': (IRRIGATION_OTHER_LINES_V, IRRIGATION_OTHER_LINES_V),
    # Fertilizer
    '@F FDATE': (FERTILIZERS_V, FERTILIZERS_L),
    # Residue
    '@R RDATE': (RESIDUES_V, RESIDUES_L),
    # Chemical
    '@C CDATE': (CHEMICAL_V, CHEMICAL_L),
    # Tillage
    '@T TDATE': (TILLAGE_V, TILLAGE_L),
    # Environment
    '@E ODATE': (ENVIRONMENT_V, ENVIRONMENT_L),
    # Harvest
    '@H HDATE': (HARVEST_DETAILS_V, HARVEST_DETAILS_L),
    # Simulation
    '@N GENER': (SM_GENERAL_LINE_V, SM_GENERAL_LINE_L),
    '@N OPTIO': (SM_OPTIONS_LINE_V, SM_OPTIONS_LINE_L),
    '@N METHO': (SM_METHODS_LINE_V, SM_METHODS_LINE_L),
    '@N MANAG': (SM_MANAGEMENT_LINE_V, SM_MANAGEMENT_LINE_L),
    '@N OUTPU': (SM_OUTPUTS_LINE_V, SM_OUTPUTS_LINE_L),
    '@  AUTOM': (SM_AUTO_MANAGEMENT_V, SM_AUTO_MANAGEMENT_V),  # Management line doesn't have any data lines.
    '@N PLANT': (SM_PLANTING_LINE_V, SM_PLANTING_LINE_L),
    '@N IRRIG': (SM_IRRI_WATER_LINE_V, SM_IRRI_WATER_LINE_L),
    '@N NITRO': (SM_NITRO_FERT_LINE_V, SM_NITRO_FERT_LINE_L),
    '@N RESID': (SM_RESIDUES_LINE_V, SM_RESIDUES_LINE_L),
    '@N HARVE': (SM_HARVESTS_LINE_V, SM_HARVESTS_LINE_L),

    # WEATHER FILEW:
    '@ INSI      LAT     LONG  ELEV   TAV   AMP REFHT': (WTH_FIRST_LINE_V, WTH_FIRST_LINE_L),
    '@DATE  S': (WTH_OTHER_LINES_V, WTH_OTHER_LINES_L),
    '@YRDAY S': (WTH_OTHER_LINES_V, WTH_OTHER_LINES_L),

    # CLIMATE CLI FILES:
    '@ INSI      LAT     LONG  ELEV   TAV   AMP  SRAY': (CLI_FIRST_LINE_V, CLI_FIRST_LINE_L),
    '@START  D': (CLI_SECOND_LINES_V, CLI_SECOND_LINES_L),
    '@ GSST  ': (CLI_THIRD_LINES_V, CLI_THIRD_LINES_L),
    '@  MTH  SAMN': (MTH_AVG_V, MTH_AVG_L),
    '@MONTH  SAMN': (MTH_AVG_V, MTH_AVG_L),
    '@  MTH  SDMN': (WGEN_PARAMS_V, WGEN_PARAMS_L),
    '@      SRAD': (RANGE_CHECK_V, RANGE_CHECK_L),
    '@BEGYR ': (FLAGGED_DATA_FIRST_LINE_V, FLAGGED_DATA_FIRST_LINE_L),
    '@         TOTAL': (FLAGGED_DATA_OTHER_LINES_V, FLAGGED_DATA_OTHER_LINES_L),

    # SOIL FILES
    '@SITE   ': (SOL_SECOND_LINE_V, SOL_SECOND_LINE_V),
    '@ SCOM  ': (SOL_THIRD_LINE_V, SOL_THIRD_LINE_V),
    '@  SLB  SLMH': (SOL_NL_LINE_V, SOL_NL_LINE_V),
    '@  SLB SLMH': (SOL_NL_LINE_V, SOL_NL_LINE_V),              # IN00020001 section in SOIL.SOL have this format.
    '@  SLB  SLPX': (SOL_NL_TO_4NL_FIRST_LINE_V, SOL_NL_TO_4NL_FIRST_LINE_V),

    # GENOTYPE FILES
    '@VAR#  VRNAME': (CULTIVAR_GRO_V, CULTIVAR_GRO_L),
    '@VAR#  VAR-NAME': (CULTIVAR_SIM_V, CULTIVAR_SIM_L),
    '@ECO#  ECONAME': (ECOTYPE_GRO_V, ECOTYPE_GRO_L),
    '@ECO#     P1': (ECOTYPE_SIM_V, ECOTYPE_SIM_L),
}


def get_section_fmt(name):
    for k in SECTION_LINE_FORMAT_SET:
        if name.startswith(k):
            return SECTION_LINE_FORMAT_SET[k]

        if SOL_INST_SECTION.match(name):
            return SECTION_LINE_FORMAT_SET['SLSOURCE']

        if CULTINAR_SECTION.match(name):
            return SECTION_LINE_FORMAT_SET['GENOTYPE']

    return DEFAULT_FMT


def get_line_fmt(line: str):
    # '0' is expression to read and write empty string.
    res = (DEFAULT_FMT, DEFAULT_FMT)

    for key in LINE_FORMAT_SET:
        if line.startswith(key):
            res = LINE_FORMAT_SET[key]
            break

    # Because there are two kinds of lines start with '@SITE' in FILEX and FILES.
    # Thus, line start with '@SITE    ' in FILES should be matched individually.
    if line.startswith('@SITE   '):
        res = LINE_FORMAT_SET['@SITE   ']

    return res
