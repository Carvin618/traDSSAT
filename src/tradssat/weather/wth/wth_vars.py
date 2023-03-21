from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar
from tradssat.format.utils import WEATHER_SECTION


header_vars = {
    # Self Defined Variable. Document doesn't specify this variable.
    CharacterVar('WSDESP', 70, spc=0, sect=WEATHER_SECTION, info='Description of Weather Station.', right_align=False)
}

main_vars = {
    CharacterVar('INSI', 4, spc=2, sect=WEATHER_SECTION, info='Institute + Site code'),
    FloatVar('LAT', 8, 3, sect=WEATHER_SECTION, info='Latitude, degrees (decimals)'),
    FloatVar('LONG', 8, 3, sect=WEATHER_SECTION, info='Longitude, degrees (decimals)'),
    FloatVar('ELEV', 5, 0, sect=WEATHER_SECTION, info='Elevation, m'),
    FloatVar('TAV', 5, 1, sect=WEATHER_SECTION, info='Air temperature average, °C'),
    FloatVar('AMP', 5, 1, sect=WEATHER_SECTION, info='Air temperature amplitude, monthly averages, °C'),
    FloatVar('REFHT', 5, 1, sect=WEATHER_SECTION, info='Height of temperature measurements, m'),
    FloatVar('WNDHT', 5, 1, sect=WEATHER_SECTION, info='Height of wind measurements, m'),
    IntegerVar('CCO2', 4, sect=WEATHER_SECTION, info='Atmospheric CO2, ppm'),

    CharacterVar('DATE', 5, spc=0, sect=WEATHER_SECTION, info='Year + days from Jan. 1'),
    FloatVar('SRAD', 5, 1, sect=WEATHER_SECTION, info='Solar radiation, MJ m-2 day-1'),
    FloatVar('TMAX', 5, 1, sect=WEATHER_SECTION, info='Air temperature maximum, °C'),
    FloatVar('TMIN', 5, 1, sect=WEATHER_SECTION, info='Air temperature minimum, °C'),
    FloatVar('RAIN', 5, 1, sect=WEATHER_SECTION, info='Precipitation, mm'),
    FloatVar('DEWP', 5, 1, sect=WEATHER_SECTION, info='Dewpoint temperature5, °C'),
    FloatVar('WIND', 5, 1, sect=WEATHER_SECTION, info='Wind run, km day-1'),
    FloatVar('PAR', 5, 1, sect=WEATHER_SECTION, info='Photosynthetic active radiation (PAR)5, moles m-2 day-1'),
    FloatVar('EVAP', 5, 1, sect=WEATHER_SECTION, ),
    FloatVar('RHUM', 5, 1, sect=WEATHER_SECTION, )
}
