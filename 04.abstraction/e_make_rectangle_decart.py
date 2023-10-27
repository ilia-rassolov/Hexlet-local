from c_make_abstraction import get_x, get_y, make_decart_point


def get_quadrant(point):
    x = get_x(point)
    y = get_y(point)

    if x > 0 and y > 0:
        return 1
    if x < 0 < y:
        return 2
    if x < 0 and y < 0:
        return 3
    if y < 0 < x:
        return 4

    return None

def change_point(point, axis, change):
    p = point.copy()
    p[axis] += change
    return p

print(change_point({"x": -2, "y": -4}, "x", 6))

def make_rectangle(p, l, h):
    p1 = change_point(p, "x", l)
    p2 = change_point(p1, "y", -h)
    p3 = change_point(p2, "x", -l)
    return {"p": p, "p1": p1, "p2": p2, "p3": p3}

print(make_rectangle({"x": -2, "y": 4}, 6, 6))


def get_start_point(rectangle):
    return rectangle["p"]

print(get_start_point({"p": {'x': -2, 'y': 4}, "p1": {'x': 4, 'y': 4}, "p2": {'x': 4, 'y': -2}, "p3": {'x': -2, 'y': -2}}))

def get_width(rectangle):
    return rectangle["p"]["y"] - rectangle["p3"]["y"]

print(get_width({"p": {'x': -2, 'y': 4}, "p1": {'x': 4, 'y': 4}, "p2": {'x': 4, 'y': -2}, "p3": {'x': -2, 'y': -2}}))

def get_height(rectangle):
    return rectangle["p1"]["x"] - rectangle["p"]["x"]

print(get_height({"p": {'x': -2, 'y': 4}, "p1": {'x': 4, 'y': 4}, "p2": {'x': 4, 'y': -2}, "p3": {'x': -2, 'y': -2}}))

def contains_origin(rectangle):
    quadrant_point = (get_quadrant(rectangle["p"]), get_quadrant(rectangle["p1"]),
    get_quadrant(rectangle["p2"]), get_quadrant(rectangle["p3"]))
    print(len(quadrant_point), len(set(quadrant_point)))
    return len(quadrant_point) == len(set(quadrant_point))

print(contains_origin({"p": {'x': 0, 'y': 0}, "p1": {'x': 0, 'y': 0}, "p2": {'x': 4, 'y': -2}, "p3": {'x': -2, 'y': -2}}))