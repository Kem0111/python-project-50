import json
import yaml


def extract_file_data(first_file_path, second_file_path):
    first_file_data = get_file_data(first_file_path)
    second_file_data = get_file_data(second_file_path)
    return first_file_data, second_file_data


def get_file_data(file_path):
    with open(file_path, 'r') as file:
        if file_path.endswith('json'):
            return json.load(file)
        return yaml.safe_load(file)
