def validate(N, H1, H2):
    H = 0
    for i in range(3, N + 1):
        H = 2 * H2 + 2 - H1
        if H < 0:
            return -1
        H1 = H2
        H2 = H
    return H

while True:
    try:
        N, A = map(float, input().split())
    except EOFError:
        break

    left, right = 0, A
    ret = 0
    for _ in range(50):
        mid = (left + right) / 2
        t = validate(int(N), A, mid)
        if t >= 0:
            right = mid
            ret = t
        else:
            left = mid
    print("{:.2f}".format(ret))
