import math

EPS = 1e-9
PI = math.acos(-1.0)

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

class Vec:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

def to_vec(a, b):
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
    oa = to_vec(o, a)
    ob = to_vec(o, b)
    return math.acos(dot(oa, ob) / math.sqrt(norm_sq(oa) * norm_sq(ob)))

# Ejemplo de uso
if __name__ == "__main__":
    # Crea los puntos del polígono
    P = [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]
    
    # Calcula el perímetro y el área
    print(f"Perímetro: {perimeter(P)}")
    print(f"Área: {area(P)}")
