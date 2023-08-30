results = []

# only odd numbers since all even binary numbers end in zero
# and we're ignoring leading zeroes, so no palindrome is possible
for i in range(1, 1_000_000, 2):
    binary = str(bin(i)).split("0b")[1]
    decimal = str(i)
    if (binary[::-1] == binary) and (decimal[::-1] == decimal):
        results.append(i)
    
print(sum(results))