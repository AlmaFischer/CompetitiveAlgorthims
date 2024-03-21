
test=1
Err=False
import sys
lines = sys.stdin.readlines()
data = [int(number) for number in lines]
while Err == False:
    incoming_missile= int(input())
    if incoming_missile <= -1:
        break
    interceptions = 1
    last = incoming_missile
    while True:
        incoming_missile= int(input())
        if incoming_missile == -1:
            print(f"Test #{test}:\n  maximum possible interceptions: {interceptions}\n")
            test+=1
            break
        if incoming_missile > 32767 or incoming_missile < -1:
            Err=True
            break
        if incoming_missile <= last:
            last=incoming_missile
            interceptions += 1
    