import math

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)

def is_inside(x1, y1, x2, y2, x3, y3, x, y):
    # Calculate area of triangle ABC
    A = area(x1, y1, x2, y2, x3, y3)
    # Calculate area of triangle PBC
    A1 = area(x, y, x2, y2, x3, y3)
    # Calculate area of triangle PAC
    A2 = area(x1, y1, x, y, x3, y3)
    # Calculate area of triangle PAB
    A3 = area(x1, y1, x2, y2, x, y)
    # Check if sum of A1, A2 and A3 is same as A
    return A == A1 + A2 + A3

def visible_area(vertices):
    # Triangulate the polygon
    total_area = 0
    n = len(vertices)
    for i in range(1, n - 1):
        total_area += area(vertices[0][0], vertices[0][1], vertices[i][0], vertices[i][1], vertices[i + 1][0], vertices[i + 1][1])
    # Check visibility of each interior point
    for x in range(min(x for x, y in vertices), max(x for x, y in vertices) + 1):
        for y in range(min(y for x, y in vertices), max(y for x, y in vertices) + 1):
            if all(is_inside(vertices[i][0], vertices[i][1], vertices[(i + 1) % n][0], vertices[(i + 1) % n][1], vertices[(i + 2) % n][0], vertices[(i + 2) % n][1], x, y) for i in range(n)):
                total_area += 1
    return total_area

# Reading input
T = int(input())
for _ in range(T):
    N = int(input())
    vertices = []
    for _ in range(N):
        x, y = map(int, input().split())
        vertices.append((x, y))
    # Calculate and print the visible area
    print("{:.2f}".format(visible_area(vertices)))
