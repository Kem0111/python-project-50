from typing import Any, Dict


def get_diff(old_dict: dict, new_dict: dict) -> Dict[str, Dict[str, Any]]:
    '''
    Compare two dictionaries and generate a new dictionary representing the
    differences between the input dictionaries.

    Args:
        old_dict: The first given dictionary to compare.
        new_dict: The second given dictionary to compare.

    Returns:
        A new dictionary representing the differences between the given
        dictionaries, including added, removed, and changed keys and values.
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

    def update_data_diff(keys, type_, node):
        for key in keys:
            data_diff[key] = {'type': type_, 'value': node[key]}

    update_data_diff(removed_keys, 'removed', old_dict)
    update_data_diff(added_keys, 'added', new_dict)
    return {key: data_diff[key] for key in sorted(data_diff.keys())}
