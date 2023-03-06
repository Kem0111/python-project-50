import itertools


PERMANENT_INDENT = 4
SPECIAL_SYMB = ' '
LEFT_SHIFT = 2


def stringify(data, depth=1, spases_count=0):

    def colculate_indent(key):
        if key[0].isalnum():
            return SPECIAL_SYMB*(PERMANENT_INDENT*depth)
        return SPECIAL_SYMB*(PERMANENT_INDENT*depth-LEFT_SHIFT)

    final_braket_indent = SPECIAL_SYMB * spases_count
    key = get_key(data)
    current_indent_befor_key = colculate_indent(key)

    def walk(key, value):
        return f'''{
            current_indent_befor_key}{key}: {stringify(
            value, depth=depth + 1,
            spases_count=spases_count + PERMANENT_INDENT
            ) if isinstance(value, dict) else make_js_format(value)
            }'''

    res = map(lambda x, y: walk(x, y), data.keys(), data.values())
    result = itertools.chain('{', res, [final_braket_indent + '}'])
    return '\n'.join(result)


def get_key(data):
    return ''.join(filter(lambda key: key, data.keys()))


def make_js_format(val):

    def make_null_string(val):
        if str(val) == 'None':
            return 'null'
        return val

    if isinstance(val, bool):
        return str(val).lower()
    return make_null_string(val)
