import argparse
import json
import yaml
from gendiff.generate_diff import generate_diff


def run_compare_files():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        "-f",
        "--format",
        default='json',
        help="Set format of output"
    )
    args = parser.parse_args()
    print(output_file(args.first_file, args.second_file))


def output_file(first_file, second_file):
    with open(first_file, 'r') as file1, open(second_file, 'r') as file2:
        if first_file.endswith('json'):
            first_file_data = json.load(file1)
            second_file_data = json.load(file2)
            return generate_diff(first_file_data, second_file_data)
        first_file_data = yaml.safe_load(file1)
        second_file_data = yaml.safe_load(file2)
        return generate_diff(first_file_data, second_file_data)
