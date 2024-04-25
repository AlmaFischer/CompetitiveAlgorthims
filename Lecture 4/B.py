
def dfs(maze,x,y,traps_l):
    num_spikes=0
        # Base cases: out of bounds or hit a wall
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] == '#':
        return False
    
    # Reached the treasure
    if maze[x][y] == 'x':
        if traps_l>=num_spikes:
            return True
        else:
            return False
    
    # Hit a trap
    if maze[x][y] == 's':
        num_spikes+=1
        if traps_l <= 0:
            return False
        traps_l -= 1
    
    # Mark the current position as visited
    maze[x][y] = '#'
    
    # Explore in all four directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        if dfs(maze, x + dx, y + dy, traps_l):
            return True
    
    return False
def maze_adventure(maze,traps_l):
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] == '@':
                return dfs(maze,x,y,traps_l)
n,m,j = map(int,input().split())
grid = [input() for _ in range(n)]
print(maze_adventure(grid,j))


