def make_diff_data(first_file_data, second_file_data):
    data_diff = {}
    for key in sorted(set(first_file_data.keys()) | set(second_file_data.keys())):
        if key in first_file_data and key in second_file_data:
            if first_file_data[key] == second_file_data[key]:
                data_diff[f'  {key}'] = first_file_data[key]
            elif isinstance(first_file_data[key], dict) and isinstance(second_file_data[key], dict):
                data_diff[f'  {key}'] = make_diff_data(first_file_data[key], second_file_data[key])
            else:
                data_diff[f'- {key}'] = first_file_data[key]    
                data_diff[f'+ {key}'] = second_file_data[key]
        elif key in first_file_data and key not in second_file_data:
            data_diff[f'- {key}'] = first_file_data[key]
        else:
            data_diff[f'+ {key}'] = second_file_data[key]
    return data_diff
