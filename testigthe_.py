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

test = 1
data = []

while True:
    try:
        num = int(input())
        if num == -1:
            break
        data.append(num)
    except EOFError:
        break

data.reverse()
data_index = 0

while data_index < len(data):
    incoming_missile = data[data_index]
    data_index += 1
    interceptions = 1
    last = incoming_missile
    while True:
        if data_index >= len(data) or data[data_index] == -1:
            print(f"Test #{test}:\n  maximum possible interceptions: {interceptions}\n")
            test += 1
            data_index += 1
            break
        if data[data_index] > 32767 or data[data_index] < -1:
            print("Invalid input. Please make sure the numbers are in the range [-1, 32767].")
            exit()
        if data[data_index] <= last:
            last = data[data_index]
            interceptions += 1
        data_index += 1

