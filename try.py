import os
from tradssat import ExpFile, WTHFile, SoilFile, CULFile, ECOFile, CLIFile
import fortranformat as ff


def expfile():
    xfile = 'C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-data\\Soybean\\IUAM8801.SBX'
    exp = ExpFile(xfile)
    var_methods = {
        'var': exp.get_var,
        'value': exp.get_value,
        'var_spc': exp.get_var_spc,
        'dims_var': exp.get_dims_val,
        'var_size': exp.get_var_size,
        'var_doce': exp.get_var_code_miss,
        'var_lims': exp.get_var_lims,
        'var_type': exp.get_var_type,
    }
    # print("Get variable 'FMOPT': ", exp.get_value('FMOPT'))
    #print("Set variable 'FMOPT': ", exp.set_value('FMOPT', 100, cond={'F': 1}))
    # for func in var_methods.values():
    #     print(func.__name__, func(var='CU'))
    exp.write('IUAM8801.SBX')


def add_var_exp():
    # xfile = 'C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-data\\Soybean\\IUAM8801.SBX'
    xfile = 'C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-data\\Sequence\\CHWC0012_modified.SQX'
    exp = ExpFile(xfile)
    # exp.set_value('ENAME', 'xxxxxxx', header=True)
    # print("Variable 'ENAME': ", exp.get_value('ENAME'))
    # exp.set_value('FNAME', 'Y')
    # print("Variable 'FMOPT': ", exp.get_var('FMOPT'), exp.get_value('FMOPT'))
    # print("Set variable 'FMOPT': ", exp.set_value('FMOPT', 100, cond={'F': 1}))
    # for func in var_methods.values():
    #     print(func.__name__, func(var='CU'))
    print()
    print(exp.get_var('FMOPT'))
    exp.add_var('IRVAL', {0: 29, 1: 28, 2: 27, 3: 28, 4: 27, 5: 28, 6: 31, 7: 28, 8: 32, 9: 34, 10: 28,}, subsect=1)

    # exp.set_value('OPOUT', 'Y')
    # exp.set_value('FMOPT', '')
    print(exp.get_value('IRVAL', subsect=1))
    exp.write('CHWC0012.SQX')


def soilfile():
    sfile = "C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-data\\Soil\\SOIL.SOL"
    sol = SoilFile(sfile)

    sol.write('SOIL.SOL')


def add_var_soil():
    sfile = "C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-data\\Soil\\SOIL.SOL"
    sol = SoilFile(sfile)

    #print(sol.get_value('SLLL', sect='IB00000001'))
    #sol.set_value('SLLL', val=0.3, sect='IB00000001', cond={'SLB': 5})
    sol.add_var('SADC', vals=[-99, -99, -99, -99, -99, -99, -99, -99], sect='IN00020001', subsect=2)
    print(sol.get_value('SADC', sect='IN00020001'))
    sol.write('SOIL.SOL')


def wth_file():
    filew = 'C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-data\\Weather\\IUAF8801.WTH'
    wth = WTHFile(filew)
    wth.write('IUAF8801.WTH')


def cli_file():
    cli_file = 'C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-data\\Weather\\Climate\\CHER.CLI'
    cli = CLIFile(cli_file)
    cli.write('CHER.CLI')


def add_var_wth():
    filew = 'C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-data\\Weather\\IUAF8801.WTH'
    wth = WTHFile(filew)

    wth.add_var('DEWP', vals=[1 for _ in range(366)], subsect=1, sect='WEATHER DATA :')
    wth.write('IUAF8801.WTH')

    filew = 'C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-data\\Weather\\DTCM6301.WTH'
    wth = WTHFile(filew)

    # wth.add_var('EVAP', vals=[1 for _ in range(364)], subsect=1, sect='WEATHER :')
    wth.write('DTCM6301.WTH')


def cul_file():
    cfile = "C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-os\\Data\\Genotype\\ALFRM048.CUL"
    cul = CULFile(cfile)

    cul.write('ALFRM048.CUL')


def fortran_format():
    header_line = ff.FortranRecordReader('(////,3X,A2)')
    line = header_line.read('*EXP.DETAILS: CHWC0012SQ CHILLICOTHE, TX WHEAT COTTON ROTATION-IRRIGATED')
    print(line)
    print([len(x) for x in line if type(x) == str])

    # line = ff.FortranRecordReader('(3F15.3)')
    # print(line.read('          1.000          0.000          0.500'))
    #
    # # Returns [1.0, 0.0, 0.5]
    # print(line.read('          1.100          0.100          0.600'))
    # # Returns [1.1, 0.1, 0.6]
    # print(line)


if __name__ == '__main__':
    expfile()
    add_var_exp()
    soilfile()
    add_var_soil()
    wth_file()
    add_var_wth()
    cli_file()
    fortran_format()