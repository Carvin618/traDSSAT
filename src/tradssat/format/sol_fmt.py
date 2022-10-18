# *SOILS:
# Institute + Country Name
SOIL_S = '1X,A10'

# Subsequent lines relate to sections, as follows:
# Line 1:
SOIL_SITE_S = '2X,A11,1X,A5,1X,F5.0,1X,A50'

# Line 2:
SOL_SECOND_LINE_V = '2(1X,A11),2(1X,A8),1X,A50'
SOL_SECOND_LINE_L = '2(1X,A11),2(1X,F8.3),1X,A50'

# Line 3:
SOL_THIRD_LINE_V = '10(1X,A5)'
SOL_THIRD_LINE_L = '1X,A5,2(1X,F5.2,1X,F5.0),2(1X,F5.2),3(1X,A5)'

# Line 4 + (NL-1), where NL = number of layers. (L = Layer number)
SOL_NL_LINE_V = '17(1X,A5)'
SOL_NL_LINE_L = '1X,F5.0,1X,A5,3(1X,F5.3),1X,F5.2,1X,F5.1,2(1X,F5.2),8(1X,F5.1)'

# Line 4 + NL to (4 + NL + (NL - 1)), where NL = number of layers. (L = Layer number)
SOL_NL_TO_4NL_FIRST_LINE_V = '16(1X,A5)'
SOL_NL_TO_4NL_FIRST_LINE_L = '1X,F5.0,15(1X,F5.1)'
