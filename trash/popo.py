
def generar_permutaciones():
    permutaciones = []
    for i in range(3):
        for j in range(3):
            if i != j:
                for k in range(3):
                    if k != i and k != j:
                        permutaciones.append([i, j, k])
    return permutaciones
def calcular_movimientos(contenedores, orden):
    movimientos = 0
    for i in range(3):
        for j in range(3):
            if i != j:
                movimientos += contenedores[i][orden[i]]
    return movimientos
def movimientos_minimos(contenedores):
    min_movimientos = float('inf')
    min_orden = None
    ordenes = generar_permutaciones()
    for orden in ordenes:
        movimientos = calcular_movimientos(contenedores, orden)
        if movimientos < min_movimientos:
            min_movimientos = movimientos
            min_orden = orden
        elif movimientos == min_movimientos:
            min_orden = min(orden, min_orden)

    return min_orden, min_movimientos


linea = input().strip()
contenedores = list(map(int, linea.split()))
orden, movimientos = movimientos_minimos([contenedores[:3], contenedores[3:6], contenedores[6:]])
colores_contenedor = ['B', 'G', 'C']
orden_salida = ''.join([colores_contenedor[i] for i in orden])
print(orden_salida, movimientos)
