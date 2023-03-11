#!/usr/bin/env python3
from gendiff.cli import get_cli_args
from gendiff.engine import generate_diff


def main():
    path1, path2, format_ = get_cli_args()
    print(generate_diff(path1, path2, formatter=format_))


if __name__ == '__main__':
    main()
