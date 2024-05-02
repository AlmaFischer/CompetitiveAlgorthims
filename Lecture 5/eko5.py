def count_trees_above_height(Trees, height):
    return sum(max(0, tree - height) for tree in Trees)

def bsearch(Trees, M):
    lo, hi = 0, max(Trees)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        count = count_trees_above_height(Trees, mid)
        if count >= M:
            lo = mid
        else:
            hi = mid - 1
    return lo

N, M = map(int, input().split())
Trees = list(map(int, input().split()))
ans = bsearch(Trees, M)
print(ans)
