
numbers = list(map(int, input().split()))
order = input().strip()
numbers.sort()
dic = {'A': numbers[0], 'B': numbers[1], 'C': numbers[2]}
for letter in order:
    print(dic[letter], end=' ')
