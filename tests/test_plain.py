from tests import test_stylish
from gendiff.engine import generate_diff


result_data = test_stylish.read(test_stylish.get_fixture_path('result_plain.txt'))
FORMAT = 'plain'


def test_nested_files():
    assert generate_diff(test_stylish.nested_file1_json, test_stylish.nested_file2_json, FORMAT) == result_data
    assert generate_diff(test_stylish.nested_file1_yaml, test_stylish.nested_file2_yaml, FORMAT) == result_data
