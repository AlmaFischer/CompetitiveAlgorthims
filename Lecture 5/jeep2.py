EPS = 1e-9

def can(cap, events, consume):
    leak = 0
    cur = cap
    dist = 0
    j = 0
    for p in events:
        km = p[0] - dist
        dist = p[0]
        consumption = km * (consume[j] / 100.0 + leak)
        cur -= consumption

        if cur < 0:
            return False
        if p[1] == "Gas":
            cur = cap
        elif p[1] == "Mechanic":
            leak = 0
        elif p[1] == "Leak":
            leak += 1
        elif p[1] == "Fuel":
            j += 1
    return True

while True:
    d, in_str, _, c = input().split()
    d = int(d)
    c = int(c)
    if c == 0:
        break

    events = []
    consume = [c]
    while True:
        d, in_str = input().split()
        d = int(d)
        if in_str == "Goal":
            break
        events.append((d, in_str))
        if in_str == "Gas":
            input()
        elif in_str == "Fuel":
            _, c = input().split()
            consume.append(int(c))

    events.append((d, in_str))
    lo = 0
    hi = 10000
    ans = 0
    while abs(hi - lo) > EPS:
        mid = (lo + hi) / 2.0
        if can(mid, events, consume):
            ans = mid
            hi = mid
        else:
            lo = mid
    print("{:.3f}".format(ans))
