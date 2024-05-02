
#Squares
def largest_square(grid, r, c):
    M, N = len(grid), len(grid[0])
    max_side = min(M, N)
    for side in range(max_side, 0, -1):
        half_side = side // 2
        for i in range(r - half_side, r + half_side + 1):
            if i < 0 or i >= M:
                continue
            for j in range(c - half_side, c + half_side + 1):
                if j < 0 or j >= N:
                    continue
                if grid[i][j] != grid[r][c]:
                    break
            else:
                continue
            break
        else:
            return side
    return 1

T = int(input())
for _ in range(T):
    M,N,Q = map(int,input().split())
    grid = [input() for _ in range(M)]
    print(M,N,Q)
    for _ in range(Q):
        r,c=map(int,input().split())
        print(largest_square(grid,r,c))