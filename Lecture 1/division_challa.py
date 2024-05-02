import sys
import math

def find_divisors(number):
    sum_div=0
    for i in range(1,int(math.sqrt(number))+1):
        if number % i == 0:
            sum_div+=i
            if number // i != i:
                sum_div += number//i
    print(sum_div)
"""def calculate(number):
    sum_div=0
    if number > 50000 and number < 1:
        print(0)
        return
    sqrt_number = int(math.sqrt(number))
    for i in range(1,sqrt_number + 1):
        if number % i == 0:
            sum_div += i
            if sqrt_number != i:
                sum_div += number//i

    print(sum_div)
"""
number=list(map(int, sys.stdin.readlines()))
for n in number:
    find_divisors(n)