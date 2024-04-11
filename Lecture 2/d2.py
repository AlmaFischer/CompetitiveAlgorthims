
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

def cross(p1, p2, circle):
    t = Point(p2.x - p1.x, p2.y - p1.y)
    a = t.x ** 2 + t.y ** 2
    b = 2.0 * (t.x * (p1.x - circle.center.x) + t.y * (p1.y - circle.center.y))
    c = circle.center.x ** 2 + circle.center.y ** 2 + p1.x ** 2 + p1.y ** 2 - 2.0 * (circle.center.x * p1.x + circle.center.y * p1.y) - circle.radius ** 2
    d = b ** 2 - 4 * a * c

    if abs(a) < 0 or d < 0:
        return False
    return True


barUP = Point(52.0, 3.66)
barDOWN = Point(52.0, -3.66)
t = int(input())
for _ in range(t):
    input()
    raul_x, raul_y  = map(float, input().split())
    golee_x, golee_y, golee_r = map(float, input().split())
    raul = Point(raul_x, raul_y)
    golee = Circle(Point(golee_x, golee_y), golee_r)
    if cross(raul, barUP, golee) and cross(raul, barDOWN, golee):
        print("No goal...")
    else:
        print("Goal!")
