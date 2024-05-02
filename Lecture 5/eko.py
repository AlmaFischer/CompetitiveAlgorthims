import bisect
def wood_cutting(M, Trees):
    Trees.sort()
    left, right = 0, Trees[-1]
    while left < right:
        mid = (left + right + 1) // 2
        idx = bisect.bisect_right(Trees, mid)
        total_wood = sum(tree - mid for tree in Trees[idx:])
        if total_wood < M:
            right = mid - 1
        else:
            left = mid
    return left
N, M = map(int, input().split())
Trees = list(map(int, input().split()))
print(wood_cutting(M,Trees))