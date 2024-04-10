def is_in_danger(nazi_troops, castle):
    for i in range(len(nazi_troops)):
        for j in range(i+1, len(nazi_troops)):
            for k in range(j+1, len(nazi_troops)):
                for l in range(k+1, len(nazi_troops)):
                    x1, y1 = nazi_troops[i]
                    x2, y2 = nazi_troops[j]
                    x3, y3 = nazi_troops[k]
                    x4, y4 = nazi_troops[l]

                    # Check if the castle is inside or on the border of the quadrilateral formed by the four Nazi troops
                    if ((x1*y2 - y1*x2) * (x2*y3 - y2*x3) < 0) != ((x3*y4 - y3*x4) * (x4*y1 - y4*x1) < 0):
                        return True
    return False

def main():
    # Read input
    n = int(input())
    nazi_troops = [tuple(map(int, input().split())) for _ in range(n)]
    s = int(input())
    castles = [tuple(map(int, input().split())) for _ in range(s)]

    # Check each castle for danger
    count = 0
    for castle in castles:
        if is_in_danger(nazi_troops, castle):
            count += 1

    # Output the result
    print(count)

if __name__ == "__main__":
    main()
