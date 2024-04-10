import math

# Function to calculate distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Function to determine orientation of triplet (p, q, r)
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0 # colinear
    elif val > 0:
        return 1 # clockwise
    else:
        return 2 # counterclockwise

# Function to find the convex hull of a set of points using Graham Scan
def convex_hull(points):
    n = len(points)
    if n < 3:
        return []

    # Find the leftmost point
    l = min(points, key=lambda x: x[0])

    # Sort the points based on polar angle
    points.sort(key=lambda x: (math.atan2(x[1] - l[1], x[0] - l[0]), x))

    hull = [points[0], points[1]]
    for i in range(2, n):
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[i]) != 2:
            hull.pop()
        hull.append(points[i])
    
    return hull

# Function to calculate the perimeter of a polygon
def polygon_perimeter(vertices):
    perimeter = 0
    n = len(vertices)
    for i in range(n):
        perimeter += distance(vertices[i], vertices[(i + 1) % n])
    return perimeter

# Function to round the result to the nearest 8 inches
def round_to_8_inches(length):
    return int(length / 12 * 12 + 0.5)

# Main function to read input and calculate the minimal possible length of the wall
def calculate_minimal_wall_length():
    num_cases = int(input().strip())
    input()  # Consume the blank line
    
    for _ in range(num_cases):
        # Read input for each case
        n, L = map(int, input().split())
        vertices = [tuple(map(int, input().split())) for _ in range(n)]

        # Find convex hull of the castle's vertices
        convex_hull_vertices = convex_hull(vertices)

        # Calculate perimeter of convex hull and add the minimal distance allowed
        perimeter = polygon_perimeter(convex_hull_vertices) + 2 * math.pi * L

        # Round the result to the nearest 8 inches
        rounded_length = round_to_8_inches(perimeter)

        # Output the result for this case
        print(rounded_length)
        print()  # Blank line between outputs

calculate_minimal_wall_length()
