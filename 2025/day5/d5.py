import numpy as np


def d5_1():
    with open('test.txt') as f:
        inp = f.read()
        inp = inp.strip()
        string_split = inp.split('\n\n')
        db = string_split[0].replace("\n", ";")
        db = [tuple(map(int, r.split('-'))) for r in db.split(';')]
        items = string_split[1].split("\n")

        print(db)


if __name__ == "__main__":
    d5_1()
