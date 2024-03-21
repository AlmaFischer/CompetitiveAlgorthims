import sys

def c_movements(bins, order):
    total_movements = 0 
    for i, color in enumerate('BGC'): 
        for j, bin_counts in enumerate(bins[i]):
            if color != order[j]: 
                total_movements += bin_counts 
    return total_movements
"""
Explicacion c_movements
si le damos a la funcion el orden GCB y los bins (basurero 0) 1 2 3 |(basurero 1) 4 5 6 |(basurero 2) 7 8 9
iteramos primero a traves de los colores BGC en la linea 5, es decir que primero vamos con "B", asiq vamos a mover a su basurero todos los B de cada bin
En este caso como B va al final de GCB solo se suma 1 y 4 a total_movements =5
Luego con el "G"
En este caso como G va primero en NUESTRO orden solo se suman los valores 5 y 8 a total_movements=18
Finalmente con el "C":
En la primera iteracion Suma el valor 3 y en la 3ra  iteracion suma el valor 9 a total_movements=30
Finalmente lo retorna
"""
def min_movements(bins):
    min_movements = float('inf')#infinito
    min_order = None
    for order in ['GCB','GBC','CGB','CBG','BGC','BCG']:
        movements = c_movements(bins, order) #cantidad de movimiento para ese orden especifico
        if movements <= min_movements: #si es menor o el va primero ABC
            min_movements = int(movements)
            min_order = order
    return min_order, min_movements
"""
Se crea inicia el valor de min_movements como infinito
luego va a probando cual es el que toma menos movimentos urtilizando la funcion c_movements
"""
bottles = [list(map(int, line.split())) for line in sys.stdin.readlines()]
results = []
for bins in bottles:
    bins = [bins[:3], bins[3:6], bins[6:]]
    order, movements = min_movements(bins) #ejcutamos min_movements
    results.append((order, movements)) #guardamos los resultados
for order, movements in results:
    print(order, movements)

