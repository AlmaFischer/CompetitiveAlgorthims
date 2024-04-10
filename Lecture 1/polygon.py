
def horner_method(Cs, x):
    result = Cs[0]
    for i in range(1, len(Cs)):
        result = result * x + Cs[i]
    return result

def solve(ces, exes):
    results = []
    for x in exes:
        result = horner_method(ces,x)
        results.append(result)
    print(' '.join(map(str, results)))
    return results

while True:
    try:
        ces = list(map(int, input().split()))
        exes = list(map(int, input().split()))
        solve(ces, exes)
    except:
        break
