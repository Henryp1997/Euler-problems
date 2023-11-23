import math
import numpy as np
import time

def get_factors(n):
    factors = []
    for i in range(2, n):
        try:
            if i > int(n / factors[0]):
                break
        except:
            pass
        if n % i == 0:
            factors.append(i)
    return factors

n = 20
flag = True
while True:
    factors_n = get_factors(n)
    factors_n.append(n)
    n += 1
    factors_n_plus_1 = get_factors(n)
    factors_n_plus_1.append(n)
    
    x = len(factors_n) * len(factors_n_plus_1)
    if x > 500:
        print(n)
    
    if flag:
        num_factors = (len(factors_n) * len(factors_n_plus_1)) + 1
        # print(num_factors, factors_n, factors_n_plus_1)
        time.sleep(2)
        flag = False
        continue
    
    if not flag:
        flag = True

    


