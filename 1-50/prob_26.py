import numpy as np

def long_division(divisor):
    decimal_digits = []
    numerators_used = [1]
    current_numerator = 10
    count = 0
    while True:
        if current_numerator < divisor:
            current_numerator *= 10
        else:
            decimal_digits.append(int(current_numerator / divisor))
            current_numerator = current_numerator % divisor

        if current_numerator == 0:
            break

        break_loop = False
        for num in numerators_used:
            if current_numerator / num == 1:
                break_loop = True
                break

        if break_loop:
            break

        numerators_used.append(current_numerator)
        count += 1

    return decimal_digits

print(long_division(10))

results = [0]
for i in range(1,1000):
    results.append(len(long_division(i)))
    
print(results.index(max(results)))
