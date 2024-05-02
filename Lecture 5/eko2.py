import bisect
def count_trees_above(height, Trees):
    index = bisect.bisect_right(Trees, height)
    return sum(Trees[i] - height for i in range(index, len(Trees)))
def bsearch(Trees, M):
    lo = 1
    hi = Trees[-1]

    while lo < hi:
        mid = (lo + hi + 1) // 2
        count = count_trees_above(mid, Trees)
        
        if count >= M:
            lo = mid
        else:
            hi = mid - 1
    
    return lo

N, M = map(int, input().split())
Trees = sorted(map(int, input().split()))
ans = bsearch(Trees, M)
print(ans)
