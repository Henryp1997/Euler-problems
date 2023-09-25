import sys

with open('0054_poker.txt', 'r') as f:
    lines = [i.strip("\n") for i in f.readlines()]

dic = {'T': '10', 'J':'11', 'Q':'12', 'K':'13', 'A':'14'}

def two_of_a_kind(vals):
    for val in vals:
        if vals.count(val) == 2:
            return 2
    return 0

def two_pairs(vals):
    for val in vals:
        if vals.count(val) == 2:
            for other_val in [i for i in vals if i != val]:
                if vals.count(other_val) == 2:
                    return 3
    return 0

def three_of_a_kind(vals):
    for val in vals:
        if vals.count(val) == 3:
            return 4
    return 0

def full_house(vals):
    if three_of_a_kind(vals) == 4 and two_of_a_kind(vals) == 2:
        return 7
    return 0

def four_of_a_kind(vals):
    for val in vals:
        if vals.count(val) == 4:
            return 8
    return 0

def straight(vals):
    vals.sort()
    count = 0
    for i, val in enumerate(vals):
        if i == 0:
            continue
        if val == vals[i - 1] + 1:
            count += 1    
    if count == 4:
        return 5
    return 0

def flush(vals, suits):
    if all(suit == suits[0] for suit in suits):
        if vals == [10, 11, 12, 13, 14] or vals == [14, 13, 12, 11, 10]:
            return 10 # royal flush
        if straight(vals) == 5:
            return 9 # straight flush
        return 6 # flush
    return 0 # no flush

def check_hand_rank(hand, suits):
    if (x := four_of_a_kind(hand)) != 0:
        return x
    if (x := full_house(hand)) != 0:
        return x
    if (x := flush(hand, suits)) != 0:
        return x
    if (x := straight(hand)) != 0:
        return x
    if (x := three_of_a_kind(hand)) != 0:
        return x
    if (x := two_pairs(hand)) != 0:
        return x
    if (x := two_of_a_kind(hand)) != 0:
        return x
    return 1

def create_lists_with_results(lines, player):
    all_hands = []
    for line in lines:
        i = line.split(" ")[:5]
        if player == 2:
            i = line.split(" ")[5:]
        vals = []
        suits = []
        for j in i:
            val = j[0]
            if val in list(dic.keys()):
                val = dic[val]
            vals.append(val)
            suits.append(j[1])
        vals = [int(i) for i in vals]
        rank = check_hand_rank(vals, suits)
        all_hands.append((vals, suits, rank))
    return all_hands

p1_hands, p2_hands = create_lists_with_results(lines, 1), create_lists_with_results(lines, 2)

p1_count, p2_count = 0, 0
for i in range(len(p1_hands)):
    p1, p2 = p1_hands[i], p2_hands[i]

    # previous prints have revealed:
    # p1 has no 10, 9, 8, 7, 5
    # p2 has no 10, 9, 8, 5

    if p1[2] == p2[2]:
        # previous prints revealed that this is only the case if the 
        # result is nothing (1) or one pair (2). Therefore, only check these two cases
        if p1[2] == 1:
            if max(p1[0]) > max(p2[0]):
                p1_count += 1
        else:
            p1_double = [i for i in p1[0] if p1[0].count(i) == 2]
            p2_double = [i for i in p2[0] if p2[0].count(i) == 2]
            if p1_double[0] > p2_double[0]:
                p1_count += 1
            elif p1_double == p2_double:
                new_p1 = [i for i in p1[0] if i not in p1_double]
                new_p2 = [i for i in p2[0] if i not in p2_double]
                if max(new_p1) > max(new_p2):
                    p1_count += 1
                    # print(p1, p2)

    # simple check if they don't have matching hands
    elif p1[2] > p2[2]:
        p1_count += 1

print(p1_count)
