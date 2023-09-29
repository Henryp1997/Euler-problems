#%%
import math

# D = 7
# x, y, a, b = 5, 2, 5, 2

# while True:
#     x_new = x*a + D*y*b
#     y_new = x*b + y*a
      
#     result = (x_new**2) - (D * (y_new**2))
    
#     if x_new**2 % result == 0 and y_new**2 % result == 0:
#         print(int(x_new**2/result), int(y_new**2/result), int(result/result))
#         break

#     x, y = x_new, y_new
#%%
for D in range(2, 1001):
    if math.sqrt(D) % 1 == 0:
        continue
    x = 2
    while True:
        if (y := math.sqrt((x**2 - 1) / D)) % 1 == 0:
            print(x, D, int(y))
            break
        x += 1
#%%