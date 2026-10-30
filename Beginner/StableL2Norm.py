import math

def solve(x):
    if len(x) == 0:
        return 0.0

    m = 0
    for j in range(len(x)):
        if abs(x[j]) > m:
            m = abs(x[j])

    if m == 0:
        return 0.0

    total = 0
    for i in range(len(x)):
        total += (x[i] / m) ** 2

    return m * math.sqrt(total)

print(solve([3.0, 4.0]))
print(solve([3e200, 4e200]))