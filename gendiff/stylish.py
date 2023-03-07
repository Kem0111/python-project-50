from gendiff.function_tools.file_reading import extract_file_data
from gendiff.function_tools.file_difference import generate_diff
from gendiff.function_tools.stringify_data import stringify


def stylish(file1_path, file2_path):
    first_file_data, second_file_data = extract_file_data(file1_path,
                                                          file2_path)
    data_difference = generate_diff(first_file_data, second_file_data)
    return stringify(data_difference)
