import argparse
from gendiff.stylish import stylish


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
        default='stylish',
        help="Set format of output"
    )
    args = parser.parse_args()
    print(stylish(args.first_file, args.second_file))
