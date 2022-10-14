import os
from tradssat import ExpFile
import fortranformat as ff


def test_expfile():
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
    print("Get variable 'FAMN': ", exp.get_value('FAMN', sect='FERTILIZERS (INORGANIC)'))
    print("Set variable 'FAMN': ", exp.set_value('FAMN', 100, cond={'F': 1}))
    # for func in var_methods.values():
    #     print(func.__name__, func(var='CU'))
    exp.write('IUAF9901.MZX')


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
    test_expfile()
    # check_weather()
    # fortran_format()