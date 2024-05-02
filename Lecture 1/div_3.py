import sys
import math

def calculate(number):
    if number <= 1:
        return 0
    div_sum = 1
    sqrt_num = math.isqrt(number)

    for i in range(2, sqrt_num + 1):
        if number % i == 0:
            if i == (number // i):
                div_sum += i
            else:
                div_sum += (i + number // i)
    
    return div_sum

num_tests = int(input())
for _ in range(num_tests):
    num = int(input())
    print(calculate(num))
