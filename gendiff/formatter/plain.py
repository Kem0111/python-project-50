from gendiff.function_tools.stringify_plain import stringify
from gendiff.function_tools.file_difference import get_diff


PLAIN_OUTPUT = {
    'removed': "Property '{}' was removed",
    'added': "Property '{}' was added with value: {}",
    'changed': "Property '{}' was updated. From {} to {}",
    'unchanged': ''
}


def plain(data1, data2):
    data_diff = get_diff(data1, data2)
    return stringify(data_diff, PLAIN_OUTPUT)
