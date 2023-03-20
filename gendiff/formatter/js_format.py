def make_js_format(val):
    json_format = {
        'None': 'null',
        'True': 'true',
        'False': 'false'
    }
    return json_format.get(str(val), val)
