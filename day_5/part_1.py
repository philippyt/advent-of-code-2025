import numpy as np
from pathlib import Path

def ranges(p: str) -> tuple[np.ndarray, np.ndarray]:
    L = Path(p).read_text().splitlines()
    i = L.index("")
    R = np.array([s.split("-") for s in L[:i]], int)
    A = np.array(L[i + 1:], int)
    return R, A

def calc(p: str) -> int:
    R, A = ranges(p)
    l = R[:, 0][:, None]
    h = R[:, 1][:, None]
    x = A[None, :]
    F = ((l <= x) & (x <= h)).any(0)
    return int(F.sum())

print(calc("day_5/puzzle_input5.txt"))