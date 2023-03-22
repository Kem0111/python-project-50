import json


PLAIN_OUTPUT = {
    'removed': "Property '{}' was removed",
    'added': "Property '{}' was added with value: {}",
    'changed': "Property '{}' was updated. From {} to {}",
    'unchanged': ''
}


def plain(data: dict, path='') -> str:
    '''
    Convert type(dict) to str as a line-by-line output of changes
    '''

    def stringify(key, node):
        type_ = node['type']
        if type_ not in PLAIN_OUTPUT:
            return plain(node['value'], path=path + f"{key}.")
        return PLAIN_OUTPUT[type_].format(
            path + key, *get_value(node, 'value', "old_value", "new_value")
        )

    res = (
        stringify(key, val) for key, val in data.items()
        if stringify(key, val)
    )
    return '\n'.join(res)


def get_value(data, key, old, new):
    if isinstance(data[key], dict) and old in data[key]:
        return stringify_value(data[key][old]), stringify_value(data[key][new])
    return (stringify_value(data[key]),)


def stringify_value(value):
    if isinstance(value, (dict, list, set, tuple)):
        return '[complex value]'
    elif not isinstance(value, (type(None), bool, int)):
        return f"'{value}'"
    return json.dumps(value)
