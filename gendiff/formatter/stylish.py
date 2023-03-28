import itertools
import json
from typing import Any, Callable, Dict, Iterable

TYPE = {
    'removed': '- ',
    'added': '+ ',
    'unchanged': '  ',
    'nested': '  ',
    'changed': '',
}
NOT_TYPE = '  '
INDENT_COUNT = 4
SPECIAL_SYMB = ' '
LEFT_SHIFT = 2


def stylish(tree: Dict[str, Any], depth: int = 1) -> str:
    """
    Convert the given tree (dictionary) to a formatted string representation.

    Args:
        tree (dict): The dictionary to be formatted.
        depth (int, optional): The current depth level for indentation.

    Returns:
        str: A formatted string representation of the tree.
    """

    str_tree = iteration_data(stringify_node, tree, depth)
    return get_result(str_tree, depth)


def stringify_node(key: str, node: Dict[str, Any], depth: int) -> str:
    """
    Format a single node of the tree.

    Args:
        key: The key of the node.
        node: The node to be formatted.
        depth (int): The current depth level for indentation.

    Returns:
        str: A formatted string representation of the node.
    """

    value, type_ = node['value'], node['type']
    if type_ == 'changed':
        return (
            f"{strigify(key, value['old_value'], depth, 'removed')}\n"
            f"{strigify(key, value['new_value'], depth, 'added')}"
        )
    return strigify(key, value, depth, type_)


def stringify_value(val: Any, depth: int) -> str:
    """
    Format the value of a node.

    Args:
        val: The value to be formatted.
        depth (int): The current depth level for indentation.

    Returns:
        str: A formatted string representation of the value.
    """

    if isinstance(val, (type(None), bool, int)):
        return json.dumps(val)
    elif not isinstance(val, dict):
        return val
    data = iteration_data(strigify, val, depth)
    return get_result(data, depth)


def strigify(key: str, value: Any, depth: int, type_: str = None) -> str:
    """
    Format a key-value pair with the specified type.

    Args:
        key: The key of the pair.
        value: The value of the pair.
        depth (int): The current depth level for indentation.
        type_ (str, optional): The type of the pair. Defaults to None.

    Returns:
        str: A formatted string representation of the key-value pair.
    """

    key_space = SPECIAL_SYMB * (INDENT_COUNT * depth - LEFT_SHIFT)
    return f'''{key_space}{TYPE.get(type_, NOT_TYPE)}{key}: {
                    stringify_value(value, depth=depth+1)
                    if type_ != "nested" else stylish(value, depth=depth+1)
    }'''


def get_result(data: Iterable[str], depth: int) -> str:
    """
    Generate the final formatted string with appropriate brackets.

    Args:
        data: The formatted data.
        depth (int): The current depth level for indentation.

    Returns:
        str: The final formatted string.
    """

    end_space = SPECIAL_SYMB * (INDENT_COUNT * depth - INDENT_COUNT)
    result = itertools.chain('{', data, [end_space + '}'])
    return '\n'.join(result)


def iteration_data(stringify_func: Callable[..., str],
                   data: Dict[str, Any], depth: int) -> Iterable[str]:
    return (
        stringify_func(key, value, depth)
        for key, value in data.items()
    )
