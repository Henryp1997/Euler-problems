current_palindrome = 0

for i in range(1000, 100, -1):
    for j in range(1000, 100, -1):
        if j*i < current_palindrome:
            break
        if (x := str(j*i)) == x[::-1]:
            if int(x) > current_palindrome:
                current_palindrome = int(x)

print(current_palindrome)