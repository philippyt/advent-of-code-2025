import numpy as np
from pathlib import Path

def rotations(p: str) -> tuple[np.ndarray, np.ndarray]:
    L = Path(p).read_text().splitlines()
    d = np.array([1 if r[0] == "R" else -1 for r in L], int)
    a = np.array([int(r[1:]) for r in L], int)
    return d, a

def calc2(p: str) -> int:
    d, a = rotations(p)
    m = d * a
    x = (50 + np.cumsum(m)) % 100
    p = np.empty_like(a)
    p[0] = 50
    p[1:] = x[:-1]
    z = (p == 0)
    jr = (100 - p) % 100
    jr[z] = 100
    jl = np.where(z, 100, p)
    j = np.where(d > 0, jr, jl)
    # if start at 0 then floor(a / 100), else if a < j, else 1 + floor((a - j) / 100)
    v = np.where(z, a // 100, np.where(a < j, 0, 1 + (a - j) // 100))
    return v.sum()

print(calc2("day_1/puzzle_input.txt"))