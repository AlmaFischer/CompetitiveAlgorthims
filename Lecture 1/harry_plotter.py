import math
def probability(N,M):
    if N + M == 0:
        return 0
    if N > M:
        print("0.000000")
        #https://en.wikipedia.org/wiki/Bertrand%27s_ballot_theorem
    else:
        print("%.6f" %((M-N+1)/(M+1))) 
while True:
    N,M = map(int,input().split())
    if N == 0 and M == 0:
        break
    probability(N,M)