import pytest
from tests import test_stylish
from gendiff.engine import generate_diff


result = test_stylish.read(test_stylish.get_fixture_path('result.json'))


FORMAT = 'json'

@pytest.mark.parametrize("file1, file2, format_", [
    (test_stylish.nested_file1_json, test_stylish.nested_file2_json, FORMAT),
    (test_stylish.nested_file1_yaml, test_stylish.nested_file2_yaml, FORMAT),
])
def test_json_files(file1, file2, format_):
    assert generate_diff(file1, file2, format_) == result
