import numpy as np
from pathlib import Path

def ranges(p: str) -> np.ndarray:
    L = Path(p).read_text().strip().split(',')
    return np.array([s.split('-') for s in L if s], int)

def calc2(p: str) -> int:
    R = ranges(p)
    ids = np.concatenate([np.arange(a, b + 1) for a, b in R])
    s = ids.astype(str)
    # festive little trick where I doubled the string and consider it pattern detection, ignore O(nk^2) runtime
    S = np.vectorize(lambda x: len(x) > 1 and (len(set(x)) == 1 or x in (x + x)[1: - 1]))
    b = S(s)
    return ids[b].sum()

print(calc2("day_2/puzzle_input2.txt"))