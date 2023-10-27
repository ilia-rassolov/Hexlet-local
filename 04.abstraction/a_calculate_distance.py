def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return d

print(calculate_distance((1, 1), (4, 5)))