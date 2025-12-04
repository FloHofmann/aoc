import numpy as np


def find_max_within_first(bat_array, start, residuals, output):
    if residuals == 0:
        return output
    n = len(bat_array)
    last_start_allowed = n - residuals
    window = bat_array[start:last_start_allowed + 1]

    max_idx = int(np.argmax(window))
    max_idx = start + max_idx
    max_val = int(bat_array[max_idx])

    residuals -= 1
    start = max_idx + 1
    output = max_val * (10**residuals) + output
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

    # ensure length k
    stack = stack[:k]

    # build integer from digits
    result = 0
    for d in stack:
        result = result * 10 + d

    return result


# ---- core functions used for benchmarking (no I/O, no prints) ----

batteries: list[np.ndarray] = []  # will be filled in main


def d32_rec_core():
    total_batteries = 12
    s = 0
    for a in batteries:
        s += find_max_within_first(a, 0, total_batteries, 0)
    return s


def d32_single_core():
    total_batteries = 12
    s = 0
    for a in batteries:
        s += max_number_from_digits(a, total_batteries)
    return s


# ---- optional: original “full” versions that do I/O + print ----

def d32_rec():
    total_batteries = 12
    r = []
    for a in batteries:
        r.append(find_max_within_first(a, 0, total_batteries, 0))


def d32_single():
    total_batteries = 12
    r = []
    for a in batteries:
        r.append(max_number_from_digits(a, total_batteries))


if __name__ == "__main__":
    import pyperf

    # 1) Read and parse input ONCE
    with open("input.txt") as f:
        lines = [line.strip() for line in f if line.strip()]

    batteries = [np.array(list(line), dtype=int) for line in lines]

    # (Optional) sanity check: both methods give same result

    # 2) Benchmark only the algorithmic cores
    runner = pyperf.Runner()
    runner.bench_func("recursive_core", d32_rec_core)
    runner.bench_func("single_core", d32_single_core)
