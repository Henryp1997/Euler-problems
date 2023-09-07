# need to check which numbers become palindromes after iterating
import sys

results = {}

lychrel_count = 0
for i in range(11, 10_000):
    palindrome = False
    count = 0
    path = []
    num = i
    lychrel = False
    while not palindrome:
        if count == 50:
            lychrel = True
            lychrel_count += 1
            break
        new_num = num + int(str(num)[::-1])
        path.append(new_num)
        if str(new_num)[::-1] == str(new_num):
            palindrome = True
        else:
            num = int(new_num)
        count += 1

    results[i] = (count, lychrel, path)

print(lychrel_count)