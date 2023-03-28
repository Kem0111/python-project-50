from typing import Any, Dict, Tuple
import json


PLAIN_OUTPUT = {
    'removed': "Property '{}' was removed",
    'added': "Property '{}' was added with value: {}",
    'changed': "Property '{}' was updated. From {} to {}",
    'unchanged': ''
}


def plain(data: Dict[str, Any], path: str = '') -> str:
    '''
    Convert a dictionary representation of a diff tree to a plain text
    representation as a line-by-line output of changes.

    Args:
        data: A dictionary representation of a diff tree.
        path: The current path in the diff tree, used for recursive calls.

    Returns:
        A plain text representation of the diff tree.
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


def get_value(data: Dict[str, Any], key: str, old: str, new: str) -> Tuple:
    '''
    Get the values from the diff tree.

    Args:
        data: A dictionary representation of a diff tree.
        key: The key in the diff tree to get the value(s) from.
        old: The key for the old value in the diff tree.
        new: The key for the new value in the diff tree.

    Returns:
        A tuple containing the value(s) from the diff tree.
    '''
    if isinstance(data[key], dict) and old in data[key]:
        return stringify_value(data[key][old]), stringify_value(data[key][new])
    return (stringify_value(data[key]),)


def stringify_value(value: Any) -> str:
    '''
    Convert a value from the diff tree into a human-readable string.

    Args:
        value: The value to be converted.

    Returns:
        A human-readable string representation of the value.
    '''
    if isinstance(value, (dict, list, set, tuple)):
        return '[complex value]'
    elif not isinstance(value, (type(None), bool, int)):
        return f"'{value}'"
    return json.dumps(value)
