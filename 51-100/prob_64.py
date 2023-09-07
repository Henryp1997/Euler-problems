import math

def conjugate(expression):
    if '-' in expression:
        result = f'{expression.split("-")[0]} + {expression.split("-")[1]}'
    else:
        result = f'{expression.split("+")[0]} - {expression.split("+")[1]}'
    return result

def simplify_denominator(multiplier, denom):
    if multiplier == 1:
        return denom
    if (denom / multiplier) % 1 == 0:
        return int(denom / multiplier)

def check_if_odd_repeating(n, a0):
    frac = (1, f'x - {a0}')
    coeffs = []
    fracs = [frac]
    while True:
        multiplier = frac[0]
        conj = conjugate(frac[1])
        denominator = n - (int(conj.split(" ")[-1]))**2
        
        # can the fraction be reduced
        if denominator / multiplier % 1 == 0:
            denominator = int(denominator / multiplier)

        if (y := int(conj.split(" ")[-1])) < denominator:
            coeff = 1
            new_numerator = f"x - {abs(y-denominator)}"
        elif y > denominator:
            coeff = y
            new_numerator = f"x - {y}"
        elif y == denominator:
            coeff = 2
            new_numerator = f"x - {y}"
        
        frac = (denominator, new_numerator)

        if frac in fracs:
            coeffs.append(2 * a0)
            if len(coeffs) % 2 == 1:
                odd = True
            else:
                odd = False
            break

        coeffs.append(coeff)
        fracs.append(frac)

    if n == 72:
        print(coeffs)

    return odd

total_odd = 0
odd_vals = []
squares = [int(i**2) for i in range(101)]
for n in range(2, 10_001):
    if n in squares:
        continue
    closest_val = [i for i in squares if i < n][-1]
    a0 = squares.index(closest_val)
    odd = check_if_odd_repeating(n, a0)
    if odd:
        odd_vals.append(n)
        total_odd += 1

print(odd_vals)
print(total_odd)
    