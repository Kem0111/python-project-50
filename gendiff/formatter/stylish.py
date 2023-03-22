import itertools


STATUS = {
    'removed': '- ',
    'added': '+ ',
    'unchanged': '  ',
    'nested': '  ',
    'changed': '',
}
NOT_STATUS = '  '
INDENT_COUNT = 4
SPECIAL_SYMB = ' '
LEFT_SHIFT = 2


def stylish(data: dict, depth=1) -> str:
    '''Convert type(dict) to str respecting line breaks, indents
    and given symbols to merg with keys'''

    end_bracket_space = SPECIAL_SYMB * (INDENT_COUNT * depth - INDENT_COUNT)
    key_space = SPECIAL_SYMB * (INDENT_COUNT * depth - LEFT_SHIFT)

    def get_string(key, value, type_):
        return f'{key_space}{type_}{key}: {stringify_value(value, depth)}'

    def stringify_node(key, node):
        value, type_ = node
        if not type_:
            return get_string(key, value, NOT_STATUS)
        elif type_ == 'changed':
            old = stringify_value(value['old_value'], depth)
            new = stringify_value(value['new_value'], depth)
            return (
                f"{get_string(key, old, STATUS['removed'])}\n"
                f"{get_string(key, new, STATUS['added'])}"
            )
        return get_string(key, value, STATUS[type_])

    diff_data = (
        stringify_node(key, get_type(val, 'value', 'type'))
        for key, val in data.items()
    )
    result = itertools.chain('{', diff_data, [end_bracket_space + '}'])
    return '\n'.join(result)


def stringify_value(val, depth):
    json_format = {
        'None': 'null',
        'True': 'true',
        'False': 'false'
    }
    if isinstance(val, dict):
        return stylish(val, depth=depth + 1)
    return json_format.get(str(val), val)


def get_type(content, value, type_):
    if not isinstance(content, dict) or value not in content:
        return content, ''
    return content[value], content[type_]
