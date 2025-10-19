def white_walkers(village):
    cu_sum_prefix = [0] * (len(village) + 1)
    list_digits = []
    for i, char in enumerate(village):
        cu_sum_prefix[i+1] = cu_sum_prefix[i] + (char == '=')
        if char.isdigit():
            list_digits.append((i, int(char)))
    if len(list_digits) < 2:
        return False
    correct_pairs = []
    for i in range(len(list_digits) - 1):
        index_1, number_1 = list_digits[i]
        index_2, number_2 = list_digits[i+1]
        count = cu_sum_prefix[index_2] - cu_sum_prefix[index_1 + 1]
        if number_1 + number_2 == 10:
            correct_pairs.append(count == 3)
    return bool(correct_pairs) and all(correct_pairs)