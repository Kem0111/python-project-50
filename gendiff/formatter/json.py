from gendiff.function_tools.file_difference import get_diff
from json import dumps


KEY_INDENT = {
    'added': '+ ',
    'removed': '- ',
    'unchanged': ''
}


def json(data1, data2):
    data_diff = get_diff(data1, data2, KEY_INDENT)
    stylish_data = dumps(data_diff, indent=2)
    return stylish_data
