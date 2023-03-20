import json
import yaml


available_formats = {
    '.json': json.loads,
    '.yml': yaml.safe_load,
    '.yaml': yaml.safe_load
}


def parse_data(data, format_):
    if format_.lower() not in available_formats:
        raise ValueError(
            'Unsuported format. Excepted {} files'
            .format(available_formats.keys())
        )
    return available_formats[format_](data)
