import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return abs(self.x - other.x) < 1e-9 and abs(self.y - other.y) < 1e-9

def to_vec(a, b):
    return Point(b.x - a.x, b.y - a.y)

def dist(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)

def perimeter(polygon):
    return sum(dist(polygon[i], polygon[i + 1]) for i in range(len(polygon) - 1))

def area(polygon):
    return abs(sum((polygon[i].x * polygon[i + 1].y - polygon[i + 1].x * polygon[i].y) for i in range(len(polygon) - 1)) / 2.0)

def dot(a, b):
    return a.x * b.x + a.y * b.y

def norm_sq(v):
    return v.x * v.x + v.y * v.y

def angle(a, o, b):
    oa = to_vec(o, a)
    ob = to_vec(o, b)
    return math.acos(dot(oa, ob) / math.sqrt(norm_sq(oa) * norm_sq(ob)))

def cross(a, b):
    return a.x * b.y - a.y * b.x

def ccw(p, q, r):
    return cross(to_vec(p, q), to_vec(p, r)) > 0

def collinear(p, q, r):
    return abs(cross(to_vec(p, q), to_vec(p, r))) < 1e-9

def is_convex(polygon):
    sz = len(polygon)
    if sz <= 3:
        return False
    is_left = ccw(polygon[0], polygon[1], polygon[2])
    for i in range(1, sz - 1):
        if ccw(polygon[i], polygon[i + 1], polygon[(i + 2) % sz]) != is_left:
            return False
    return True

def in_polygon(pt, polygon):
    if len(polygon) == 0:
        return False
    angle_sum = 0
    for i in range(len(polygon) - 1):
        if ccw(pt, polygon[i], polygon[i + 1]):
            angle_sum += angle(polygon[i], pt, polygon[i + 1])
        else:
            angle_sum -= angle(polygon[i], pt, polygon[i + 1])
    return abs(abs(angle_sum) - 2 * math.pi) < 1e-9

def line_intersect_seg(p, q, a, b):
    d = (b.y - a.y) * (q.x - p.x) - (b.x - a.x) * (q.y - p.y)
    if d == 0:
        return None  # Parallel or coincident lines
    t1 = ((a.x - p.x) * (q.y - p.y) - (a.y - p.y) * (q.x - p.x)) / d
    t2 = ((a.x - p.x) * (b.y - a.y) - (a.y - p.y) * (b.x - a.x)) / d
    if not (0 <= t1 <= 1 and 0 <= t2 <= 1):
        return None  # Intersection is not within segments
    return Point(p.x + t1 * (q.x - p.x), p.y + t1 * (q.y - p.y))

def cut_polygon(a, b, polygon):
    result = []
    for i in range(len(polygon)):
        left1 = cross(to_vec(a, b), to_vec(a, polygon[i]))
        left2 = cross(to_vec(a, b), to_vec(a, polygon[i - 1]))
        if left1 >= 0:
            result.append(polygon[i])
        if left1 * left2 < 0:
            intersection_point = line_intersect_seg(polygon[i], polygon[i - 1], a, b)
            if intersection_point:
                result.append(intersection_point)
    if result and not result[-1] == result[0]:
        result.append(result[0])
    return result

def convex_hull(points):
    n = len(points)
    if n <= 3:
        if not (points[0] == points[-1]):
            points.append(points[0])
        return points
    pivot = min(points, key=lambda p: (p.y, p.x))
    points = sorted(points, key=lambda p: math.atan2(p.y - pivot.y, p.x - pivot.x))
    stack = [points[0], points[1], points[2]]
    for i in range(3, n):
        while len(stack) > 1 and not ccw(stack[-2], stack[-1], points[i]):
            stack.pop()
        stack.append(points[i])
    return stack

tc = int(input())
for _ in range(tc):
    n = int(input())
    polygon = []
    for _ in range(n):
        x, y = map(int, input().split())
        polygon.append(Point(x, y))
    polygon.append(polygon[0])
    simplified_polygon = polygon[:]
    for i in range(n, 0, -1):
        simplified_polygon = cut_polygon(polygon[i], polygon[i - 1], simplified_polygon)
    print("{:.2f}".format(area(simplified_polygon)))
