import math

def continued_frac(N):
    a0 = math.floor(math.sqrt(N))
    # numerator is just the number after sqrt(N), e.g., numerator=4 in this expression: sqrt(N) + 4 
    nume = a0
    denom = N - a0**2
    a = []
    while True:
        a1 = math.floor((a0 + nume) / denom)
        a.append(a1)
        if a1 == 2 * a0:
            break
        nume = a1*denom - nume # conjugated
        if ((N - nume**2) / denom) % 1 == 0:
            denom = int((N - nume**2) / denom)

    return a

if __name__ == "__main__":
    count = 0
    for N in range(2, 10_001):
        if math.sqrt(N) % 1 == 0:
            continue
        if len(continued_frac(N)) % 2 == 1:
            count += 1

    print(count)


# # OLD below
# #%%

# import math

# def conjugate(expression):
#     if '-' in expression:
#         result = f'{expression.split("-")[0]} + {expression.split("-")[1]}'
#     else:
#         result = f'{expression.split("+")[0]} - {expression.split("+")[1]}'
#     return result

# def simplify_denominator(multiplier, denom):
#     if multiplier == 1:
#         return denom
#     if (denom / multiplier) % 1 == 0:
#         return int(denom / multiplier)

# def check_if_odd_repeating(n, a0):
#     frac = (1, f'x - {a0}')
#     coeffs = []
#     fracs = [frac]
#     while True:
#         multiplier = frac[0]
#         conj = conjugate(frac[1])
#         denominator = n - (int(conj.split(" ")[-1]))**2
        
#         # can the fraction be reduced
#         if denominator / multiplier % 1 == 0:
#             denominator = int(denominator / multiplier)

#         if (y := int(conj.split(" ")[-1])) < denominator:
#             coeff = 1
#             new_numerator = f"x - {abs(y-denominator)}"
#         elif y > denominator:
#             coeff = y
#             new_numerator = f"x - {y}"
#         elif y == denominator:
#             coeff = 2
#             new_numerator = f"x - {y}"
        
#         frac = (denominator, new_numerator)

#         if frac in fracs:
#             coeffs.append(2 * a0)
#             if len(coeffs) % 2 == 1:
#                 odd = True
#             else:
#                 odd = False
#             break

#         coeffs.append(coeff)
#         fracs.append(frac)

#     if n == 72:
#         print(coeffs)

#     return odd

# total_odd = 0
# odd_vals = []
# squares = [int(i**2) for i in range(101)]
# for n in range(2, 10_001):
#     if n in squares:
#         continue
#     closest_val = [i for i in squares if i < n][-1]
#     a0 = squares.index(closest_val)
#     odd = check_if_odd_repeating(n, a0)
#     if odd:
#         odd_vals.append(n)
#         total_odd += 1

# print(odd_vals)
# print(total_odd)

# #%%
# import math

# def generate_coefficients(n):
#     a0 = math.floor(math.sqrt(n))
#     vals = [math.sqrt(n)]
#     a = [a0]
#     i = 0
#     while True:
#         i += 1
#         next_val = 1 / (vals[i - 1] - a[i - 1])
#         next_a = math.floor(next_val)
#         vals.append(next_val)
#         a.append(next_a)
#         if next_a == 2 * a0:
#             break

#     return a

# odd_count = 0
# for N in range(2, 10_001):
#     if math.sqrt(N) % 1 == 0:
#         continue
#     a = generate_coefficients(N)
#     if len(a[1:]) % 2 == 1:
#         odd_count += 1

# print(odd_count)

# print(generate_coefficients(976))
