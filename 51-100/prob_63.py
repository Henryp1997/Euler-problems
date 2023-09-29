import math
import numpy as np

n = 16807

n = 2
count = 0
while True:
    if str(n)[0] == '1' and all(i == '0' for i in str(n)[1:]):
        pass
    elif (x := (10 ** (np.log10(n) / math.ceil(np.log10(n))))) % 1 < 0.00000000000001:
        count += 1
        print(n, x)
    n += 1
    # print(count)