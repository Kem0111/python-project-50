from json import dumps


def json(data):
    stylish_data = dumps(data, indent=2)
    return stylish_data
