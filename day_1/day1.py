import numpy as np
from pathlib import Path

def rotations(p):
    L = Path(p).read_text().splitlines()
    d = np.array([1 if r[0] == "R" else -1 for r in L], int)
    a = np.array([int(r[1:]) for r in L], int)
    return d, a

def calc(p):
    d, a = rotations(p)
    m = d * a
    x = (50 + np.cumsum(m)) % 100
    return np.sum(x == 0)

print(calc("day_1/puzzle_input.txt"))