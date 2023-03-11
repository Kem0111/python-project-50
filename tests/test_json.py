from tests import test_stylish
from gendiff.gendiff import generat_diff


result = test_stylish.read(test_stylish.get_fixture_path('result.json'))


FORMAT = 'json'


def test_json_files():
    assert generat_diff(test_stylish.nested_file1_json, test_stylish.nested_file2_json, FORMAT) == result


def test_yaml_files():
    assert generat_diff(test_stylish.nested_file1_yaml, test_stylish.nested_file2_yaml, FORMAT) == result