def construct(numbers):
    L = []
    length_of_increasing = 0
    
    for num in numbers:
        pos = 0
        for i, val in enumerate(L):
            if val < num:
                pos = i + 1
            else:
                break
        
        if pos == len(L):
            L.append(num)
        else:
            L[pos] = num
        
        if pos + 1 >= length_of_increasing:
            length_of_increasing = pos + 1
    
    return length_of_increasing

if __name__ == "__main__":
    T = 1
    
    while True:
        numbers = []
        num = int(input())
        if num == -1:
            break
        
        numbers.append(num)
        
        while True:
            num = int(input())
            if num == -1:
                break
            numbers.append(num)
        
        numbers.reverse()
        length_of_increasing = construct(numbers)
        
        print(f"Test #{T}:\n  maximum possible interceptions: {length_of_increasing}")
        T += 1
