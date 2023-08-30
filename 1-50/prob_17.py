dic1 = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

dic2 = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

dic3 = {
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

def count(num):
    num = str(num)
    num = num if len(num) == 3 else f'0{num}' if len(num) == 2 else f'00{num}'
    x = ""
    hundred = False
    if num[0] != '0':
        x += f'{dic1[int(num[0])]}hundred'
        hundred = True

    if num[1] == '1':
        if hundred:
            x += 'and'
        x += f'{dic2[int(num[1:])]}'
        return x, len(x)

    if num[1] != '0':
        if hundred:
            x += 'and'
        x += f'{dic3[int(num[1])*10]}'

    if num[-1] == '0':
        return x, len(x)

    if hundred and num[1] == '0':
        x += 'and'
    x += f'{dic1[int(num[-1])]}'
    
    return x, len(x)

total = 11
for i in range(1,1000):
    x, length = count(i)
    total += length

print(total)