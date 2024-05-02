def bsearch(Trees, N, M):
    lo = 1
    hi = Trees[N-1]
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        count = 0
        for i in range(N):
            if Trees[i] > mid:
                count += Trees[i] - mid
        if count >= M:
            lo = mid
        else:
            hi = mid - 1
    return lo
N,M = map(int, input().split())
Trees = list(map(int, input().split()))
Trees.sort()
ans = bsearch(Trees, N, M)
print(ans)

