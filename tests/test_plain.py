from tests import test_stylish
from gendiff.engine import generat_diff


result_data = test_stylish.read(test_stylish.get_fixture_path('result_plain.txt')).rstrip().split('\n\n\n')

FORMAT = 'plain'

def test_plain_files():
    assert generat_diff(test_stylish.plain_file1_json, test_stylish.plain_file2_json, FORMAT)== result_data[1]
    assert generat_diff(test_stylish.plain_file1_yaml, test_stylish.plain_file2_yaml, FORMAT)== result_data[1]


def test_nested_files():
    assert generat_diff(test_stylish.nested_file1_json, test_stylish.nested_file2_json, FORMAT)== result_data[0]
    assert generat_diff(test_stylish.nested_file1_yaml, test_stylish.nested_file2_yaml, FORMAT)== result_data[0]
