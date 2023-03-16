from gendiff.function_tools.js_format import make_js_format


def stringify(data, output, path=''):

    def walk(key, val):
        status = val['type']
        if status not in output:
            return stringify(val['value'], output, path=path+f"{key}.")
        return output[status].format(
            path+key, *get_value(val, 'value', "old_value", "new_value")
        )

    res = (walk(key, val) for key, val in data.items() if walk(key, val))
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
    return make_js_format(value)
