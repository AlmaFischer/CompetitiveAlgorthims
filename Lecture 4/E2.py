def find_solution(size, values, pieces, used):
    if size == 0:
        return values[0] == values[1]
    if size == 1:
        for i in range(len(pieces)):
            if not used[i]:
                if (pieces[i][0] == values[0] and pieces[i][1] == values[1]) or \
                        (pieces[i][0] == values[1] and pieces[i][1] == values[0]):
                    return True
        return False
    
    possible = False
    
    for i in range(len(pieces)):
        if not used[i]:
            temp = [0, 0]
            
            if pieces[i][0] == values[0]:
                temp[0] = pieces[i][1]
            elif pieces[i][1] == values[0]:
                temp[0] = pieces[i][0]
            else:
                continue
            
            used[i] = True
            for j in range(len(pieces)):
                if not used[j]:
                    if pieces[j][0] == values[1]:
                        temp[1] = pieces[j][1]
                    elif pieces[j][1] == values[1]:
                        temp[1] = pieces[j][0]
                    else:
                        continue
                    
                    used[j] = True
                    possible = find_solution(size - 2, temp, pieces, used)
                    used[j] = False
            used[i] = False
        
        if possible:
            break
    
    return possible

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        ignore = input().split()
        values = [int(ignore[1]), int(ignore[2])]
        
        m = int(input())
        ignore = input()
        
        pieces = []
        for _ in range(m):
            piece = list(map(int, input().split()))
            pieces.append(piece)
        
        used = [False] * m
        
        if find_solution(n, values, pieces, used):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
