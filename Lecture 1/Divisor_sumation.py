import sys
import math
def calculate(number):
    sum=0
    if number > 50000 and number < 1:
        print(0)
        exit()
    j=1
    while j < number:
        if number % j == 0:
            sum += j
        j+=1
    print(sum) 
"""number=list(map(int, sys.stdin.readlines()))
for n in number[1:]:
    calculate(n)"""


num_tests = int(input())
for _ in range(num_tests):
    num = int(input())
    calculate(num)
