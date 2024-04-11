import math
T = int(input())
for _ in range(T):
    x, y, z = map(int, input().split())
    totaltime=x+y
    timeexpectedbyfamily=totaltime/3
    ExtraTimeA=x-timeexpectedbyfamily
    amount_A = ExtraTimeA/timeexpectedbyfamily*z
    print(int(round(amount_A)))
