import sys

while True:
    try:
        r, c = map(int, input().split())
        ans = 0
        terrain = []
        for row in range(r):
            terrain.append(list(input()))
        for i in range(r):
            for j in range(c):
                k = 1
                
                if terrain[i][j] == '*':
                    k = 0
                    continue
                #vamos porbando arriba abajo al lado y al otro
                if i+1 < r and terrain[i+1][j] == '*':
                    k = 0
                    continue

                if i-1 >= 0 and terrain[i-1][j] == '*':
                    k = 0
                    continue
                if j+1 < c and terrain[i][j+1] == '*':
                    k = 0
                    continue
                if j-1 >= 0 and terrain[i][j-1] == '*':
                    k = 0
                    continue

                if k:
                    ans += 1

        print(ans)
    except EOFError:
        break

