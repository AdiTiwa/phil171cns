import sys

ITER_LIMIT = 2000
OVERFLOW_LIMIT = 1000

if len(sys.argv) < 2:
    print("enter name of program script")
    sys.exit(0)

filename = sys.argv[1]
program = []

with open(filename, "r") as file:
    for line in file:
        instruction = line.strip().split(" ")
        instruction = (instruction[0], *map(int, instruction[1:]))

        if not instruction[0] in "ID":
            print(f"error on line {len(program) + 1}: {instruction[0]} is not an instruction")
            sys.exit(1)

        if instruction[0] == "I" and not len(instruction[1:]) == 2:
            print(f"error on line {len(program) + 1}: 'I', or increment, requires 2 arguments")
            sys.exit(1)

        if instruction[0] == "D" and not len(instruction[1:]) == 3:
            print(f"error on line {len(program) + 1}: 'D', or decrement, requires 3 arguments")
            sys.exit(1)

        program.append(instruction)
print('lexed and parsed file!')

print('set your initial state with spaces between them (eg, $: 1 1 2 => R_0 = 1, R_1 = 1, R_2 = 2)')
print('remember; R_0 IS the starting PC, or the index of the starting instruction (start counting at 1, those who know)')
reg = list(map(int, input("$: ").split(" ")))
reg = [*reg, *[0 for _ in range(OVERFLOW_LIMIT - len(reg))]] # initalize the rest of the registers to 0 (please work :prayer_hands:)

for itr in range(ITER_LIMIT):
    try:
        instr = program[reg[0] - 1]
    except:
        print(f"program terminated at PC {reg[0]} at itr {itr}")
        
        last_nonzero = -1
        for idx, val in enumerate(reg):
            if val != 0:
                last_nonzero = idx

        print(f"registers: {reg[:last_nonzero + 1]}")
        break
    
    if instr[0] == "I":
        reg[instr[1]] += 1
        reg[0] = instr[2]

    if instr[0] == "D":
        if reg[instr[1]] > 0:
            reg[instr[1]] -= 1
            reg[0] = instr[2]
        else:
            reg[0] = instr[3]
