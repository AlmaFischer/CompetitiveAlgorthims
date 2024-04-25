def calc_pos(pos,instr,instructions):
    if instr=="LEFT":
        pos-=1
    if instr =="RIGHT":
        pos+=1
    elif instr.startswith("SAME AS"):
        index = int(instr.split()[-1]) - 1
        pos=calc_pos(pos,instructions[index],instructions)
    return pos
T = int(input().strip())
for _ in range(T):
    pos=0
    n = int(input().strip())
    instructions = []
    for _ in range(n):
        pepe=input().strip()
        instructions.append(pepe)
    for instr in instructions:
        pos =calc_pos(pos,instr,instructions)
    print(pos)

    
