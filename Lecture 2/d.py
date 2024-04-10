def isgoal(ball_x, ball_y, arquero_x, arquero_y, radioarquero):
    if ball_x > 52.5 and abs(ball_y) <= 3.66:
        return True
    if ball_x > arquero_x:
        return False
    if abs(ball_y - arquero_y) <= radioarquero:
        return False
    return True

num_cases = int(input())
for caso in range(num_cases):
    ball_x, ball_y = map(float, input().split())
    arquero_x, arquero_y, radioarquero = map(float, input().split())
    if isgoal(ball_x, ball_y, arquero_x, arquero_y, radioarquero):
        print("Goal!")
    else:
        print("No goal...")
