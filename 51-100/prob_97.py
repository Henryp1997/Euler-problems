import math, numpy as np

N = 28433
k = 0
while True:
    full_num = N*(2**k)
    if math.ceil(np.log10(full_num)) == 10:
        break
    k += 1

digits = [int(i) for i in str(full_num)][::-1]

while k < 7830457:
    k += 1
    digits = [i*2 for i in digits]
    for i, val in enumerate(digits):
        if i != 0:
            if digits[i - 1] >= 10:
                digits[i] += 1
    for i, val in enumerate(digits):
        digits[i] = digits[i] % 10

# account for the +1 in 28433*2^7830457 + 1
digits[0] = digits[0] + 1

print("".join([str(i) for i in digits[::-1]]))