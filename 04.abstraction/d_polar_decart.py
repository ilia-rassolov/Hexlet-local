import math


def make_point(x, y):
    return {
        "angle": math.atan2(y, x),
        "radius": math.sqrt((x ** 2) + (y ** 2)),
    }

def get_x(point):
    return point["radius"] * math.cos(point["angle"])


def get_y(point):
    return point["radius"] * math.sin(point["angle"])



print(make_point(3, 4))
print(get_x({"angle": 1, "radius": 6}) ** 2)
print(get_y({"angle": 1, "radius": 6}) ** 2)