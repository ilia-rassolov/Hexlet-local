def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]

def make_segment(point1, point2):
    print(point1)
    return {"begin_point": point1, "end_point": point2}

print(make_segment({'x': 1, 'y': 2}, {'x': 3, 'y': 6}))


def get_mid_point_of_segment(segment):
    return make_decart_point((get_x(segment["begin_point"]) + get_x(segment["end_point"])) / 2,
                             (get_y(segment["begin_point"]) + get_y(segment["end_point"])) / 2)


print(get_mid_point_of_segment({'begin_point': {'x': 1, 'y': 2}, 'end_point': {'x': 3, 'y': 6}}))


def get_begin_point(segment):
    return segment["begin_point"]


print(get_begin_point({'begin_point': {'x': 1, 'y': 2}, 'end_point': {'x': 3, 'y': 6}}))


def get_end_point(segment):
    return segment["end_point"]


print(get_end_point({'begin_point': {'x': 1, 'y': 2}, 'end_point': {'x': 3, 'y': 6}}))
