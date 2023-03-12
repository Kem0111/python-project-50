from gendiff.engine import generate_diff
import os


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


def test_stylish_json():
    assert generate_diff(nested_file1_json, nested_file2_json) == result_data


def test_stylish_json_yaml():
    assert generate_diff(nested_file1_json, nested_file2_yaml) == result_data


def test_diff_stylish_yaml():
    assert generate_diff(nested_file1_yaml, nested_file2_yaml) == result_data
