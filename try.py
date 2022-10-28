import os
from tradssat import (ExpFile, WTHFile, SoilFile, CULFile, ECOFile,
                      CLIFile, DSSATRun, set_dssat_dir, GeneticMgr, SoilMgr, WeatherFileMgr)

import fortranformat as ff


def expfile():
    xfile = 'C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-data\\Maize\\IUAF9901.MZX'
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

    sfile = "C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-data\\Soil\\AG.SOL"
    sol = SoilFile(sfile)

    sol.write('AG.SOL')


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

    cfile = "C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-os\\Data\\Genotype\\BACER048.CUL"
    cul = CULFile(cfile)
    cul.write('BACER048.CUL')


def eco_file():
    ecofile = "C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-os\\Data\\Genotype\\ALFRM048.ECO"
    eco = ECOFile(ecofile)
    eco.write('ALFRM048.ECO')

    ecofile = "C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-os\\Data\\Genotype\\BACER048.ECO"
    eco = ECOFile(ecofile)
    eco.write('BACER048.ECO')


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


def exp_file_mgr():
    set_dssat_dir('C:\\Users\\57block\\workspace\\dssat\\data\\exp_example_win')
    path = 'C:\\Users\\57block\\workspace\\dssat\\data\\exp_example_win\\IUAF9901.MZX'
    run = DSSATRun(path)

    # Get cultivar for treatment 1
    run.get_trt_val('INGENO', trt=1)

    # Change level of treatment factor
    run.set_trt_factor_level(trt=1, factor='CULTIVARS', level=2)

    # Change value of a factor level (in this case cultivar type)
    run.set_factor_level_val('INGENO', 'IB0067', level=1)

    # Access soil variable SLLL for treatment 2
    run.get_trt_val('SLLL', trt=2)


def gen_file_mgr():
    gen = GeneticMgr(crop='MZIXM', cult='PC0001')

    # Returns P1 for MZIXM cultivar PC0001
    gen.get_value('P1')

    # Returns ecotype variable TOPT for cultivar PC001
    gen.get_value('TOPT')


def soil_file_mgr():
    soil_mgr = SoilMgr('IB00000005')
    soil_mgr.get_value('SLU1')


def weather_file_mgr():
    wth_mgr = WeatherFileMgr('ACNM')
    wth_mgr.get_value('RAIN')


if __name__ == '__main__':
    set_dssat_dir('C:\\Users\\57block\\workspace\\dssat\\data\\exp_example_win')

    # expfile()
    # add_var_exp()
    # soilfile()
    # add_var_soil()
    # wth_file()
    # add_var_wth()
    # cli_file()
    # fortran_format()
    # cul_file()
    # eco_file()
    # exp_file_mgr()
    # gen_file_mgr()
    # soil_file_mgr()
    weather_file_mgr()
