import numpy as np
from scipy.signal import convolve2d


def test():
    out_1 = d4_1("test.txt")
    assert out_1 == 13
    out_2 = d4_2("test.txt")
    assert out_2 == 43
    print('tests passed')


def d4_1(input_path):
    f = open(input_path)
    input = f.read().strip().replace('@', '1').replace('.', '0').split('\n')
    mat = np.array(
        [list(i) for i in input], dtype=int)
    mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    conv_ = convolve2d(mat, mask, 'same', 'fill', fillvalue=0)
    mask = (mat > 0) & (conv_ < 4)
    count = mask.sum()

    return count


def d4_2(input_path):
    f = open(input_path)
    input = f.read().strip().replace('@', '1').replace('.', '0').split('\n')
    mat = np.array(
        [list(i) for i in input], dtype=int)
    mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    count = remove_roll(mat, mask, 0)
    return count


def remove_roll(mat, mask, count):
    conv_ = convolve2d(mat, mask, 'same', 'fill', fillvalue=0)
    removable = (mat > 0) & (conv_ < 4)
    if removable.sum() == 0:
        return count
    mat[removable] = 0
    count = count + removable.sum()
    return remove_roll(mat, mask, count)


if __name__ == "__main__":
    out = d4_2("input.txt")
    print(out)
