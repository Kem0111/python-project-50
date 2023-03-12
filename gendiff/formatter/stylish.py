from gendiff.function_tools.file_difference import get_diff
from gendiff.function_tools.stringify_data import stringify


KEY_INDENT = {
    'added': '+ ',
    'removed': '- ',
    'unchanged': '  '
}


def stylish(data1, data2):
    data_diff = get_diff(data1, data2, KEY_INDENT)
    return stringify(data_diff)
