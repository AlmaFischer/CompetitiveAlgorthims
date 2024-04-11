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
    last_humble_number = 1
    index2 = index3 = index5 = index7 = 0
    
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    next_multiple_of_7 = 7
    
    for _ in range(1, n):
        next_humble = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5, next_multiple_of_7)
        last_humble_number = next_humble
        
        if next_humble == next_multiple_of_2:
            index2 += 1
            next_multiple_of_2 = last_humble_number * 2
        if next_humble == next_multiple_of_3:
            index3 += 1
            next_multiple_of_3 = last_humble_number * 3
        if next_humble == next_multiple_of_5:
            index5 += 1
            next_multiple_of_5 = last_humble_number * 5
        if next_humble == next_multiple_of_7:
            index7 += 1
            next_multiple_of_7 = last_humble_number * 7
            
    return last_humble_number

while True:
        n = int(input())
        if n == 0:
            break
        humble_number = nth_humble_number(n)
        print(f"The {ordinal(n)} humble number is {humble_number}.")