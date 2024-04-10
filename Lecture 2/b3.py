from dataclasses import dataclass
import math

EPS = 1E-8

@dataclass
class Point:
    x: float
    y: float

    def __add__(self, t):
        return Point(self.x + t.x, self.y + t.y)

    def __sub__(self, t):
        return Point(self.x - t.x, self.y - t.y)

    def dot(self, a):
        return self.x * a.x + self.y * a.y

    def norm(self):
        return math.sqrt(self.dot(self))

    def rotate(self, theta):
        return Point(self.x * math.cos(theta) + self.y * math.sin(theta),
                     self.x * math.sin(theta) - self.y * math.cos(theta))

    def cross(self, p):
        return self.x * p.y - p.x * self.y

@dataclass
class Line:
    a: float
    b: float
    c: float

    @staticmethod
    def from_points(p1, p2):
        if abs(p1.x - p2.x) < EPS:
            return Line(1.0, 0.0, -p1.x)
        else:
            a = -(p1.y - p2.y) / (p1.x - p2.x)
            b = 1.0
            c = -(a * p1.x) - p1.y
            return Line(a, b, c)

    def slope(self):
        return -self.a / self.b

    def y_cross(self):
        return -self.c / self.b

    def x_cross(self):
        return -self.c / self.a

    def normal(self):
        return Point(self.a / math.sqrt(self.a**2 + self.b**2),
                     self.b / math.sqrt(self.a**2 + self.b**2))

    def d(self):
        return self.c / math.sqrt(self.a**2 + self.b**2)

    def intersect(self, l):
        return Point((-self.b*l.c + l.b*self.c) / (self.a*l.b - l.a*self.b),
                     (-self.a*l.c + l.a*self.c) / (self.a*l.b - l.a*self.b))

    def are_parallel(self, line):
        return abs((self.a * line.a + self.b * line.b)
                   / (math.sqrt(self.a**2 + self.b**2) * math.sqrt(line.a**2 + line.b**2))) < EPS

    def angle(self, line):
        return math.acos((self.a * line.a + self.b * line.b)
                         / (math.sqrt(self.a**2 + self.b**2) * math.sqrt(line.a**2 + line.b**2)))

@dataclass
class Segment:
    p: Point
    q: Point

    def does_intersect(self, seg2, *, include_p=False, include_q=False):
        cross1 = (seg2.q - self.p).cross(self.q - self.p)
        cross2 = (seg2.p - self.p).cross(self.q - self.p)
        cross3 = (self.q - seg2.p).cross(seg2.q - seg2.p)
        cross4 = (self.p - seg2.p).cross(seg2.q - seg2.p)

        return (cross1 * cross2 < 0 or (include_p and math.fabs(cross2) < EPS)) and \
               (cross3 * cross4 < 0 or (include_p and math.fabs(cross4) < EPS))

# Example usage:
# Define points
p1 = Point(0, 0)
p2 = Point(1, 1)
p3 = Point(0, 1)
p4 = Point(1, 0)

# Define segments
seg1 = Segment(p1, p2)
seg2 = Segment(p3, p4)

# Check if segments intersect
print(seg1.does_intersect(seg2))  # Output: True
