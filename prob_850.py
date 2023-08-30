import numpy as np
import math
import matplotlib.pyplot as plt
from pprint import pprint
import requests
import os
import urllib.parse

def power(x, exp):
    appid = 'Y82H2H-AAHL3G3L7W'

    query = urllib.parse.quote_plus(f'{x}^{exp}')
    query_url = f"http://api.wolframalpha.com/v2/query?" \
                f"appid={appid}" \
                f"&input={query}" \
                f"&format=plaintext" \
                f"&output=json"

    response = requests.get(query_url).json()

    result = int(response['queryresult']['pods'][1]['subpods'][0]['plaintext'])
    
    return result

# N = 10

# S = 0
# for k in range(1, N + 1):
#     if k % 2 == 0:
#         continue
#     for n in range(1, N + 1):
#         f = [np.power(i, k)/n % 1 for i in range(1, n + 1)]
#         S += sum(f)

# print(S)

##########################
# N = 1234
# k = 7
# # for k in range(1, n + 1):
# for n in range(1, N + 1):
#     f = [(np.power(i, k)/n) % 1 for i in range(1, n + 1)]

#     if n == 1234 or n == 10:
#         print(sum(f))

#     plt.plot(n, sum(f), 'kx')

# plt.plot((x := np.array(range(2, N))), 0.5*(x - 1), 'b--')
# plt.plot((x := np.array(range(2, N))), 0.25*x, 'r--')
# # plt.xticks(np.arange(2,N+1,1))
# plt.grid()
# plt.show()

##########################
n = 100
k = 1
f = 0
for i in range(1, n + 1):
    print(i)
    # p = power(i, k)
    p = np.power(i, k)
    p_over_n = p / n
    f += p_over_n % 1

print(k, f)

##########################
