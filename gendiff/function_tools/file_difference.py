def get_diff(first_file_data, second_file_data, indent):
    data_diff = {}
    all_keys = set(first_file_data.keys()) | set(second_file_data.keys())
    for key in sorted(all_keys):
        if key in first_file_data and key in second_file_data:
            diff = get_compare_dict(key, first_file_data,
                                    second_file_data, indent)
            data_diff.update(diff)
        elif key in first_file_data and key not in second_file_data:
            data_diff[f'{indent["removed"]}{key}'] = first_file_data[key]
        else:
            data_diff[f'{indent["added"]}{key}'] = second_file_data[key]
    return data_diff


def get_compare_dict(key, first_dict, second_dict, indent):
    if first_dict[key] == second_dict[key]:
        return {f'{indent["unchanged"]}{key}': first_dict[key]}
    elif all(
        isinstance(val.get(key), dict) for val in (first_dict, second_dict)
    ):
        return {
            f'{indent["unchanged"]}{key}': get_diff(first_dict[key],
                                                    second_dict[key],
                                                    indent)
        }
    return {
        f'{indent["removed"]}{key}': first_dict[key],
        f'{indent["added"]}{key}': second_dict[key]
    }
