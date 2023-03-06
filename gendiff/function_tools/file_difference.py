def make_diff_data(first_file_data, second_file_data):
    data_diff = {}
    all_keys = set(first_file_data.keys()) | set(second_file_data.keys())
    for key in sorted(all_keys):
        if key in first_file_data and key in second_file_data:
            diff = get_compare_dict(key, first_file_data, second_file_data)
            data_diff.update(diff)
        elif key in first_file_data and key not in second_file_data:
            data_diff[f'- {key}'] = first_file_data[key]
        else:
            data_diff[f'+ {key}'] = second_file_data[key]
    return data_diff


def get_compare_dict(key, first_dict, second_dict):
    if first_dict[key] == second_dict[key]:
        return {f'  {key}': first_dict[key]}
    elif all(
        isinstance(val.get(key), dict) for val in (first_dict, second_dict)
    ):
        return {f'  {key}': make_diff_data(first_dict[key], second_dict[key])}
    return {f'- {key}': first_dict[key], f'+ {key}': second_dict[key]}
