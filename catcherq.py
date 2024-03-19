import sys

test = 1
Err = False
lines = sys.stdin.readlines()
data = [int(number) for number in lines]
data_index = 0

while Err == False:
    if data[data_index] == -1:
        break
    incoming_missile = data[data_index]
    data_index += 1
    interceptions = 1
    last = incoming_missile
    while True:
        if data[data_index] == -1:
            print(f"Test #{test}:\n maximum possible interceptions: {interceptions}\n")
            test += 1
            data_index += 1
            break
        if data[data_index] > 32767 or data[data_index] < -1:
            Err = True
            break
        if data[data_index] <= last:
            last = data[data_index]
            interceptions += 1
        data_index += 1

