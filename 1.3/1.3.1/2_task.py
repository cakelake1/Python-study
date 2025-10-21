def digital_rain(col):
    zero = 0
    one = 0
    res = ''
    start = 0
    end = 0
    max_length = 0
    diff_index = {0:-1}
    for i,n in enumerate(col):
        if n =='0':
            zero += 1
        else:
            one += 1
        diff = one - zero
        if diff in diff_index:
            start_index = diff_index[diff] + 1
            current_lenght = i - start_index + 1
            if current_lenght > max_length:
                max_length = current_lenght
                start = start_index
                end = i + 1
            elif current_lenght == max_length and current_lenght > 0:
                if start_index > start:
                    start = start_index
                    end = i + 1
        else:
            diff_index[diff] = i
    if max_length == 0 :
        return ''
    for i in range(start,end):
        res += col[i]
    return res
