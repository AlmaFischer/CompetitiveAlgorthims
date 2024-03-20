data = input("put numbers here: ") # 0 1 2, 3 4 5, 6 7 8
mylist = data.split() #Lista de todos los valores
possibilities = [[],[],[]]
possibilities[0].append(int(mylist[3])+int(mylist[6]))
possibilities[0].append(int(mylist[4])+int(mylist[7]))
possibilities[0].append(int(mylist[5])+int(mylist[8]))
possibilities[1].append(int(mylist[0])+int(mylist[6]))
possibilities[1].append(int(mylist[1])+int(mylist[7]))
possibilities[1].append(int(mylist[2])+int(mylist[8]))
possibilities[2].append(int(mylist[0])+int(mylist[3]))
possibilities[2].append(int(mylist[1])+int(mylist[4]))
possibilities[2].append(int(mylist[2])+int(mylist[5]))
print(possibilities)
for x in possibilities:
    print(x)
