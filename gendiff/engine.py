import argparse
from gendiff.stylish import stylish
from gendiff.plain import plain
from gendiff.json import json


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
    if args.format == 'plain':
        print(plain(args.first_file, args.second_file))
    elif args.format == 'json':
        print(json(args.first_file, args.second_file))
    else:
        print(stylish(args.first_file, args.second_file))
