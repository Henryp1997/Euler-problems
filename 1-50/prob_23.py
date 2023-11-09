def get_divisors(n):
    divisors = []
    max_ = n
    for i in range(1, n):
        if len(divisors) > 2:
            max_ = n / divisors[1]
        if i > max_:
            return divisors
        if n % i == 0:
            divisors.append(i)
            
def check_abundant(n):
    try:
        if sum(get_divisors(n)) > n:
            return True
    except:
        return False
    return False

abundant = []
total = 0
count = 0
for i, val in enumerate(range(28124)):
    with open('test.txt', 'w') as f:
        f.write(f'{i}')
    try:
        if check_abundant(val):
            abundant.append(val)
            count += 1
        yes = True
        for k in abundant:
            if val - k in abundant:
                yes = False
                break
        if yes:
            total += val
    except:
        pass

print(total)