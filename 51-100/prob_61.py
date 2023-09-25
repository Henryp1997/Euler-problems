import math
import sys

# triangle 45 to 141
tris = []
for i in range(45, 141):
    tris.append(int(0.5 * i * (i + 1)))
print(tris)
# square 32 to 101
squares = []
for i in range(32, 101):
    squares.append(int(i**2))
# print(squares)
# pentagonal 26 to 82
pents = []
for i in range(26, 83):
    pents.append(int(0.5 * i * (3*i - 1)))

# hexagonal 23 to 71
hexs = []
for i in range(23, 72):
    hexs.append(int(i * (2*i - 1)))

# heptagonal 21 to 64
hepts = []
for i in range(21, 65):
    hepts.append(int(0.5 * i * (5*i - 3)))

# octagonal 19 to 59
octs = []
for i in range(19, 60):
    octs.append(int(i * (3*i - 2)))

####################################################################################
def int_check3(n):
    if math.sqrt(1 + 8*int(n)) % 2 == 1:
        return True
    return False

def int_check4(n):
    if math.sqrt(int(n)) % 1 == 0:
        return True
    return False

def int_check5(n):
    if math.sqrt(1 + 24*int(n)) % 6 == 5:
        return True
    return False

def int_check6(n):
    if math.sqrt(1 + 8*int(n)) % 4 == 3:
        return True
    return False

def int_check7(n):
    if math.sqrt(9 + 40*int(n)) % 10 == 7:
        return True
    return False

def int_check8(n):
    if math.sqrt(1 + 3*int(n)) % 3 == 2:
        return True
    return False

funcs = [int_check4, int_check5, int_check6, int_check7, int_check8]
def cycle_number(n):
    if str(n)[-2] == '0':
        return []  
    vals_to_check = []
    for i in range(10):
        for j in range(10):
            cycled = str(n)[-2] + str(n)[-1] + str(i) + str(j)
            vals_to_check.append(int(cycled))
    return vals_to_check

def which_list(n, already_done):
    if n in squares and 4 not in already_done:
        return 4
    if n in pents and 5 not in already_done:
        return 5
    if n in hexs and 6 not in already_done:
        return 6
    if n in hepts and 7 not in already_done:
        return 7
    if n in octs and 8 not in already_done:
        return 8
    return 0

# for num1 in tris:
#     already_done = []
#     vals_to_check = cycle_number(num1)
#     for num2 in vals_to_check:
#         if (x := which_list(num2, already_done)) != 0:
#             already_done.append(x)
#             vals_to_check = cycle_number(num2)
#             for num3 in vals_to_check:
#                 if (x := which_list(num3, already_done)) != 0:
#                     already_done.append(x)
#                     vals_to_check = cycle_number(num3)
#                     for num4 in vals_to_check:
#                         if (x := which_list(num4, already_done)) != 0:
#                             already_done.append(x)
#                             vals_to_check = cycle_number(num4)
#                             for num5 in vals_to_check:
#                                 if (x := which_list(num5, already_done)) != 0:
#                                     already_done.append(x)
#                                     vals_to_check = cycle_number(num5)
#                                     for num6 in vals_to_check:
#                                         if (x := which_list(num6, already_done)) != 0:
#                                             already_done.append(x)
#                                             vals_to_check = cycle_number(num6)
#                                             print(num1, num2, num3, num4, num5, num6, already_done)
#                                             break

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(10):
            for d in range(1, 10):
                for e in range(10):
                    for f in range(1, 10):
                        for g in range(10):
                            for h in range(1, 10):
                                for i in range(10):
                                    for j in range(1, 10):
                                        for k in range(10):
                                            num = f'{a}{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{a}{a}'
                                            already_done = []
                                            if (x := which_list(int(f'{a}{a}{b}{c}'), already_done)) != 0:
                                                already_done.append(x)
                                                if (x := which_list(int(f'{b}{c}{d}{e}'), already_done)) != 0:
                                                    already_done.append(x)
                                                    if (x := which_list(int(f'{d}{e}{f}{g}'), already_done)) != 0:
                                                        already_done.append(x)
                                                        if (x := which_list(int(f'{f}{g}{h}{i}'), already_done)) != 0:
                                                            already_done.append(x)
                                                            if (x := which_list(int(f'{h}{i}{j}{k}'), already_done)) != 0:
                                                                already_done.append(x)
                                                                if (x := which_list(int(f'{j}{k}{a}{a}'), already_done)) != 0:
                                                                    already_done.append(x)
                                                                    print(num)



