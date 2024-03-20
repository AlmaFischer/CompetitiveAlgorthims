def subida(a, b, h):
    movs = 0
    distance = 0
    if a == b:
        return -1
    if a < 0 or a > 100 or b < 0 or b > 100 or h <= 0 or h > 100000:
        return -1
    while True:
        distance += a
        movs +=1
        if distance >= h:
            return movs
        distance -=b
print(subida(*map(int,input().split())))
