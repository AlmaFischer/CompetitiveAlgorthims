import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def buscar_numero(matriz, numero):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == numero:
                return fila, columna
    return None, None  # Return None if number not found

pattern = [[int(x) for x in input().split()] for _ in range(3)]
total_length = 0
for i in range(1, 10):
    x1, y1 = buscar_numero(pattern, i)
    x2, y2 = buscar_numero(pattern, i + 1)
    print("Number:", i)
    print("x1, y1:", x1, y1)
    print("x2, y2:", x2, y2)
    if x1 is not None and x2 is not None:  # Check if both points are found
        total_length += calculate_distance(x1, y1, x2, y2)
    else:
        print("Number", i+1, "not found. Total length up to this point:", total_length)
        break  # Break loop if any point is not found
else:
    print("All numbers found. Total length:", total_length)
