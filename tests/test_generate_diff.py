from gendiff.generate_diff import generate_diff
import os


# def test_compair_files():
#     file1 = 'tests/fixtures/file1.json'
#     file2 = 'tests/fixtures/file1.json'

def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)    


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


result_data = get_fixture_path('result.txt')
file1_json = get_fixture_path('file1.json')
file2_json = get_fixture_path('file2.json')
assert generate_diff(file1_json, file2_json) == read(result_data)