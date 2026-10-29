import numpy as np
import math

def solve(x):
    norm = 0

    for i in range(len(x)):
        norm += x[i] ** 2

    L2norm = math.sqrt(norm)

import numpy as np
import math

def solve(x):
    norm = 0

    for i in range(len(x)):
        norm += x[i] ** 2

    L2norm = math.sqrt(norm)
    
    if L2norm == 0:
        raise ValueError("Cannot normalize a zero vector")

    result = []
    for j in range(len(x)):
        result.append(x[j] / L2norm)

    return np.array(result)
    result = []
    for j in range(len(x)):
        result.append(x[j] / L2norm)

    return np.array(result)

print(solve([3.0, 4.0]))
print(solve([0.0, 0.0]))