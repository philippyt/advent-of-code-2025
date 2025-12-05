import numpy as np
from pathlib import Path

def ranges(p: str) -> np.ndarray:
    L = Path(p).read_text().splitlines()
    o = []
    for s in L:
        if "-" in s:
            a, b = s.split("-")
            o.append((int(a), int(b)))
    return np.array(o, int)

def calc2(p: str) -> int:
    R = ranges(p)
    a = R[:, 0]
    b = R[:, 1]
    S = np.column_stack((a, np.ones(len(a), int)))
    E = np.column_stack((b + 1, -np.ones(len(b), int)))
    e = np.vstack((S, E))
    i = np.argsort(e[:, 0])
    X = e[i, 0]
    D = e[i, 1]
    C = np.cumsum(D)
    L = X[1:] - X[:-1]
    return int(L[C[:-1] > 0].sum())

print(calc2("day_5/puzzle_input5.txt"))