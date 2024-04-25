max_len = 8
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def check(bit_set, n, x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return (bit_set >> (x * n + y)) & 1 == 0

def calculate(bit_set, n, start_x, start_y, length, result_set):
    if length == 0:
        result_set.add(bit_set)
        return
    for i in range(len(dx)):
        x = start_x + dx[i]
        y = start_y + dy[i]
        if check(bit_set, n, x, y):
            k = x * n + y
            bit_set ^= 1 <<k
            calculate(bit_set, n, x, y, length - 1, result_set)
            bit_set ^= 1 << k


#main
test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    bit_set = 0
    for _ in range(n):
        row = input()
        for j in range(len(row)):
            if row[j] != 'X':
                bit_set ^= 1 << (_ * n + j)
    if n < 3:
        print(0)
        continue
    result_set = set()
    length = max_len
    for i in range(n):
        for j in range(n):
            k = i * n + j
            if not (bit_set >> k) & 1:
                bit_set ^= 1 << k
                calculate(bit_set, n, i, j, length - 1, result_set)
                bit_set ^= 1 << k
    print(len(result_set))


