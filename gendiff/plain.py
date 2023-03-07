from gendiff.function_tools.file_reading import extract_file_data
from gendiff.function_tools.plain_data import get_plain_data


def plain(file1_path, file2_path):
    first_file_data, second_file_data = extract_file_data(file1_path,
                                                          file2_path)
    return get_plain_data(first_file_data, second_file_data)
