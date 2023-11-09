# import math
# import numpy as np
# from prob_64 import continued_frac

# def get_convergent(convergent_num, n):
#     cont_frac_coeffs = continued_frac(n)
#     a0 = int(0.5 * cont_frac_coeffs[-1])
#     period = len(cont_frac_coeffs)

#     if convergent_num > period:
#         num_full_lists = int(convergent_num / period)
#         for i in range(num_full_lists):
#             cont_frac_coeffs += cont_frac_coeffs[:period]
#         cont_frac_coeffs = [a0] + cont_frac_coeffs
#         cont_frac_coeffs = cont_frac_coeffs[:convergent_num]
#     else:
#         cont_frac_coeffs = [a0] + cont_frac_coeffs[:convergent_num - 1]
    
#     # calculate convergent fraction
#     denom = cont_frac_coeffs[-2]*cont_frac_coeffs[-1] + 1
#     x = cont_frac_coeffs[-1]
#     for i in range((length := int(len(cont_frac_coeffs)) - 3)):
#         y = denom 
#         denom = cont_frac_coeffs[length - i]*denom + x
#         x = y
        
#     nume = (cont_frac_coeffs[0] * denom) + x

#     return nume, denom
# # 37/14
# def long_division(nume, denom):
#     digits = []
#     used_numes = []
#     while True:
#         floor = int(nume / denom)
#         digits.append(floor)
#         nume = (nume - (floor * denom)) * 10

#         if int(nume / 10) in used_numes:
#             break
#         used_numes.append(int(nume / 10))
#     print(digits)

#     return

# # print(get_convergent(9, 7))
# long_division(45, 17)
import math
import numpy as np

def digital_expansion(N):
    sqrt = math.floor(math.sqrt(N))
    for i in range(1, 100):
        for j in range(10):
            check = str(sqrt) + str(j)
            if i == 1:
                check = str(sqrt) + "." + str(j)

            to_check = str(int("".join([i for i in str(check) if i != "."])) ** 2)

            if to_check[:len(str(N))] == str(N):
                if i == 1:
                    sqrt = str(sqrt) + "." + str(j - 1)
                else:
                    sqrt = str(sqrt) + str(j - 1)
                break
            else:
                if check[-1] == '9':
                    if i == 1:
                        sqrt = str(sqrt) + "." + str('9')
                    else:
                        sqrt = str(sqrt) + str('9')

    return sqrt


total = 0

for N in range(2, 3):

    if math.sqrt(N) % 1 == 0:
        continue

    sqrt = digital_expansion(N)
    total += sum([int(i) for i in sqrt if i != '.'])

print(total)

print(digital_expansion(17))