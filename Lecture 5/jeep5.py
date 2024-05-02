import sys
for line in sys.stdin:
    if line.strip() == "0 Fuel consumption 0":
        break
    curr = 0.0
    tanque = 0.0
    distanica = 0
    consumption = 0
    leak = 0
    while True:
        parts = line.strip().split()
        n = int(parts[0])
        s = parts[1]
        curr += leak * (n - distanica)
        curr += (consumption / 100.0) * (n - distanica)
        tanque = max(curr, tanque)
        if s == "Goal":
            break
        if s == "Fuel":
            consumption = int(parts[3])
        elif s == "Leak":
            leak += 1
        elif s =="Mechanic":
            leak = 0
        elif s == "Gas":
            curr = 0.0
        distanica = n
        line = input()
    print("{:.3f}".format(tanque))


