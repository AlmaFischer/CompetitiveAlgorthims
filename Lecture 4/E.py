def dfs(grid, visited, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '.' or visited[row][col]:
        return 0
    visited[row][col] = True
    count = 1
    count += dfs(grid, visited, row + 1, col)
    count += dfs(grid, visited, row - 1, col)
    count += dfs(grid, visited, row, col + 1)
    count += dfs(grid, visited, row, col - 1)
    return count

def count_octaves(grid):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    octaves = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'X' and not visited[i][j]:
                octave_size = dfs(grid, visited, i, j)
                if octave_size % 8 == 0:
                    octaves += octave_size // 8
    return octaves

T = int(input())
for _ in range(T):
    N = int(input())
    grid = [input() for _ in range(N)]
    print(count_octaves(grid))