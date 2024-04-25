MAX = 5842
HN = [0] * (MAX + 10)

def generate_humble_numbers():
    global HN
    HN[1] = 1
    w, x, y, z = 1, 1, 1, 1

    for i in range(2, MAX + 1):
        HN[i] = min(min(2 * HN[w], 3 * HN[x]), min(5 * HN[y], 7 * HN[z]))

        if HN[i] == 2 * HN[w]:
            w += 1
        if HN[i] == 3 * HN[x]:
            x += 1
        if HN[i] == 5 * HN[y]:
            y += 1
        if HN[i] == 7 * HN[z]:
            z += 1
generate_humble_numbers()

while True:
    N = int(input())
    if N == 0:
        break
    if 10 < N % 100 < 20:
        print(f"The {N}th humble number is {HN[N]}.")
    elif N % 10 == 1:
        print(f"The {N}st humble number is {HN[N]}.")
    elif N % 10 == 2:
        print(f"The {N}nd humble number is {HN[N]}.")
    elif N % 10 == 3:
        print(f"The {N}rd humble number is {HN[N]}.")
    else:
        print(f"The {N}th humble number is {HN[N]}.")


