results = []

def check_is_candidate(n):
    for digit in str(n):
        if str(n).count(digit) != 1:
            return False
    return True

for i in range(9182, 9877):
    if check_is_candidate(i):
        x = int(i * 2)
        if check_is_candidate(x):
            if any(val in str(x) for val in str(i)):
                continue
            if '0' not in str(x):
                results.append((i, x, f'{i}{x}'))

print(max(results, key=lambda x: x[2]))
