import numpy as np
from pathlib import Path

def ranges(p: str) -> np.ndarray:
    L = Path(p).read_text().strip().split(',')
    return np.array([s.split('-') for s in L if s], int)

def calc(p: str) -> int:
    R = ranges(p)
    # turning problem into vectorized operations on one big int array
    ids = np.concatenate([np.arange(a, b + 1) for a, b in R])
    s = ids.astype(str)
    l = np.char.str_len(s)
    m = (l % 2 == 0)
    h = l // 2
    # numpy lists np.vectorize under "functional programming" in the docs, which is quite generous for a glorified for loop
    S = np.vectorize(lambda x, a, b: x[a:b])
    L = S(s, 0, h)
    R = S(s, h, l)
    b = m & (L == R)
    return ids[b].sum()

print(calc("day_2/puzzle_input2.txt"))