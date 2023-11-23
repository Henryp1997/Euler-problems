#%%
from utils import prime_check

def truncate_prime(n):
    left = []
    right = []
    for i in range(len(str(n))):
        truncated_l = int(str(n)[i:])
        truncated_r = int(str(n)[:i+1])
        left.append(truncated_l)
        right.append(truncated_r)
    return list(set(left[1:] + right[:-1]))

def check_truncatable(n):
    truncated = truncate_prime(n)
    count = 0
    for i in truncated:
        if i in primes_checked:
            count += 1
            continue
        if prime_check(i):
            primes_checked.append(i)
            count += 1
    if len(truncated) == count:
        return True
    return False

def same_first_or_last_two_digits(n):
    n = str(n)
    if str(n)[0] == str(n)[1] or str(n)[-1] == str(n)[-2]:
        return True
    return False

skip_dict = {
    '1': 2,
    '2': 1,
    '3': 4,
    '4': 3,
    '5': 2,
    '6': 1,
    '7': 6,
    '8': 5,
    '9': 4,
    '0': 3
}

truncatable = []
primes_checked = []
n = 11
while True:
    wrong_digits = any(val in str(n) for val in ['4', '6', '8', '0'])
    two_not_at_start = '2' in str(n)[1:]
    five_not_at_start = '5' in str(n)[1:]
    starts_or_ends_1 = str(n)[0] == '1' or str(n)[-1] == '1'
    starts_or_ends_9 = str(n)[0] == '9' or str(n)[-1] == '9'
    divisible_by_ones = same_first_or_last_two_digits(n)
    prime = prime_check(n)
    if wrong_digits or two_not_at_start or five_not_at_start or starts_or_ends_1 or starts_or_ends_9 or divisible_by_ones or not prime:
        n += skip_dict[str(n)[-1]]
        continue

    if check_truncatable(n):
        truncatable.append(n)
        print(len(truncatable), n)

    if len(truncatable) == 11:
        break

    n += skip_dict[str(n)[-1]]

print(sum(truncatable))
# %%
