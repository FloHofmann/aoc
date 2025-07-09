from pathlib import Path
max_cal_sum = 0

with open(Path("/home/flo/github/aoc/2022/inp-d1.txt"), 'r') as f:
    count = 0
    for line in f:
        if line.strip():
            count += int(line)
        else:
            if max_cal_sum < count:
                max_cal_sum = count

            count = 0

print(max_cal_sum)
