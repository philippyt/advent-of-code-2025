import numpy as np
from pathlib import Path

ASCII = 48

def ranges(p: str) -> np.ndarray:
    L = Path(p).read_bytes().splitlines()
    return np.array([[s - ASCII for s in l] for l in L], int)

def calc(p: str) -> int:
    R = ranges(p)
    _, m = R.shape
    T = R[:, :, None]
    O = R[:, None, :]
    E = T * 10 + O
    M = np.triu(np.ones((m, m), bool), 1)
    e = np.where(M, E, -1)
    A = e.max((1, 2))
    return int(A.sum())

print(calc("day_3/puzzle_input3.txt"))