import math
import sys

# triangle 45 to 141
tris = []
for i in range(45, 141):
    tris.append(int(0.5 * i * (i + 1)))

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

def which_list(n):
    if n in squares and 4:
        return 4
    if n in pents and 5:
        return 5
    if n in hexs and 6:
        return 6
    if n in hepts and 7:
        return 7
    if n in octs and 8:
        return 8
    return 0

results = []

def recursion(num, count=0):
    if count == 0:
        global path
        path = [num]
    if count == 6:
        if str(path[-1])[-2:] == str(path[0])[:2]:
            print(path)
        path = []
        return path
    vals_to_check = cycle_number(num)
    for x in vals_to_check:
        if which_list(x) != 0 and  str(path[-1])[-2:] == str(path[0])[:2]:
            count += 1
            path.append(x)
            recursion(x, count)
    return path

for num in tris:
    # vals_to_check = cycle_number(num1)
    # for num2 in vals_to_check:
    #     if (x := which_list(num2)) != 0:
    #         vals_to_check = cycle_number(num2)
    #         for num3 in vals_to_check:
    #             if (x := which_list(num3)) != 0:
    #                 vals_to_check = cycle_number(num3)
    #                 for num4 in vals_to_check:
    #                     if (x := which_list(num4)) != 0:
    #                         vals_to_check = cycle_number(num4)
    #                         for num5 in vals_to_check:
    #                             if (x := which_list(num5)) != 0:
    #                                 vals_to_check = cycle_number(num5)
    #                                 for num6 in vals_to_check:
    #                                     if (x := which_list(num6)) != 0:
    #                                         vals_to_check = cycle_number(num6)
    #                                         if str(num6)[-2:] == str(num1)[:2]:
    #                                             results.append((num1, num2, num3, num4, num5, num6))
    try:
        recursion(num)
    except:
        pass

for result in results:
    nums = []
    for i in result:
        if (x := which_list(i)) not in nums:
            nums.append(x)
    if len(nums) == 6:
        print(result)
        print(sum(result))
