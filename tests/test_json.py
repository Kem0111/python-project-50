import pytest
from tests import test_stylish
from gendiff.engine import generate_diff
import json


result = test_stylish.read(test_stylish.get_fixture_path('result.json'))


@pytest.mark.parametrize("file1, file2", [
    (test_stylish.nested_file1_json, test_stylish.nested_file2_json),
    (test_stylish.nested_file1_yaml, test_stylish.nested_file2_yaml),
])
def test_json_files(file1, file2, format_='json'):
    assert generate_diff(file1, file2, format_) == result
    assert json.loads(generate_diff(file1, file2, format_))
