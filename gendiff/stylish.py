from gendiff.function_tools.file_reading import extract_file_data
from gendiff.function_tools.file_difference import make_diff_data
from gendiff.function_tools.stringify_data import stringify


PERMANENT_INDENT = 4
SPECIAL_SYMB = ' '
LEFT_SHIFT = 2


def stylish(file_path1, file_path2):
    first_file_data, second_file_data = extract_file_data(file_path1, file_path2)
    data_diference = make_diff_data(first_file_data, second_file_data)
    return stringify(data_diference, PERMANENT_INDENT, SPECIAL_SYMB, LEFT_SHIFT)
