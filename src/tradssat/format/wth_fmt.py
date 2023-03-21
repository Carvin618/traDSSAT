# XXX_H: The fortran format expression for header which is start with '@'.
# XXX_S: The fortran format expression for section which is start with '*'.
# XXX_V: The fortran format expression for variable name.
# XXX_L: The fortran format expression for variable value.

# Line 1
WEATHER_S = '1X,A70'

# Line 2
WTH_FIRST_LINE_V = '1X,A5,2(1X,A8),5(1X,A5)'
WTH_FIRST_LINE_L = '1X,A5,2(1X,F8.3),1X,F5.0,4(1X,F5.1),1X,F5.0'
WTH_OTHER_LINES_V = 'A5,9(1X,A5)'
WTH_OTHER_LINES_L = 'A5,9(1X,F5.1)'
