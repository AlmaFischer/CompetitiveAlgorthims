import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def buscar_numero(matriz, numero):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == numero:
                return fila,columna

pattern = [[int(x) for x in input().split()] for _ in range(3)]
total_length = 0
for i in range(1,9):
    x1,y1=buscar_numero(pattern,i)
    x2,y2=buscar_numero(pattern,i+1)
    total_length+=calculate_distance(x1,y1,x2,y2)
print(total_length)
