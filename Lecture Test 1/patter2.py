import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def buscar_numero(matriz, numero):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == numero:
                return fila, columna
    return None

pattern = [[int(x) for x in input().split()] for _ in range(3)]

# Initialize variables to store the total length
total_length = 0

# Define the pivots' coordinates
pivots = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}

# Calculate the total length of the unlock pattern
for i in range(9):
    pos = buscar_numero(pattern, i)
    if pos is not None:
        x, y = pos
        if i != 1:  # Exclude the first pivot since it has no previous pivot
            prev_x, prev_y = pivots[i - 1]
            total_length += calculate_distance(prev_x, prev_y, x, y)
        total_length += calculate_distance(x, y, pivots[i][0], pivots[i][1])

print(total_length)
