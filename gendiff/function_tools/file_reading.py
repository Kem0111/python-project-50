from gendiff.function_tools.parser import parse_data
import os


def read_file(file1_path, file2_path):
    file1_format = os.path.splitext(file1_path)[1]
    file2_format = os.path.splitext(file2_path)[1]
    with open(file1_path, 'r') as file1,\
         open(file2_path, 'r') as file2:
        first_data = file1.read()
        second_data = file2.read()
    first_file_data = parse_data(first_data, file1_format)
    second_file_data = parse_data(second_data, file2_format)
    return first_file_data, second_file_data
