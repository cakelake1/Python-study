def massdriver(activate):
    if len(activate) < 2 :
        return -1
    dict_activate = {}
    result = -1
    for i, j in enumerate(activate):
        if j in dict_activate:
            if result == -1 or dict_activate[j] < result:
                result = dict_activate[j]
        else:
            dict_activate[j] = i
    return result