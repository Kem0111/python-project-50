from gendiff.stylish import stylish
import os


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)    


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


result_data = read(get_fixture_path('nested.txt')).rstrip().split('\n\n\n')
file1_json = get_fixture_path('nested_file1.json')
file2_json = get_fixture_path('nested_file2.json')
file1_yaml = get_fixture_path('nested_file1.yml')
file2_yaml = get_fixture_path('nested_file2.yaml')


def test_diff_json_files():
    assert stylish(file1_json, file2_json) == result_data[3]


def test_diff_same_yaml_files():
    assert stylish(file1_yaml, file2_yaml) == result_data[3]


def test_yml_json_file():
    assert stylish(file1_json, file2_yaml) == result_data[3]
