def BigMinus(s1, s2): 
    check_lengh = len(s1) < len(s2) or (len(s1) == len(s2) and s1 < s2)
    a, b = ((s1, s2), (s2, s1))[check_lengh]
    b = b.zfill(len(a))
    list = []
    debt = 0
    for i in range(len(a)-1, -1, -1):
        digit = int(a[i]) - int(b[i]) - debt
        debt = digit < 0
        digit += debt * 10
        list.append(str(digit))
    result = ''.join(reversed(list))
    result = result.lstrip('0')
    return result or '0'