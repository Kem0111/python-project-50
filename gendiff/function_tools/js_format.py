def make_js_format(val):
    format_ = {
        'None': 'null',
        'True': 'true',
        'False': 'false'
    }
    if str(val) in format_:
        return format_[str(val)]
    return val
