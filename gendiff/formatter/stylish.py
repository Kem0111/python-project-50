from gendiff.function_tools.file_difference import get_diff
from gendiff.function_tools.stringify_data import stringify


INDENT = '  '


def stylish(data1, data2):
    data_diff = get_diff(data1, data2, INDENT)
    return stringify(data_diff)
