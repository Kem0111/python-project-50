from gendiff.formatter.json import json
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.tree_structure import get_diff
from gendiff.parser import parse_data
import os


OUTPUT_FORMATS = {
    'stylish': stylish,
    'plain': plain,
    'json': json
}


def generate_diff(file1_path, file2_path, formatter='stylish'):
    if formatter not in OUTPUT_FORMATS:
        raise ValueError(
            'Unsupported format. Expected {}'.format(OUTPUT_FORMATS.keys())
            )
    file1_data, file2_data = read_files(file1_path, file2_path)
    file1_format, file2_format = extract_formats(file1_path, file2_path)
    data1 = parse_data(file1_data, file1_format)
    data2 = parse_data(file2_data, file2_format)
    data_diff = get_diff(data1, data2)
    format_function = OUTPUT_FORMATS[formatter]
    return format_function(data_diff)


def read_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1,\
         open(file2_path, 'r') as file2:
        first_data = file1.read()
        second_data = file2.read()
    return first_data, second_data


def extract_formats(file1_path, file2_path):
    return os.path.splitext(file1_path)[1], os.path.splitext(file2_path)[1]
