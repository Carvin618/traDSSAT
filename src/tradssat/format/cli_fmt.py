# XXX_H: The fortran format expression for header which is start with '@'.
# XXX_S: The fortran format expression for section which is start with '*'.
# XXX_V: The fortran format expression for variable name.
# XXX_L: The fortran format expression for variable value.

# CLIMATE:
CLIMATE_S = '1X,A70'

# Line 2
CLI_FIRST_LINE_V = '1X,A5,2(1X,A8),7(1X,A5)'
CLI_FIRST_LINE_L = '1X,A5,2(1X,F8.3),1X,F5.0,5(1X,F5.1),1X,I5'
CLI_SECOND_LINES_V = '1X,A5,5(1X,A5),1X,A50'
CLI_SECOND_LINES_L = '2(1X,I5),2(1X,F5.2),2(1X,F5.1),1X,A50'
CLI_THIRD_LINES_V = '2(1X,A5)'
CLI_THIRD_LINES_L = '2(1X,I5)'

# MONTHLY AVERAGES
MTH_AVG_S = 'A16'
MTH_AVG_V = '9(1X,A5)'
MTH_AVG_L = '1X,I5,6(1X,F5.1),2(1X,F5.3) '

# RANGE CHECK VALUES
RANGE_CHECK_S = 'A18'
RANGE_CHECK_V = 'A11,11(1X,A5)'
RANGE_CHECK_L = 'A11,11(1X,F5.1)'

# WGEN PARAMETERS
WGEN_PARAMS_S = 'A14'
WGEN_PARAMS_V = '15(1X,A5)'
WGEN_PARAMS_L = '1X,I5,10(1X,F5.1),2(1X,F5.3,1X,F5.1)'

# FLAGGED DATA COUNT
FLAGGED_DATA_S = 'A18'
FLAGGED_DATA_FIRST_LINE_V = '6(1X,A5)'
FLAGGED_DATA_FIRST_LINE_L = '6(1X,I5)'
FLAGGED_DATA_OTHER_LINES_V = 'A15,12(1X,A6)'
FLAGGED_DATA_OTHER_LINES_L = 'A15,12(1X,I6)'
