""" def massdriver(activate):
    if len(activate) < 2 :
        return -1
    dict_activate = {}
    for i in activate:
        dict_activate[i] = dict_activate.get(i, 0) + 1
        if i not in dict_activate:
            return dict_activate[i]
        dict_activate[i] += 1
    return -1 """
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

print(massdriver([1,2,3])) # false
print(massdriver([1,2,3])) # true
print(massdriver([1,3,2])) # true
print(massdriver([1,3,2,3])) # False
print(massdriver([1,1]))  # true
print(massdriver([1,2,3,1,2,3,4]))
print(massdriver(([1,2,3,4,3,4,2])))
print(massdriver(([1,2,3,4,5,6,7])))
print(massdriver(([1,2,3,4,5,6,7,5,7])))