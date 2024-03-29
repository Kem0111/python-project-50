from gendiff.engine import generate_diff
import os
import pytest


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


result_data = read(get_fixture_path('result_stylish.txt'))
nested_file1_json = get_fixture_path('nested_file1.json')
nested_file2_json = get_fixture_path('nested_file2.json')
nested_file1_yaml = get_fixture_path('nested_file1.yml')
nested_file2_yaml = get_fixture_path('nested_file2.yaml')


@pytest.mark.parametrize("file1, file2", [
    (nested_file1_json, nested_file2_json),
    (nested_file1_json, nested_file2_yaml),
    (nested_file1_yaml, nested_file2_yaml),
])
def test_stylish(file1, file2):
    assert generate_diff(file1, file2) == result_data
