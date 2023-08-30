def get_divisors(n):
    yes = []
    for i in range(1, n):
        if n % i == 0:
            yes.append(i)
    return yes

def d(n):
    divisors = get_divisors(n)
    sum_ = sum(divisors)
    if (k := sum(get_divisors(sum_))) == n:
        if k == sum_:
            return False
        return sum_
    return False

if __name__ == "__main__":
    amicable = []
    for i in range(1, 10000):
        if i in amicable:
            continue
        if not (j := d(i)):
            pass
        else:
            amicable.append(i)
            amicable.append(j)

    amicable = list(dict.fromkeys(amicable))

    print(sum(amicable))
