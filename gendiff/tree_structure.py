def get_diff(old_dict, new_dict):
    '''
    Make new updated dictionary with difference block
    based on given dicts
    '''
    data_diff = {}
    for key in (old_dict.keys() & new_dict.keys()):
        if old_dict[key] == new_dict[key]:
            data_diff[key] = {
                'type': 'unchanged',
                'value': old_dict[key]
            }
        elif isinstance(old_dict[key], dict) and isinstance(new_dict[key],
                                                            dict):
            data_diff[key] = {
                'type': 'nested',
                'value': get_diff(old_dict[key], new_dict[key])
            }
        else:
            data_diff[key] = {
                'type': 'changed',
                'value': {
                    'old_value': old_dict[key],
                    'new_value': new_dict[key]
                }
            }
    removed_keys = old_dict.keys() - new_dict.keys()
    added_keys = new_dict.keys() - old_dict.keys()

    def update_data_diff(keys, status, given_dict):
        for key in keys:
            data_diff[key] = {'type': status, 'value': given_dict[key]}

    update_data_diff(removed_keys, 'removed', old_dict)
    update_data_diff(added_keys, 'added', new_dict)
    return {key: data_diff[key] for key in sorted(data_diff.keys())}
