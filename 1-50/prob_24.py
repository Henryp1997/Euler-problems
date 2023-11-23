import math
import itertools

result = []
available_digits = list(range(10))
current_amount = 1_000_000
current_amounts = []
for i in range(9, 0, -1):
    max_divisor = math.floor(current_amount / math.factorial(i))
    current_amount -= (max_divisor * math.factorial(i))
    if current_amount == 0:
        num_final_perms = current_amounts[-1]
        result += list(itertools.permutations(available_digits))[num_final_perms - 1]
        break
    current_amounts.append(current_amount)
    permutation_val = available_digits[max_divisor]
    result.append(permutation_val)
    available_digits = [i for i in available_digits if i != permutation_val]

print("".join([str(i) for i in result]))
