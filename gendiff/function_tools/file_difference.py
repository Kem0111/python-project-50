def get_diff(old_dict, new_dict):

    def get_type(old_value, new_value):
        if old_value == new_value:
            return {
                'type': 'unchanged',
                'value': old_value
            }
        elif isinstance(old_value, dict) and isinstance(new_value, dict):
            return {
                'type': 'nested',
                'value': get_diff(old_value, new_value)
            }
        return {
            'type': 'changed',
            'value': {
                'old_value': old_value,
                'new_value': new_value
            }
        }

    data_diff = ({
        key: get_type(old_dict[key], new_dict[key])
        for key in old_dict.keys() & new_dict.keys()
    })
    removed_val = {
        key: {'type': 'removed', 'value': old_dict[key]}
        for key in old_dict.keys() - new_dict.keys()
    }
    added_val = {
        key: {'type': 'added', 'value': new_dict[key]}
        for key in new_dict.keys() - old_dict.keys()
    }
    data_diff.update(removed_val)
    data_diff.update(added_val)
    return {key: data_diff[key] for key in sorted(data_diff.keys())}
