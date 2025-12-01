from pathlib import Path

def process_line(line, dial):
    if line.startswith('R'):
        number = int(line[1::])
        dial += number
        if dial > 99: 
            dial = dial % 99 -1
    else:
        number = int(line[1::])
        dial -= number
        if dial < 0:
            dial = dial % 99 + 1
    return dial

nulcount = 0
dial = 50

with open(Path("input.txt")) as f:
    for line in f:
        print(f"Dial: {dial}\n")
        l = line.strip()
        print(l)
        if l == "":
            continue
        dial = process_line(l, dial)
        print(f"new dial: {dial}\n\n")
        if dial == 0:
            nulcount += 1

    print(nulcount)
