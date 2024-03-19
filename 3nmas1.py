def cycle_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n+1
        length += 1
    return length
def max(i,j):
    max_len=0
    for num in range(i,j+1):
        current=cycle_length(num)
        if current > max_len:
            max_len = current
    return max_len

while True:
    i,j = map(int,input().split())
    if i > 10000 or j > 10000 or i < 0 or j < 0:
        break
    max_len = max(i,j)
    print(i,j,max_len)