from gendiff.generate_diff import generate_diff
import os


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


def test_diff_files():
    assert generate_diff(file1_json, file2_json) == result_data[0]


def test_same_files():
    assert generate_diff(file3_json, file3_json) == result_data[1]
