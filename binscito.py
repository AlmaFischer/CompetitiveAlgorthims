import sys

bottles = [list(map(int, line.split())) for line in sys.stdin.readlines()]

Brown = []
Green = []
Clear = []

order = {}

for row, line in enumerate(bottles):
    Brown.append([])
    Green.append([])
    Clear.append([])

    Brown[row].extend([bottles[row][3] + bottles[row][6], bottles[row][0] + bottles[row][6], bottles[row][0] + bottles[row][3]])
    Green[row].extend([bottles[row][4] + bottles[row][7], bottles[row][1] + bottles[row][7], bottles[row][1] + bottles[row][4]])
    Clear[row].extend([bottles[row][5] + bottles[row][8], bottles[row][2] + bottles[row][8], bottles[row][2] + bottles[row][5]])

    #deben estar en orden alfabetico
    order[row] = {"BCG": Brown[row][0] + Clear[row][1] + Green[row][2],
                "BGC": Brown[row][0] + Green[row][1] + Clear[row][2],
                "CBG": Clear[row][0] + Brown[row][1] + Green[row][2],
                "CGB": Clear[row][0] + Green[row][1] + Brown[row][2],
                "GBC": Green[row][0] + Brown[row][1] + Clear[row][2],
                "GCB": Green[row][0] + Clear[row][1] + Brown[row][2]}

for row in range(0, len(order)):
    moves = min(order[row].values())
    for key, value in order[row].items():
        if moves == value:
            print (key, value)
            break