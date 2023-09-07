from fractions import Fraction

a = [1,2,1]
n = len(a)

d = []
for i in range(n):
    if i == 0:
        d.append(1/a[0])
        continue
    d.append(1/(d[i-1] + (1/a[n-i])))
d[-1] += 2

num_digits = len(str(d[-1]).split(".")[1])

numerator = int(d[-1] * 10**num_digits)
denominator = 10**num_digits

frac = Fraction(numerator, denominator).limit_denominator()
print(frac)