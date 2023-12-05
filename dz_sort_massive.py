def get_min_max(data, get_min):
    if get_min:
       return min(data)
    return max(data)

print(get_min_max([1,2,3,2,1], False)) # 3