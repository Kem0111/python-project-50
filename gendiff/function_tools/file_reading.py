import json
import yaml


def extract_file_data(first_file_path, second_file_path):
    with open(first_file_path, 'r') as file1, open(second_file_path, 'r') as file2:
        if first_file_path.endswith('json'):
            first_file_data = json.load(file1)
            second_file_data = json.load(file2)
            return first_file_data, second_file_data
        first_file_data = yaml.safe_load(file1)
        second_file_data = yaml.safe_load(file2)
        return first_file_data, second_file_data
