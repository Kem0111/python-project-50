from gendiff.function_tools.file_difference import get_diff
from gendiff.function_tools.stringify_stylish import stringify


KEY_SYMB = {
    'removed': '- ',
    'added': '+ ',
    'unchanged': '  ',
    'nested': '  ',
    'changed': '',
}


def stylish(data1, data2):
    data_diff = get_diff(data1, data2)
    return stringify(data_diff, KEY_SYMB)
