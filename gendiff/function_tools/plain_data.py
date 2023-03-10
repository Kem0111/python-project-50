from gendiff.function_tools.js_format import make_js_format


def get_plain_diff(first_file, second_file, path=''):

    def walk(key, file1, file2):
        if key in file1 and key in file2:
            diff = get_compair(key, file1, file2, path)
            return diff
        elif key in file1 and key not in file2:
            return f"Property '{path+key}' was removed"
        diff = make_string_format(file2[key])
        return f"Property '{path+key}' was added with value: {diff}"

    all_keys = set(first_file.keys()) | set(second_file.keys())
    plain_data = (
        walk(key, first_file, second_file) for key in sorted(all_keys)
    )
    return '\n'.join(filter(lambda some_data: len(some_data) > 0, plain_data))


def get_compair(key, file1, file2, path):
    if all(
        isinstance(val.get(key), dict) for val in (file1, file2)
    ):
        return get_plain_diff(file1[key], file2[key], path=path + key + '.')
    elif file1[key] != file2[key]:
        return f"Property '{path+key}' was updated. \
From {make_string_format(file1[key])} to {make_string_format(file2[key])}"
    return ''


def make_string_format(value):
    if isinstance(value, (dict, list, set, tuple)):
        return '[complex value]'
    elif not isinstance(value, (type(None), bool, int)):
        return f"'{value}'"
    return make_js_format(value)
