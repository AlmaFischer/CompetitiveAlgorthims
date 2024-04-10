class Vec:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
def dot_product(v1, v2):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z
points = []
for _ in range(4):
    x, y, z = map(int, input().split())
    if not (-10**6 <= x <= 10**6 and -10**6 <= y <= 10**6 and -10**6 <= z <= 10**6):
        print("Invalid")
        exit()
    points.append([x, y, z])
AB = Vec(points[1][0] - points[0][0], points[1][1] - points[0][1], points[1][2] - points[0][2])
CD = Vec(points[3][0] - points[2][0], points[3][1] - points[2][1], points[3][2] - points[2][2])
if dot_product(AB, CD) == 0:
    print("Valid")
else:
    print("Invalid")

