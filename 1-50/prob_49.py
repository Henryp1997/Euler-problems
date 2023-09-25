from prob_46 import prime_check

def permutations_4(n):
    perms = []
    for i in range(4):
        remaining_3 = [a for a in range(4) if a != i]
        for j in remaining_3:
            remaining_2 = [a for a in range(4) if a not in (i, j)]
            for k in remaining_2:
                remaining_1 = [a for a in range(4) if a not in (i, j, k)]
                for l in remaining_1:
                    
                    result1 = int(str(n)[i] + str(n)[j] + str(n)[k] + str(n)[l])
                    result2 = int(str(n)[i] + str(n)[j] + str(n)[l] + str(n)[k])
                    
                    for result in (result1, result2):
                        if result not in perms:
                            if len(str(result)) == 4:
                                perms.append(result)

    return perms, len(perms)

def check_val(n):
    perms = permutations_4(n)[0]

    if 1487 in perms:
        return False

    for perm in perms:
        for other_perm in perms:
            if other_perm > perm:
                if (i := 2*other_perm - perm) in perms:
                    vals = [perm, other_perm, i]
                    for val in vals:
                        if not prime_check(val):
                            return False

                    print(vals)    
                    
                    return True
            elif other_perm < perm:
                if (i := 2*perm - other_perm) in perms:
                    vals = [other_perm, perm, i]
                    for val in vals:
                        if not prime_check(val):
                            return False
                        
                    print(vals) 

                    return True

    return False

primes = []
for i in range(1001, 10_001, 2):
    if prime_check(i):
        primes.append(i)

for n in primes:
    if check_val(n) and n not in permutations_4(1847)[0]:
        break


