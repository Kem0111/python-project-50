import itertools


def stringify(data, indent, replacer, left_shift):
    depth=1
    spases_count=0
    final_braket_indent = replacer * spases_count
    current_indent_befor_key = calculate_indent_count(
        data, replacer, indent, depth)(left_shift)

    def walk(key, value):
        spases_count = spases_count + indent
        depth = depth + 1 
        return f'''{
            current_indent_befor_key}{key}: {stringify(
            value, indent, replacer, left_shift
            ) if isinstance(value, dict) else make_js_format(value)
            }'''

    res = map(lambda x, y: walk(x, y), data.keys(), data.values())
    result = itertools.chain('{', res, [final_braket_indent + '}'])
    return '\n'.join(result)


def calculate_indent_count(data, replacer, indent, depth):
    key = ''.join(filter(lambda key: key, data.keys()))
    if key[0].isalnum():
        return replacer*(indent*depth)
    
    def shift_key(left_shift):
        return replacer*(indent*depth-left_shift)
    
    return shift_key()


def make_js_format(val):

    def make_null_string(val):
        if str(val) == 'None':
            return 'null'
        return val

    if isinstance(val, bool):
        return str(val).lower()
    return make_null_string(val)
