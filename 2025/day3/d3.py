import numpy as np


def d31():
    f = open("input.txt")
    batteries = f.read().strip()
    batteries = batteries.split('\n')

    r = []

    for i in batteries:
        a = np.array(list(i), dtype=int)
        max_idx = np.argmax(a[:-1])
        decimal = a[max_idx]
        digit = np.max(a[max_idx+1:])
        r.append(10*decimal + digit)

    print(sum(r))
    f.close()


def d32_rec():
    f = open("input.txt")
    batteries = f.read().strip()
    batteries = batteries.split('\n')

    total_batteries = 12

    r = []

    for i in batteries:
        a = np.array(list(i), dtype=int)
        storage = 0
        max_num = find_max_within_first(a, 0, total_batteries, storage)
        r.append(max_num)

    print(sum(r))
    f.close()


def d32_single():
    f = open("input.txt")
    batteries = f.read().strip()
    batteries = batteries.split('\n')

    total_batteries = 12

    r = []

    for i in batteries:
        a = np.array(list(i), dtype=int)
        storage = 0
        max_num = max_number_from_digits(a, total_batteries)
        r.append(max_num)

    print(sum(r))
    f.close()


def find_max_within_first(bat_array, start, residuals, output):
    if residuals == 0:
        return output
    n = len(bat_array)
    last_start_allowed = n-residuals
    window = bat_array[start:last_start_allowed+1]

    max_idx = int(np.argmax(window))
    max_idx = start + max_idx
    max_val = int(bat_array[max_idx])

    residuals -= 1
    start = max_idx + 1
    output = max_val*(10**residuals) + output
    return find_max_within_first(bat_array, start, residuals, output)


def max_number_from_digits(bat_array, k):
    drop = len(bat_array) - k  # how many digits we can discard
    stack = []

    for d in bat_array:
        d = int(d)
        while drop and stack and stack[-1] < d:
            stack.pop()
            drop -= 1
        stack.append(d)

    # if we never dropped enough (sequence already non-decreasing),
    # just take the first k digits
    stack = stack[:k]

    # build integer from digits
    result = 0
    for d in stack:
        result = result * 10 + d

    return result


if __name__ == "__main__":
    import pyperf
    runner = pyperf.Runner()

    runner.timeit(
        name='recursive',
        stmt=d32_rec(),
    )

    runner.timeit(
        name='single',
        stmt=d32_single(),
    )
