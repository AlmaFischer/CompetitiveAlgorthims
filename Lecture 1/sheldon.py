import math
def counting(A,B,C,P,case):
    if A > 100000000 and B > 100000000 and C > 100000000 and P > 100000000:
        return 0
    gcd_value = math.gcd(A, math.gcd(B, C))
    if C / gcd_value < 200:
        return 0
    count = 0
    max_i = P // A
    max_j = P // B
    max_k = P // C
    for i in range(max_i + 1):
        for j in range(min(max_j, (P - A*i) // B) + 1):
            k_remainder = P - A*i - B*j
            if k_remainder % C == 0 and k_remainder // C <= max_k:
                count += 1

    print(f"Case {case}: {count}")
num_tests = int(input())
for _ in range(num_tests):
    A,B,C,P = list(map(int,input().split()))
    counting(A,B,C,P,num_tests)