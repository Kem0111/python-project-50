import argparse
from gendiff.generate_diff import generate_diff


def compare_files():
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
    output = generate_diff(args.first_file, args.second_file)
    print(output)
