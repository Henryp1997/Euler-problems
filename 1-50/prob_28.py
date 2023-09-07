import math
N = 1001
result = 4 * sum([(4*(n**2) + n + 1) for n in range(1, math.floor(N/2) + 1)]) + 1

print(result)