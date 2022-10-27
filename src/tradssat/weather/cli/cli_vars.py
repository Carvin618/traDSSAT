from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar
from tradssat.format.utils import CLIMATE_SECTION

header_vars = {
    CharacterVar('CLDESP', 70, spc=1, sect=CLIMATE_SECTION, info='Description of climate file.', right_align=False),
}

main_vars = {
    # CLIMATE
    CharacterVar('INSI', 4, spc=2, sect=CLIMATE_SECTION, info='Institute + Site code'),
    FloatVar('LAT', 8, 3, sect=CLIMATE_SECTION, info='Latitude, degrees (decimals)'),
    FloatVar('LONG', 8, 3, sect=CLIMATE_SECTION, info='Longitude, degrees (decimals)'),
    FloatVar('ELEV', 5, 0, sect=CLIMATE_SECTION, info='Elevation, m'),
    FloatVar('TAV', 5, 1, sect=CLIMATE_SECTION, info='Air temperature average, °C'),
    FloatVar('AMP', 5, 1, sect=CLIMATE_SECTION, info='Air temperature amplitude, monthly averages, °C'),
    FloatVar('SRAY', 5, 1, sect=CLIMATE_SECTION, info='Solar radiation,yearly average, MJ m-2 day-1'),
    FloatVar('TMXY', 5, 1, sect=CLIMATE_SECTION, info=''),
    FloatVar('TMNY', 5, 1, sect=CLIMATE_SECTION, info=''),
    IntegerVar('RAIY', 5, sect=CLIMATE_SECTION, info='Rainfall,yearly total, mm '),

    IntegerVar('START', 5, spc=0, sect=CLIMATE_SECTION, info='Start of summary period for climate (CLI) files, Year'),
    IntegerVar('DURN', 5, sect=CLIMATE_SECTION, info='Duration of summarization period for climate files, Yr'),
    FloatVar('ANGA', 5, 2, sect=CLIMATE_SECTION, info='Angstrom "a" coefficient'),
    FloatVar('ANGB', 5, 2, sect=CLIMATE_SECTION, info='Angstrom "b" coefficient '),
    FloatVar('REFHT', 5, 1, sect=CLIMATE_SECTION, info='Reference height for weather measurements, m'),
    FloatVar('WNDHT', 5, 1, sect=CLIMATE_SECTION, info='Reference height for windspeed measurements, m '),
    CharacterVar('SOURCE', 50, sect=CLIMATE_SECTION, info='', right_align=False),
    IntegerVar('GSST', 5, sect=CLIMATE_SECTION, info='Growing season start day, Doy'),
    IntegerVar('GSDU', 5, sect=CLIMATE_SECTION, info='Growing season duration, Day'),

    # MONTHLY AVERAGES
    IntegerVar('MTH', 5, spc=1, sect='MONTHLY AVERAGES', info=''),
    IntegerVar('MONTH', 5, spc=1, sect='MONTHLY AVERAGES', info=''),        # 'MONTH' variable name in some cli files.
    FloatVar('SAMN', 5, 1, spc=1, sect='MONTHLY AVERAGES', info=''),
    FloatVar('XAMN', 5, 1, spc=1, sect='MONTHLY AVERAGES', info=''),
    FloatVar('NAMN', 5, 1, spc=1, sect='MONTHLY AVERAGES', info=''),
    FloatVar('RTOT', 5, 1, spc=1, sect='MONTHLY AVERAGES', info=''),
    FloatVar('RNUM', 5, 1, spc=1, sect='MONTHLY AVERAGES', info=''),
    FloatVar('SHMN', 5, 1, spc=1, sect='MONTHLY AVERAGES', info=''),
    FloatVar('AMTH', 5, 3, spc=1, sect='MONTHLY AVERAGES', info=''),
    FloatVar('BMTH', 5, 3, spc=1, sect='MONTHLY AVERAGES', info=''),

    # WGEN PARAMETERS
    IntegerVar('MTH', 5, spc=1, sect='WGEN PARAMETERS', info=''),
    FloatVar('SDMN', 5, 1, spc=1, sect='WGEN PARAMETERS', info=''),
    FloatVar('SDSD', 5, 1, spc=1, sect='WGEN PARAMETERS', info=''),
    FloatVar('SWMN', 5, 1, spc=1, sect='WGEN PARAMETERS', info=''),
    FloatVar('SWSD', 5, 1, spc=1, sect='WGEN PARAMETERS', info=''),
    FloatVar('XDMN', 5, 1, spc=1, sect='WGEN PARAMETERS', info=''),
    FloatVar('XDSD', 5, 1, spc=1, sect='WGEN PARAMETERS', info=''),
    FloatVar('XWMN', 5, 1, spc=1, sect='WGEN PARAMETERS', info=''),
    FloatVar('XWSD', 5, 1, spc=1, sect='WGEN PARAMETERS', info=''),
    FloatVar('NAMN', 5, 1, spc=1, sect='WGEN PARAMETERS', info=''),
    FloatVar('NASD', 5, 1, spc=1, sect='WGEN PARAMETERS', info=''),
    FloatVar('ALPHA', 5, 3, spc=1, sect='WGEN PARAMETERS', info=''),
    FloatVar('RTOT', 5, 1, spc=1, sect='WGEN PARAMETERS', info=''),
    FloatVar('PDW', 5, 3, spc=1, sect='WGEN PARAMETERS', info=''),
    FloatVar('RNUM', 5, 1, spc=1, sect='WGEN PARAMETERS', info=''),

    # RANGE CHECK VALUES
    CharacterVar('SRAD', 11, spc=0, sect='RANGE CHECK VALUES'),
    FloatVar('TMAX', 5, 1, spc=1, sect='RANGE CHECK VALUES', info=''),
    FloatVar('TMIN', 5, 1, spc=1, sect='RANGE CHECK VALUES', info=''),
    FloatVar('RAIN', 5, 1, spc=1, sect='RANGE CHECK VALUES', info=''),
    FloatVar('DEWP', 5, 1, spc=1, sect='RANGE CHECK VALUES', info=''),
    FloatVar('WIND', 5, 1, spc=1, sect='RANGE CHECK VALUES', info=''),
    FloatVar('SUNH', 5, 1, spc=1, sect='RANGE CHECK VALUES', info=''),
    FloatVar('PAR', 5, 1, spc=1, sect='RANGE CHECK VALUES', info=''),
    FloatVar('TDRY', 5, 1, spc=1, sect='RANGE CHECK VALUES', info=''),
    FloatVar('TWET', 5, 1, spc=1, sect='RANGE CHECK VALUES', info=''),
    FloatVar('EVAP', 5, 1, spc=1, sect='RANGE CHECK VALUES', info=''),
    FloatVar('RHUM', 5, 1, spc=1, sect='RANGE CHECK VALUES', info=''),

    # FLAGGED DATA COUNT
    IntegerVar('BEGYR', 11, spc=1, sect='FLAGGED DATA COUNT', info=''),
    IntegerVar('BEGMN', 5, spc=1, sect='FLAGGED DATA COUNT', info=''),
    IntegerVar('BEGDY', 5, spc=1, sect='FLAGGED DATA COUNT', info=''),
    IntegerVar('ENDYR', 5, spc=1, sect='FLAGGED DATA COUNT', info=''),
    IntegerVar('ENDMN', 5, spc=1, sect='FLAGGED DATA COUNT', info=''),
    IntegerVar('ENDDY', 5, spc=1, sect='FLAGGED DATA COUNT', info=''),

    CharacterVar('TOTAL', 15, spc=0, sect='FLAGGED DATA COUNT'),
    IntegerVar('RAIN', 6, spc=1, sect='FLAGGED DATA COUNT', info=''),
    IntegerVar('TMAX', 6, spc=1, sect='FLAGGED DATA COUNT', info=''),
    IntegerVar('TMIN', 6, spc=1, sect='FLAGGED DATA COUNT', info=''),
    IntegerVar('SRAD', 6, spc=1, sect='FLAGGED DATA COUNT', info=''),
    IntegerVar('SUNH', 6, spc=1, sect='FLAGGED DATA COUNT', info=''),
    IntegerVar('DEWP', 6, spc=1, sect='FLAGGED DATA COUNT', info=''),
    IntegerVar('WIND', 6, spc=1, sect='FLAGGED DATA COUNT', info=''),
    IntegerVar('PAR', 6, spc=1, sect='FLAGGED DATA COUNT', info=''),
    IntegerVar('TDRY', 6, spc=1, sect='FLAGGED DATA COUNT', info=''),
    IntegerVar('TWET', 6, spc=1, sect='FLAGGED DATA COUNT', info=''),
    IntegerVar('EVAP', 6, spc=1, sect='FLAGGED DATA COUNT', info=''),
    IntegerVar('RHUM', 6, spc=1, sect='FLAGGED DATA COUNT', info=''),

}
