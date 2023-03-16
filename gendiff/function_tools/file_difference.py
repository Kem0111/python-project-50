def get_diff(old_dict, new_dict):
    '''
    Make new updated dictionary with difference block
    based on given dicts
    '''

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
    removed_keys = old_dict.keys() - new_dict.keys()
    added_keys = new_dict.keys() - old_dict.keys()

    def update_data_diff(keys, status, given_dict):
        for key in keys:
            data_diff[key] = {'type': status, 'value': given_dict[key]}

    update_data_diff(removed_keys, 'removed', old_dict)
    update_data_diff(added_keys, 'added', new_dict)
    return {key: data_diff[key] for key in sorted(data_diff.keys())}
