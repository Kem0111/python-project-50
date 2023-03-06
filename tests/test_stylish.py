from gendiff.stylish import stylish
import os


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)    


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


result_data = read(get_fixture_path('result.txt')).rstrip().split('\n\n\n')
plain_file1_json = get_fixture_path('file1.json')
plain_file2_json = get_fixture_path('file2.json')
plain_file1_yaml = get_fixture_path('file1.yml')
plain_file2_yaml = get_fixture_path('file2.yml')
nested_file1_json = get_fixture_path('nested_file1.json')
nested_file2_json = get_fixture_path('nested_file2.json')
nested_file1_yaml = get_fixture_path('nested_file1.yml')
nested_file2_yaml = get_fixture_path('nested_file2.yaml')


def test_diff_plain_json_fiiles():
    assert stylish(plain_file1_json, plain_file2_json) == result_data[0]


def test_same_file():
    assert stylish(plain_file1_json, plain_file1_json) == result_data[1]


def test_diff_plain_yaml_fiiles():
    assert stylish(plain_file1_yaml, plain_file2_yaml) == result_data[0]


def test_diff_nested_json_files():
    assert stylish(nested_file1_json, nested_file2_json) == result_data[2]


def test_diff_nested_yaml_files():
    assert stylish(nested_file1_yaml, nested_file2_yaml) == result_data[2]


def test_nested_yml_json_file():
    assert stylish(nested_file1_json, nested_file2_yaml) == result_data[2]
