def get_mid_point(point1, point2):
    return {
        'x': (point1["x"] + point2["x"]) / 2, 'y': (point1["y"] + point2["y"]) / 2
    }


print(get_mid_point({'x': 2, 'y': 2}, {'x': 8, 'y': 12}))
