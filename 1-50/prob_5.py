n = 20
factor_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
while True:
    count = 0
    for factor in factor_list:
        if n % factor == 0:
            count += 1
    if count == 10:
        print(n)
        break
    n += 20