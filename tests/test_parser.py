import requests
from gendiff.function_tools.parser import parse_data


json_data = requests.get("https://jsonplaceholder.typicode.com/posts/1").text


def test_parse_network():
    assert parse_data(json_data, '.json')
