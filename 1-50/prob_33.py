# dont need to check xs or ys that have a zero in them
# because integers 0X don't make sense, and also because if the zero is in the second position
# for the multiples of 10, this would become a trivial result

vals_to_check = [i for i in range(11, 100) if i % 10 != 0]

def check_if_curious(x, y):
    actual_val = x / y
    for i in str(x):
        if i in str(y):
            if str(x)[0] == str(x)[1]:
                a = int(str(x)[0])
            else:
                a = int("".join([str(j) for j in str(x) if j != i]))
            if str(y)[0] == str(y)[1]:
                b = int(str(y)[0])
            else:
                b = int("".join([str(j) for j in str(y) if j != i]))
            
            # this checks that the new fraction is equivalent in value
            if (val := a / b) == actual_val:
                return True
    return False

results = []
for numerator in vals_to_check:
    for denominator in vals_to_check:
        if numerator < denominator:
            if check_if_curious(numerator, denominator):
                if [denominator, numerator] not in results:
                    results.append([numerator, denominator])

numerator_prod = 1
denominator_prod = 1
for result in results:
    numerator_prod *= result[0]
    denominator_prod *= result[1]

print(results)
print(int(denominator_prod / numerator_prod))