import os
from tradssat import ExpFile, WTHFile, SoilFile
import fortranformat as ff


# def test_expfile():
#     xfile = 'C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-data\\Soybean\\IUAM8801.SBX'
#     exp = ExpFile(xfile)
#     var_methods = {
#         'var': exp.get_var,
#         'value': exp.get_value,
#         'var_spc': exp.get_var_spc,
#         'dims_var': exp.get_dims_val,
#         'var_size': exp.get_var_size,
#         'var_doce': exp.get_var_code_miss,
#         'var_lims': exp.get_var_lims,
#         'var_type': exp.get_var_type,
#     }
#     print("Get variable 'FMOPT': ", exp.get_value('FMOPT'))
#     #print("Set variable 'FMOPT': ", exp.set_value('FMOPT', 100, cond={'F': 1}))
#     # for func in var_methods.values():
#     #     print(func.__name__, func(var='CU'))
#     exp.write('IUAM8801.SBX')

def test_add_var():
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

def test_soilfile():
    sfile = "C:\\Users\\57block\\workspace\\dssat\\data\\dssat-csm-data\\Soil\\SOIL.SOL"
    sol = SoilFile(sfile)

    sol.write('SOIL.SOL')

# def check_weather():
#     weather_dir = 'C:/Users/57block/workspace/dssat/data/dssat-csm-data/Weather'
#     sequence_dir = 'C:/Users/57block/workspace/dssat/data/dssat-csm-data/Sequence'
#
#     weather_files = os.listdir(weather_dir)
#     sequence_files = os.listdir(sequence_dir)
#
#     #print(weather_files[0])
#     #print(squence_files[0])
#
#     common_file = []
#
#     for f in sequence_files:
#         if f.split('.')[0] in weather_files:
#             common_file.append(f)
#
#     print(common_file)
#

# def fortran_format():
#     header_line = ff.FortranRecordReader('(////,3X,A2)')
#     line = header_line.read('*EXP.DETAILS: CHWC0012SQ CHILLICOTHE, TX WHEAT COTTON ROTATION-IRRIGATED')
#     print(line)
#     print([len(x)  for x in line if type(x) == str])
#
#     # line = ff.FortranRecordReader('(3F15.3)')
#     # print(line.read('          1.000          0.000          0.500'))
#     #
#     # # Returns [1.0, 0.0, 0.5]
#     # print(line.read('          1.100          0.100          0.600'))
#     # # Returns [1.1, 0.1, 0.6]
#     # print(line)


if __name__ == '__main__':
    # test_expfile()
    # test_add_var()
    # test_soilfile()
    # check_weather()
    # fortran_format()