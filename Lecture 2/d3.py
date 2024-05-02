import math

DEBUG = False

def intersection(X1, Y1, X2, Y2, R):
    # check if goalie is in the way of the ball
    if X1 < 0.0:
        return False
    dx = X2 - X1
    dy = Y2 - Y1
    return dx*dx + dy*dy <= R*R

def main():
    T = int(input())
    for _ in range(T):
        input()
        ballX, ballY = map(float, input().split())
        goalieX, goalieY, goalieRad = map(float, input().split())
        shiftX = ballX
        shiftY = ballY
        netX = 52.50 - shiftX
        netY1 = 3.66 - shiftY
        netY2 = -3.66 - shiftY
        ballX = 0.0
        ballY = 0.0
        goalieX -= shiftX
        goalieY -= shiftY
        slope1 = netY1 / netX if netX != 0 else 0
        slope2 = netY2 / netX if netX != 0 else 0

        # perpendicular slope of line from center of circle to lines
        slopeBall1 = -netX / netY1 if netY1 != 0 else 0
        slopeBall2 = -netX / netY2 if netY2 != 0 else 0

        # find equation of lines given the above slopes
        b1 = goalieY - slopeBall1 * goalieX
        b2 = goalieY - slopeBall2 * goalieX

        # find point of intersection
        x1 = b1 / (slope1 - slopeBall1) if slope1 != slopeBall1 else goalieX
        x2 = b2 / (slope2 - slopeBall2) if slope2 != slopeBall2 else goalieX
        y1 = slopeBall1 * x1 + b1
        y2 = slopeBall2 * x2 + b2

        if netY1 == 0:
            x1 = goalieX
            y1 = 0
        if netY2 == 0:
            x2 = goalieX
            y2 = 0
        if netX == 0 and goalieX == 0:
            x1 = x2 = 0
            if (ballY < netY2 and goalieY > netY2) or (ballY > netY1 and goalieY < netY1):
                y1 = y2 = ballY
            else:
                y1 = y2 = goalieY
        elif netX == 0:
            x1 = x2 = 0
            y1 = y2 = goalieY


        # check if point of intersection is within radius of the goalie
        intersec1 = intersection(x1, y1, goalieX, goalieY, goalieRad)
        intersec2 = intersection(x2, y2, goalieX, goalieY, goalieRad)
        intersec3 = intersection(ballX, ballY, goalieX, goalieY, goalieRad)

        if intersec1 and intersec2 or intersec3:
            print("No goal...")
        else:
            print("Goal!")

if __name__ == "__main__":
    main()
