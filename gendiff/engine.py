from typing import Callable, Dict
from gendiff.formatter.json import json
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.tree_structure import get_diff
from gendiff.parser import parse_data
import os


OUTPUT_FORMATS: Dict[str, Callable] = {
    'stylish': stylish,
    'plain': plain,
    'json': json
}


def generate_diff(file1_path, file2_path, formatter='stylish'):
    """
    Compare two files and generate a diff string in the specified format.

    Args:
        file1_path: Path to the first file.
        file2_path: Path to the second file.
        formatter: Output format for the diff string (default: 'stylish').

    Returns:
        A formatted diff string representing the differences
        between the two files.
    """

    if formatter not in OUTPUT_FORMATS:
        raise ValueError(
            'Unsupported format. Expected {}'.format(OUTPUT_FORMATS.keys())
        )
    file1_data, file2_data = read_file(file1_path), read_file(file2_path)
    file1_format = get_format(file1_path)
    file2_format = get_format(file2_path)
    data1 = parse_data(file1_data, file1_format)
    data2 = parse_data(file2_data, file2_format)
    data_diff = get_diff(data1, data2)
    format_function = OUTPUT_FORMATS[formatter]
    return format_function(data_diff)


def read_file(file_path):
    with open(file_path, 'r') as file:
        first_data = file.read()
    return first_data


def get_format(file_path):
    return os.path.splitext(file_path)[1]
