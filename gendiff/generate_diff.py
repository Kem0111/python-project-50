import json
import itertools


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        first_file_data = json.load(file1)
        second_file_data = json.load(file2)
        return make_diff_dict(first_file_data, second_file_data)


def make_diff_dict(first_file, second_file):
    dict_with_diff = {}
    for key in sorted(set(first_file.keys()) | set(second_file.keys())):
        if key in first_file and key in second_file:
            if first_file[key] == second_file[key]:
                dict_with_diff[key] = first_file[key]
            else:
                dict_with_diff[f'- {key}'] = first_file[key]
                dict_with_diff[f'+ {key}'] = second_file[key]
        elif key in first_file and key not in second_file:
            dict_with_diff[f'- {key}'] = first_file[key]
        else:
            dict_with_diff[f'+ {key}'] = second_file[key]
    return stringify(dict_with_diff)


def stringify(value, replacer=' ', spases_count=2, depth=0):
    current_indent = replacer * (spases_count + depth)
    indent = replacer * depth
    if isinstance(value, (int, str, bool)):
        return str(value)

    def walk(key, val):
        return f'''{
            current_indent}{key}: {stringify(
            val, replacer, spases_count, depth=depth + spases_count
            ) if isinstance(val, dict) else make_lower_bool(val)
            }'''

    res = map(lambda x, y: walk(x, y), value.keys(), value.values())
    result = itertools.chain('{', res, [indent + '}'])
    return '\n'.join(result)


def make_lower_bool(val):
    if isinstance(val, bool):
        return str(val).lower()
    return val
