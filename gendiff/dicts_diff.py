def build_diff(data1: dict, data2: dict):
    diff = list()
    sorted_keys = sorted(
        list(set(data1.keys()) | set(data2.keys()))
    )
    for key in sorted_keys:
        if key not in data1:
            diff.append({
                'key': key,
                'operation': 'add',
                'new': data2[key]
            })
        elif key not in data2:
            diff.append({
                'key': key,
                'operation': 'removed',
                'old': data1[key]
            })
        elif isinstance(data1[key], dict) and isinstance(
                data2[key], dict):
            child = build_diff(data1[key], data2[key])
            diff.append({
                'key': key,
                'operation': 'nested',
                'value': child
            })
        elif data1[key] == data2[key]:
            diff.append({
                'key': key,
                'operation': 'same',
                'value': data1[key]
            })
        elif data1[key] != data2[key]:
            diff.append({
                'key': key,
                'operation': 'changed',
                'old': data1[key],
                'new': data2[key]
            })
    return diff
