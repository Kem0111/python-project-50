from tests import test_stylish
from gendiff.json import json


result = test_stylish.read(test_stylish.get_fixture_path('result.json'))


def test_json_files():
    assert json(test_stylish.nested_file1_json, test_stylish.nested_file2_json) == result


def test_yaml_files():
    assert json(test_stylish.nested_file1_yaml, test_stylish.nested_file2_yaml) == result