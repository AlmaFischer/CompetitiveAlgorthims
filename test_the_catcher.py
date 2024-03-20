import sys

while True:
    try:
        input_lines = sys.stdin.readlines()
        if not input_lines:
            break
        for line in input_lines:
            n, m = map(int, line.split())
            s = 0
            if n > m:
                n, m = m, n
            for i in range(n, m + 1):
                c = 1
                j = i
                while j > 1:
                    if j % 2 == 0:
                        j //= 2
                    else:
                        j = 3 * j + 1
                    c += 1
                if c >= s:
                    s = c
            print(n, m, s)
    except EOFError:
        break


