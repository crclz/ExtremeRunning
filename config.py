import re


def load_route_file(filename):
    with open(filename, 'r', encoding='utf8') as f:
        lines = f.read().splitlines(keepends=False)
        lines = list([p.strip() for p in lines])

        # ignore white lines
        lines = list([p for p in lines if p != ''])

    route = []

    for line in lines:
        ss = re.split(' |\t|,', line)
        ss = [p for p in ss if p != '']
        if len(ss) != 2:
            raise RuntimeError(f"格式错误: {line}. 请检查路径文件")

        try:
            lng = float(ss[0])
            lat = float(ss[1])
            route.append([lng, lat])
        except ValueError:
            raise RuntimeError(f"数字格式错误: {line}. 请检查路径文件")

    # check for duplicated points
    hits = set()
    for point in route:
        p_tuple = (*point,)
        if p_tuple in hits:
            raise RuntimeError(f"重复的坐标点: {point}. 请检查路径文件")
        hits.add(p_tuple)

    return route
