import numpy as np

def solve(A, x):
    A = np.array(A)
    x = np.array(x)
    return A@x

print(solve([[0.0, 1.0, 0.0]], [5.0, 6.0, 7.0])
)