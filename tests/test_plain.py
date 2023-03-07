from tests import test_stylish
from gendiff.plain import plain


result_data = test_stylish.read(test_stylish.get_fixture_path('result_plain.txt')).rstrip().split('\n\n\n')

def test_plain_files():
    assert plain(test_stylish.plain_file1_json, test_stylish.plain_file2_json)== result_data[1]
    assert plain(test_stylish.plain_file1_yaml, test_stylish.plain_file2_yaml)== result_data[1]


def test_nested_files():
    assert plain(test_stylish.nested_file1_json, test_stylish.nested_file2_json)== result_data[0]
    assert plain(test_stylish.nested_file1_yaml, test_stylish.nested_file2_yaml)== result_data[0]
