import numpy as np
from numpy.lib.stride_tricks import sliding_window_view as swv
from pathlib import Path

def ranges(p: str) -> np.ndarray:
    L = Path(p).read_text().splitlines()
    return np.array([[s == '@' for s in l] for l in L], int)

def calc(p: str) -> int:
    R = ranges(p)
    W = swv(np.pad(R, 1), (3, 3))
    N = W.sum(axis = (2, 3)) - R
    A = (R == 1) & (N < 4)
    return int(A.sum())

print(calc("day_4/puzzle_input4.txt"))