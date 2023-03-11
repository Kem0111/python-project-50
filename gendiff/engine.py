from gendiff.formatter.json import json
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.function_tools.file_reading import read_file


STRING_FORMAT = {
    'stylish': stylish,
    'plain': plain,
    'json': json
}


def generate_diff(file_path1, file_path2, formatter='stylish'):
    file1_data, file2_data = read_file(file_path1, file_path2)
    format_function = STRING_FORMAT[formatter]
    return format_function(file1_data, file2_data)
