from gendiff.engine import output_file
import os
from gendiff.scripts.gendiff import main


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)    


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


result_data = read(get_fixture_path('result.txt')).rstrip().split('\n\n\n')
file1_json = get_fixture_path('file1.json')
file2_json = get_fixture_path('file2.json')
file3_json = get_fixture_path('file3.json')
file1_yml = get_fixture_path('file1.yml')
file2_yml = get_fixture_path('file2.yml')
file3_yaml = get_fixture_path('file3.yaml')


def test_same_files_json():
    assert output_file(file3_json, file3_json) == result_data[1]


def test_diff_files_json():
    assert output_file(file1_json, file2_json) == result_data[0]


def test_diff_files_yml():
    assert output_file(file1_yml, file2_yml) == result_data[0]


def test_same_files_yaml():
    assert output_file(file3_yaml, file3_yaml) == result_data[2]