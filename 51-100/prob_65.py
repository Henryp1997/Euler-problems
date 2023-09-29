coeffs = [2]
k = 1
for i in range(99):
    if i % 3 == 1:
        coeffs.append(2*k)
        k += 1
        continue
    coeffs.append(1)

b = coeffs[-2]*coeffs[-1] + 1
x = coeffs[-1]
for i in range((length := int(len(coeffs)) - 3)):
    y = b
    b = coeffs[length - i]*b + x
    x = y
    
numerator = (coeffs[0] * b) + x

print(sum([int(i) for i in str(numerator)]))
    