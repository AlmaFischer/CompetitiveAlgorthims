def recur(r, c, index, level):
    global fg, point, sp, tr
    if level == space:
        if c == tr:
            return True
        return False
    fg[index] = True
    for i in range(sp):
        if fg[point[i]['ind']]:
            continue
        if c == point[i]['r']:
            if recur(point[i]['r'], point[i]['c'], point[i]['ind'], level + 1):
                return True
    fg[index] = False
    return False
def Cal():
    x = recur(sr, sc, 30, 0)
    if x:
        print("YES")
    else:
        print("NO")
    for x in range(35):
        fg[x] = False


while True:
    space = int(input())
    if space == 0:
        break
    spices = int(input())
    sr, sc = map(int, input().split())
    tr, tc = map(int, input().split())
    sp = spices
    point = []
    for i in range(spices):
        r, c = map(int, input().split())
        point.append({'r': r, 'c': c, 'ind': i})
        if r != c:
            point.append({'r': c, 'c': r, 'ind': i})
            sp += 1
    fg = [False] * 40
    Cal()
