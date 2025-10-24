def EEC_help(arr1, arr2):
    if len(arr1) != len(arr2) :
        return False
    dict_arr1, dict_arr2 = {}, {}
    for i in range(len(arr1)):
        dict_arr1[arr1[i]] = 1 + dict_arr1.get(arr1[i], 0)
        dict_arr2[arr2[i]] = 1 + dict_arr2.get(arr2[i], 0)
    for j in dict_arr1:
        if dict_arr1[j] != dict_arr2.get(j,0):
            return False
    return True