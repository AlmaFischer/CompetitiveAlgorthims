T = int(input())

for _ in range(T):
    M, N, Q = map(int, input().split())
    grid = [list(input()) for _ in range(M)]
    
    print(M, N, Q)
    for _ in range(Q):
        r, c = map(int, input().split())
        valid = True
        res = 1
        center = grid[r][c]
        len_ = 3
        
        while valid:
            iniciofila = r - len_ // 2
            finfila = r + len_ // 2
            iniciocolumna = c - len_ // 2
            fincolumna = c + len_ // 2
            
            if iniciofila < 0 or iniciocolumna < 0:#casos borde
                valid = False
            if finfila >= M or fincolumna >= N:
                valid = False
            
            for i in range(iniciofila, finfila + 1):
                if not valid:
                    break
                if grid[i][iniciocolumna] != center or grid[i][fincolumna] != center:
                    valid = False
            for i in range(iniciocolumna, fincolumna + 1):
                if not valid:
                    break
                if grid[iniciofila][i] != center or grid[finfila][i] != center:
                    valid = False
            if valid:
                res = len_
            len_ += 2
        
        print(res)
