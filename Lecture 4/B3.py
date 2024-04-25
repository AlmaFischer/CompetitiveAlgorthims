N, M, nSpike = map(int, input().split())
map = []
visited_go = [[0] * M for _ in range(N)]
visited_out = [[0] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
flag = [0]

def go_in_mazes(x, y, count, direct):
    if count > nSpike:
        return
    if direct == 1:
        visited_go[x][y] = 1
    else:
        visited_out[x][y] = 1

    if map[x][y] == 'x' and direct == 1:
        go_in_mazes(x, y, count, 2)
        return
    if map[x][y] == '@' and direct == 2:
        flag[0] = 1
        return
    for i in range(4):
        tempx = x + dx[i]
        tempy = y + dy[i]
        if 0 <= tempx < N and 0 <= tempy < M:
            if direct == 1 and not visited_go[tempx][tempy]:
                if map[tempx][tempy] != '#':
                    if map[tempx][tempy] == 's':
                        go_in_mazes(tempx, tempy, count + 1, direct)
                    else:
                        go_in_mazes(tempx, tempy, count, direct)
                if flag[0]:
                    return
            elif direct == 2 and not visited_out[tempx][tempy]:
                if map[tempx][tempy] != '#':
                    if map[tempx][tempy] == 's':
                        go_in_mazes(tempx, tempy, count + 1, direct)
                    else:
                        go_in_mazes(tempx, tempy, count, direct)
                if flag[0]:
                    return

    if direct == 1:
        visited_go[x][y] = 0
    else:
        visited_out[x][y] = 0

for _ in range(N):
    row = input()
    map.append(row)

startx, starty = -1, -1
for i in range(N):
    for j in range(M):
        if map[i][j] == '@':
            startx, starty = i, j
            break
    if startx != -1:
        break

flag[0] = 0
go_in_mazes(startx, starty, 0, 1)

if flag[0]:
    print("SUCCESS")
else:
    print("IMPOSSIBLE")
