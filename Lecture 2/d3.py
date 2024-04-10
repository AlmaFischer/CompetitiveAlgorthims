def intersection(x1, y1, x2, y2, r):
    return (x2 - x1)**2 + (y2 - y1)**2 <= r**2

def main():
    T = int(input())
    for _ in range(T):
        input()
        ball_x, ball_y  = map(float, input().split())
        goalie_x, goalie_y, goalie_rad = map(float, input().split())
        net_x = 52.50 - ball_x
        net_y1, net_y2 = (3.66 - ball_y), (-3.66 - ball_y)
        goalie_x -= ball_x
        goalie_y -= ball_y

        slopes = [net_y1 / net_x if net_x != 0 else 0, net_y2 / net_x if net_x != 0 else 0]
        ball_slopes = [-net_x / net_y if net_y != 0 else 0 for net_y in [net_y1, net_y2]]
        bs = [goalie_y - ball_slopes[i] * goalie_x for i in range(2)]
        points = [(bs[i] / (slopes[i] - ball_slopes[i]), ball_slopes[i] * bs[i] / (slopes[i] - ball_slopes[i])) if slopes[i] != ball_slopes[i] else (goalie_x, goalie_y) for i in range(2)]

        for i in range(2):
            if net_y1 == 0 and i == 0:
                points[i] = (goalie_x, 0)
            elif net_y2 == 0 and i == 1:
                points[i] = (goalie_x, 0)
            elif net_x == 0 and goalie_x == 0:
                points[i] = (0, ball_y if (ball_y < net_y2 and goalie_y > net_y2) or (ball_y > net_y1 and goalie_y < net_y1) else goalie_y)
            elif net_x == 0:
                points[i] = (0, goalie_y)

        if intersection(*points[0], goalie_x, goalie_y, goalie_rad) and intersection(*points[1], goalie_x, goalie_y, goalie_rad) or intersection(ball_x, ball_y, goalie_x, goalie_y, goalie_rad):
            print("No goal...")
        else:
            print("Goal!")

if __name__ == "__main__":
    main()
