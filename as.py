
import itertools

def solve(front_sp, rear_sp):
    ratios = []
    for front in front_sp:
        for rear in rear_sp:
            ratios.append(rear / front)
    ratios.sort()
    max_spread = 0
    for i in range(len(ratios) - 1):
        spread = ratios[i + 1] / ratios[i]
        if spread > max_spread:
            max_spread = spread
    
    return max_spread
while True:
    line = input().split()
    if line[0] == "0":
        break
    f, r = map(int, line)
    front_sp = list(map(int, input().split()))
    rear_sp = list(map(int, input().split()))
    
    max_spread = solve(front_sp, rear_sp)
    print("{:.2f}".format(max_spread))
