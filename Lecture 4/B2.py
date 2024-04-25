
def get_out(maze,x,y,traps_l):
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] == '#':
        return False
    if maze[x][y] == '@':
        return True
    if maze[x][y] == 's':
        if traps_l <= 0:
            return False
        traps_l -= 1
    maze[x][y] = '#'
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        if get_out(maze, x + dx, y + dy, traps_l):
            return True
    return False

def dfs(maze, x, y, traps_l):
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] == '#':
        return False
    if maze[x][y] == 'x':
        return get_out(maze,x,y,traps_l)
    if maze[x][y] == 's':
        if traps_l <= 0:
            return False
        traps_l -= 1
    maze[x][y] = 'V'
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        if dfs(maze, x + dx, y + dy, traps_l):
            return True
    
    return False

def maze_adventure(maze, traps_l,arrobas):
    for _ in range(arrobas):
        for x in range(len(maze)):
            for y in range(len(maze[x])):
                if maze[x][y] == '@':
                    maze[x][y]=="#"
                    result = dfs(maze, x, y, traps_l)
                    if result == False:
                        continue
                    if result == True:
                        return result
n, m, j = map(int, input().split())
maze = [list(input()) for _ in range(n)]
maze2=maze.copy()
arrobas=0
for x in maze:
    for y in maze:
        if y == '@':
            arrobas+=1
print("SUCCESS" if maze_adventure(maze, j,arrobas) else "IMPOSSIBLE")
