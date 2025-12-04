def day2_1():
    import math
    f = open('input.txt')
    line = f.read()
    line = line.strip().replace("'", "").replace('\n', '')
    ranges = line.split(',')
    invalids = []
    for i in ranges:
        r1 = i.split('-')
        r = range(int(r1[0]), int(r1[1])+1)
        for j in r:
            num_digits = int(math.log10(j)+1)
            str_num = str(j)
            if (num_digits % 2 == 0) and (str_num[0:int(num_digits/2)] == str_num[int(num_digits/2)::]):
                invalids.append(j)

    f.close()
    print(sum(invalids))


def day2_2():
    import math
    f = open('input.txt')
    line = f.read()
    line = line.strip().replace('\n', '')

    ranges = line.split(',')
    invalids = []
    for i in ranges:
        r = i.split('-')
        r = range(int(r[0]), int(r[1])+1)

        for j in r:
            str_num = str(j)

            doubled = (str_num + str_num)[1:-1]
            idx = doubled.find(str_num)
            if idx == -1:
                continue
            else:
                invalids.append(j)

    f.close()
    print(sum(invalids))


if __name__ == "__main__":
    day2_2()
