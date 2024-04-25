t = int(input())

for tc in range(1, t + 1):
    team = []
    for i in range(10):
        player, a, d = input().split()
        a, d = int(a), int(d)
        team.append((player, a, d))
        
    team.sort(key=lambda x: (-x[1], x[2], x[0]))
    first_half = sorted(team[:5])
    second_half = sorted(team[5:])
    
    print(f"Case {tc}:")
    print("(" + ", ".join([x[0] for x in first_half]) + ")")
    print("(" + ", ".join([x[0] for x in second_half]) + ")")

