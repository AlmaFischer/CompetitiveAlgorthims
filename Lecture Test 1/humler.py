import itertools

def ordinal(n):
    text=str(n)[-1]
    ene=str(n)
    if text == '1':
        return ene + 'st'
    elif text == '2':
        return ene + 'nd'
    elif text == '3':
        return ene + 'rd'
    else:
        return ene + 'th'
def nth_humble_number(n):
    humble_numbers = [1]
    factors = [2, 3, 5, 7]
    pointers = [0] * len(factors)
    for _ in range(n - 1):
        next_humble = min(humble_numbers[pointers[i]] * factor for i, factor in enumerate(factors))
        humble_numbers.append(next_humble)
        for i, factor in enumerate(factors):
            if humble_numbers[pointers[i]] * factor == next_humble:
                pointers[i] += 1
    return humble_numbers[-1]

def humble_numbers2():
    primes = (2,3,5,7)
    result = [1]
    yield 1

    def make_multiple(_p):
        return (_p * result[i] for i in itertools.count())

    iters = map(make_multiple, primes)
    merged = heapq.merge(*iters)
    for k,_ in itertools.groupby(merged):
        result.append(k)
        yield k

while True:
    n = int(input())
    if n == 0:
        break
    humble_number = nth_humble_number(n)
    print(f"The {ordinal(n)} humble number is {humble_number}.")