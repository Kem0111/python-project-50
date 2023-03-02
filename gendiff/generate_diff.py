import json
import itertools


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)
        dict_with_diff = {}
        for key in sorted(set(data1.keys()) | set(data2.keys())):
            if key in data1 and key in data2:
                if data1[key] == data2[key]:
                    dict_with_diff[key] = data1[key]
                else:
                    dict_with_diff[f'- {key}'] = data1[key]
                    dict_with_diff[f'+ {key}'] = data2[key]
            elif key in data1 and key not in data2:
                dict_with_diff[f'- {key}'] = data1[key]
            else:
                dict_with_diff[f'+ {key}'] = data2[key]
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

print(generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file3.json'))