# XXX_H: The fortran format expression for header which is start with '@'.
# XXX_S: The fortran format expression for section which is start with '*'.
# XXX_V: The fortran format expression for variable name.
# XXX_L: The fortran format expression for variable value.

# SECTION NAMES
CULTIVAR_S = '1X,A70'
ECOTYPE_S = '1X,A70'

# STANDARD CULTIVARS
CULTIVAR_GRO_V = '1X,A4,2X,A16,1X,A5,1X,A6,18(1X,A5)'
CULTIVAR_GRO_L = ('A6,1X,A16,A6,1X,A6,F6.1,F6.3,3(F6.1),3(F6.2),' 
                  'F6.0,F6.1,F6.2,F6.3,F6.1,F6.2,2(F6.1),2(F6.3)')

# SPECIAL CULTIVARS
CULTIVAR_SIM_V = '1X,A4,2X,A16,1X,A5,1X,A6,9(1X,A5)'
CULTIVAR_SIM_L = 'A6,1X,A16,1X,A5,1X,A6,1X,F5.1,1X,F5.2,1X,F5.1,2(1X,F5.1),4(1X,F5.2),1X,F5.1'

# STANDARD ECOTYPE
ECOTYPE_GRO_V = '1X,A4,2X,A17,2(1X,A2),20(1X,A5)'
ECOTYPE_GRO_L = ('A6,1X,A17,2(1X,A2),1X,F5.2,3(1X,F5.1),1X,F5.0,1X,F5.1,1X,F5.2,1X,F5.1,2(1X,F5.0),1X,F5.2,2(1X,F5.1)'
                 '1X,F5.3,1X,F5.1,5(1X,F5.3)')

# SPECIAL ECOTYPE
ECOTYPE_SIM_V = '1X,A4,2X,A5,32(1X,A5)'
ECOTYPE_SIM_L = ('A6,1X,F5.0,1X,F5.2,2(1X,F5.0),2(1X,F5.2),1X,F5.0,6(1X,F5.1),2(1X,F5.2),'
                 '1X,F5.0,9(1X,F5.1),1X,F5.0,1X,F5.1,1X,F5.2,1X,F5.0,2(1X,F5.1),1X,F5.0')


