def subida(a, b, h):
    if a == b:
        return -1

    if a < 0 or a > 1000 or b < 0 or b > 1000 or h <= 0 or h > 100000:
        return -1
    avance = a - b
    ciclos = h // avance

    if h % avance != 0:
        ciclos += 1

    return ciclos
data = input() #5 0 15
data1=data.split()

print(subida(int(data1[0]),int(data1[1]),int(data1[2])))
