from gendiff.formatter.json import json
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.function_tools.file_reading import read_file


OUTPUT_FORMATS = {
    'stylish': stylish,
    'plain': plain,
    'json': json
}


def generate_diff(file1_path, file2_path, formatter='stylish'):
    file1_data, file2_data = read_file(file1_path, file2_path)
    format_function = OUTPUT_FORMATS[formatter]
    return format_function(file1_data, file2_data)
