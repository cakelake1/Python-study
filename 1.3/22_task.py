def SherlockValidString(s):
    for i in s:
        if not (('a' <= i <= 'z') or ('A' <= i <= 'Z')):
            return False
    lower_s = s.lower()
    dict_chars = {}
    for i in lower_s:
        dict_chars[i] = dict_chars.get(i, 0) + 1
    chars_list = list(dict_chars.values())
    if all(j == chars_list[0] for j in chars_list):
        return True # все значения одинаковые
    min_chars = min(chars_list)
    max_chars = max(chars_list)
    min_count = sum(1 for j in chars_list if j == min_chars )
    max_count = sum(1 for j in chars_list if j == max_chars)
    if (max_chars - min_chars ==1) and (max_count ==1):
        return True
    if (min_chars == 1) and (min_count == 1):
        return True
    return False