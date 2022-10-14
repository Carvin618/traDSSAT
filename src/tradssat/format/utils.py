from .exper_fmt import *
# from .wth_fmt import *

DEFAULT_FMT = '0'

SECTION_LINE_FORMAT_SET = {
    # EXPER FILE
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
    'ENVIRON': ENVIRONMENT,
    'HARVEST': HARVEST,
    'SIMULAT': SIMULATION,

    # WEATHER FILE
    # 'WEATHER': WEATHER_S,

}

LINE_FORMAT_SET = {
    # EXPER FILE:
    # Experiment Details
    '@PEOPLE': (PEOPLE_V, PEOPLE_L),
    '@ADDRESS': (ADDRESS_V, ADDRESS_L),
    '@SITE': (SITE_V, SITE_L),
    '@NOTES': (NOTES_V, NOTES_L),
    # Treatments
    '@N R O C': (TREATMENTS_V, TREATMENTS_L),
    # Cultivar
    '@C CR IN': (CULTIVARS_V, CULTIVARS_L),
    # Fields
    '@L ID_FI': (FIELDS_FIRST_LINE_V, FIELDS_FIRST_LINE_L),
    '@L .....': (FIELDS_OTHER_LINES_V, FIELDS_OTHER_LINES_L),
    '@L      ': (FIELDS_OTHER_LINES_V, FIELDS_OTHER_LINES_L),  # both '.' and ' ' exists in FILEX.
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

    # WEATHER FILE:
    # '@ INSI  ': (WTH_FIRST_LINE_V, WTH_OTHER_LINES_L),
    # '@DATE  S': (WTH_OTHER_LINES_V, WTH_OTHER_LINES_L),
}


def get_section_fmt(name):
    res = DEFAULT_FMT
    for k in SECTION_LINE_FORMAT_SET:
        if name.startswith(k):
            res = SECTION_LINE_FORMAT_SET[k]
            break

    return res


def get_line_fmt(line: str):
    # '0' is expression to read and write empty string.
    res = (DEFAULT_FMT, DEFAULT_FMT)
    for key in LINE_FORMAT_SET:
        if line.startswith(key):
            res = LINE_FORMAT_SET[key]
            break

    return res
