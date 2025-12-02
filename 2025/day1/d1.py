from pathlib import Path

def process_line(line, dial):
    if line.startswith('R'):
        number = int(line[1::])
        dial += number
        if dial > 99: 
            dial = dial % 100
    else:
        number = int(line[1::])
        dial -= number
        if dial < 0:
            dial = dial % 100
    return dial

def process_line_new_method(line: str, dial: int):
    """
    line: e.g. 'R50', 'L23'
    dial: current dial position in [0, 99]

    returns: (hits_this_line, new_dial)
    """
    line = line.strip()
    direction = line[0]
    steps = int(line[1:])
    p = dial % 100  # just in case

    # --- count how many times we hit 0 during this rotation ---
    if direction == 'R':
        # k such that p + k ≡ 0 (mod 100)
        r = (-p) % 100
    elif direction == 'L':
        # k such that p - k ≡ 0 (mod 100)
        r = p % 100
    else:
        raise ValueError(f"Unknown direction: {direction}")

    # first positive k where we hit 0
    first_k = r if r != 0 else 100

    if first_k > steps:
        hits = 0
    else:
        hits = 1 + (steps - first_k) // 100

    # --- update dial position ---
    if direction == 'R':
        dial = (p + steps) % 100
    else:  # 'L'
        dial = (p - steps) % 100

    return hits, dial

pos = 50         # starts at 50
total_cross = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        c, pos = process_line_new_method(line, pos)
        total_cross += c

print("Total crossings:", total_cross)
print("Final dial:", pos)
