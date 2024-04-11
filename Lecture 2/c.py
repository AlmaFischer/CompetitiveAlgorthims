import math
PI = math.pi
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return abs(self.x - other.x) < 0 and abs(self.y - other.y) < 0

class Vec:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

def toVec(a, b):
    return Vec(b.x - a.x, b.y - a.y)

def dist(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)

def perimeter(P):
    result = 0.0
    for i in range(len(P) - 1):
        result += dist(P[i], P[i + 1])
    return result

def area(P):
    result = 0.0
    for i in range(len(P) - 1):
        x1, y1 = P[i].x, P[i].y
        x2, y2 = P[i + 1].x, P[i + 1].y
        result += (x1 * y2 - x2 * y1)
    return abs(result) / 2.0

def dot(a, b):
    return a.x * b.x + a.y * b.y

def norm_sq(v):
    return v.x * v.x + v.y * v.y

def angle(a, o, b):
    oa = toVec(o, a)
    ob = toVec(o, b)
    return math.acos(dot(oa, ob) / math.sqrt(norm_sq(oa) * norm_sq(ob)))

def cross(a, b):
    return a.x * b.y - a.y * b.x

def ccw(p, q, r):
    return cross(toVec(p, q), toVec(p, r)) > 0

def collinear(p, q, r):
    return abs(cross(toVec(p, q), toVec(p, r))) < 0

def isConvex(P):
    sz = len(P)
    if sz <= 3:
        return False
    isLeft = ccw(P[0], P[1], P[2])
    for i in range(1, sz - 1):
        if ccw(P[i], P[i + 1], P[(i + 2) if (i + 2) < sz else 1]) != isLeft:
            return False
    return True

def inPolygon(pt, P):
    if len(P) == 0:
        return False
    sum = 0
    for i in range(len(P) - 1):
        if ccw(pt, P[i], P[i + 1]):
            sum += angle(P[i], pt, P[i + 1])
        else:
            sum -= angle(P[i], pt, P[i + 1])
    return abs(abs(sum) - 2 * PI) < 0

def lineIntersectSeg(p, q, A, B):
    a = B.y - A.y
    b = A.x - B.x
    c = B.x * A.y - A.x * B.y
    u = abs(a * p.x + b * p.y + c)
    v = abs(a * q.x + b * q.y + c)
    return Point((p.x * v + q.x * u) / (u + v), (p.y * v + q.y * u) / (u + v))

def cutPolygon(a, b, Q):
    P = []
    for i in range(len(Q)):
        left1 = cross(toVec(a, b), toVec(a, Q[i]))
        left2 = 0
        if i != len(Q) - 1:
            left2 = cross(toVec(a, b), toVec(a, Q[i + 1]))
        if left1 > -0:
            P.append(Q[i])
        if left1 * left2 < -0:
            P.append(lineIntersectSeg(Q[i], Q[i + 1], a, b))
    if P and not (P[-1] == P[0]):
        P.append(P[0])
    return P

def angleCmp(a, b):
    if collinear(pivot, a, b):
        return dist(pivot, a) < dist(pivot, b)
    d1x = a.x - pivot.x
    d1y = a.y - pivot.y
    d2x = b.x - pivot.x
    d2y = b.y - pivot.y
    return math.atan2(d1y, d1x) - math.atan2(d2y, d2x)

def CH(P):
    n = len(P)
    if n <= 3:
        if not (P[0] == P[n - 1]):
            P.append(P[0])
        return P
    P0 = 0
    for i in range(1, n):
        if P[i].y < P[P0].y or (P[i].y == P[P0].y and P[i].x > P[P0].x):
            P0 = i
    P[0], P[P0] = P[P0], P[0]
    global pivot
    pivot = P[0]
    P[1:] = sorted(P[1:], key=lambda x: angleCmp(x))
    S = [P[n - 1], P[0], P[1]]
    i = 2
    while i < n:
        j = len(S) - 1
        if ccw(S[j - 1], S[j], P[i]):
            S.append(P[i])
            i += 1
        else:
            S.pop()
    return S

def main():
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        p = []
        for _ in range(n):
            x, y = map(int, input().split())
            p.append(Point(x, y))
        p.append(p[0])
        sz = len(p)
        pcopy = p[:]
        for i in range(sz - 1, 0, -1):
            pcopy = cutPolygon(p[i], p[i - 1], pcopy)
        print("{:.2f}".format(area(pcopy)))

if __name__ == "__main__":
    main()
