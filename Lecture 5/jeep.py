def puede(cap, events, consume):
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

# Read input
test_cases = []
while True:
    line = list(input().split())
    d,c = int(line[0]),int(line[3])
    if c == 0:
        break

    eventos = []
    consumption = [c]

    while True:
        line = input().split()
        d, evento = int(line[0]), line[1]
        if evento == "Goal":
            break
        eventos.append((d, evento))
        if evento == "Gas":
            input()
        elif evento == "Fuel":
            c = int(line[2])
            consumption.append(c)

    eventos.append((d, evento))
    lo = 0
    hi = 10000
    ans = 0
    while abs(hi - lo) > 0:
        mid = (lo + hi) / 2.0
        if puede(mid, eventos, consumption):
            ans = mid
            hi = mid
        else:
            lo = mid
    print("{:.3f}".format(ans))