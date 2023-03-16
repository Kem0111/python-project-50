import itertools
from gendiff.function_tools.js_format import make_js_format

INDENT_COUNT = 4
SPECIAL_SYMB = ' '
LEFT_SHIFT = 2


def stringify(data: dict, symbols: dict, depth=1, spaces_count=0) -> str:
    '''
    Convert type(dict) to str respecting line breaks, indents
    and given symbols to merg with keys
    '''

    def stringify_value(val):
        if isinstance(val, dict):
            return stringify(
                val, symbols, depth=depth+1,
                spaces_count=spaces_count+INDENT_COUNT
            )
        return make_js_format(val)

    closing_bracket_spacing = SPECIAL_SYMB * spaces_count
    key_space = SPECIAL_SYMB * (INDENT_COUNT * depth - LEFT_SHIFT)

    def walk(key, func):
        value, status = func
        if status == 'changed':
            old = stringify_value(value['old_value'])
            new = stringify_value(value['new_value'])
            return (
                f"{key_space}{symbols['removed']}{key}: {old}\n"
                f"{key_space}{symbols['added']}{key}: {new}"
            )
        return f'''{
            key_space}{symbols.get(status, '  ')}{key}: {stringify_value(value)
            }'''

    diff_data = (
        walk(key, get_status(val, 'value', 'type'))
        for key, val in data.items()
    )
    result = itertools.chain('{', diff_data, [closing_bracket_spacing + '}'])
    return '\n'.join(result)


def get_status(content, value, type_):
    if not isinstance(content, dict) or value not in content:
        return content, None
    return content[value], content[type_]
