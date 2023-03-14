import json
import yaml


def parse_data(data, format_):
    if format_.lower() == '.json':
        return json.loads(data)
    return yaml.safe_load(data)
