import numpy as np
from pathlib import Path

ASCII = 48
BATTERIES = 12

def ranges(p: str) -> np.ndarray:
    L = Path(p).read_bytes().splitlines()
    return np.array([[s - ASCII for s in l] for l in L], int)

def calc2(p: str) -> int:
    R = ranges(p)
    _, m = R.shape
    B = BATTERIES
    T = 0
    # numpy's contribution here is mostly psychological
    for r in R:
        f = m - B
        s = np.zeros(m, int)
        t = 0
        for d in r:
            while f and t and d > s[t - 1]:
                t -= 1
                f -= 1
            s[t] = d
            t += 1
        b = s[:B]
        T += b.dot(10 ** np.arange(B - 1, -1, -1))
    return T

print(calc2("day_3/puzzle_input3.txt"))