

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
    d, in_, _, c = map(str, input().split())
    c = int(c)
    if c == 0:
        break
    events = []
    consume = [c]
    while True:
        d, in_ = map(str, input().split())
        if in_ == "Goal":
            break
        events.append((int(d), in_))
        if in_ == "Gas":
            input()
        elif in_ == "Fuel":
            in_, c = map(str, input().split())
            consume.append(int(c))
    events.append((int(d), in_))
    lo, hi, ans = 0, 10000, 0
    while abs(hi - lo) > 0:
        mid = (lo + hi) / 2.0
        if can(mid, events, consume):
            ans = mid
            hi = mid
        else:
            lo = mid
    print("{:.3f}".format(ans))
