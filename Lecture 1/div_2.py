def divisor_sum(n):
    divisor_sum = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum

# Input
num_tests = int(input())
for _ in range(num_tests):
    num = int(input())
    print(divisor_sum(num))