import math

vy = [[] for _ in range(20)]
vy0 = [[] for _ in range(20)]
vx = []
vc = 0
mind = 0

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def comparator(a, b):
    return abs(a - 5.0) < abs(b - 5.0)

def dfs(cx, cy, index, d):
    global mind
    if d >= mind:
        return
    
    if cx == 10.0 and cy == 5.0:
        mind = d
        return
    elif index >= vc:
        dfs(10.0, 5.0, index, d + dist(cx, cy, 10.0, 5.0))
    else:
        suc = True
        for p in range(index, vc):
            d1 = vx[p] - cx
            d2 = 10.0 - vx[p]
            y = (cy * d2 + 5.0 * d1) / (d1 + d2)
            if y < vy0[p][0] or (y > vy0[p][1] and y < vy0[p][2]) or y > vy0[p][3]:
                suc = False
                break
        
        if suc:
            dfs(10.0, 5.0, vc, d + dist(cx, cy, 10.0, 5.0))
            return

        for i in range(vc - 1, index - 1, -1):
            for j in range(4):
                suc = True
                for p in range(index, i):
                    d1 = vx[p] - cx
                    d2 = vx[i] - vx[p]
                    y = (cy * d2 + vy[i][j] * d1) / (d1 + d2)
                    if y < vy0[p][0] or (y > vy0[p][1] and y < vy0[p][2]) or y > vy0[p][3]:
                        suc = False
                        break
                
                if suc:
                    dfs(vx[i], vy[i][j], i + 1, d + dist(cx, cy, vx[i], vy[i][j]))

if __name__ == "__main__":
    while True:
        vc = int(input())
        if vc == -1:
            break
        
        vx.clear()
        for _ in range(vc):
            vy_tmp = []
            vy0_tmp = []
            tmp = float(input())
            vx.append(tmp)
            for _ in range(4):
                tmp = float(input())
                vy_tmp.append(tmp)
                vy0_tmp.append(tmp)
            vy_tmp.sort()
            vy.append(vy_tmp)
            vy0.append(vy0_tmp)

        mind = 1e99
        dfs(0.0, 5.0, 0, 0.0)
        print("{:.2f}".format(mind))
