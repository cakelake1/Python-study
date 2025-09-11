def white_walkers(village):
    list_digits = [(i, int(char)) for i, char in enumerate(village) if char.isdigit()]
    if len(list_digits) < 2:
        return False
    correct_pairs = []
    for i in range(len(list_digits) - 1):
        index_1, number_1 = list_digits[i]
        index_2, number_2 = list_digits[i+1]
        if number_1 + number_2 != 10:
            continue
        between = village[index_1 + 1:index_2].count('=')
        correct_pairs.append(between == 3)
    return bool(correct_pairs) and all(correct_pairs)