from gendiff.function_tools.file_reading import extract_file_data
from gendiff.function_tools.file_difference import get_generate_diff
from json import dumps


INDENT = ''


def json(file1_path, file2_path):
    first_file_data, second_file_data = extract_file_data(file1_path,
                                                          file2_path)
    data = get_generate_diff(first_file_data, second_file_data, INDENT)
    stylish_data = dumps(data, indent=2)
    return stylish_data
