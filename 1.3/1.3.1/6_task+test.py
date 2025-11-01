""" def TRC_sort(trc):
    if not trc:
        return trc
    Lo = 0
    Mid = 0
    Hi = len(trc) - 1
    if Mid > Hi:
        return trc
    while Mid <= Hi:
        if trc[Mid] == 0:
            trc[Mid], trc[Lo] = trc[Lo], trc[Mid]
            Lo += 1
            Mid += 1
        elif trc[Mid] == 1:
            Mid += 1
        else: 
            trc[Mid], trc[Hi] = trc[Hi], trc[Mid]
            Hi -= 1
    return trc and TRC_sort(trc) """

def sort_1(arr, Lo, Mid, Hi):
    if Mid > Hi:
        return
    if arr[Mid] == 0:
        arr[Mid], arr[Lo] = arr[Lo], arr[Mid]
        Lo += 1
        Mid += 1
    elif arr[Mid] == 1:
        Mid += 1
    elif arr[Mid] == 2 :   
        arr[Mid], arr[Hi] = arr[Hi], arr[Mid]
        Hi -= 1
    sort_1(arr, Lo, Mid, Hi)
def TRC_sort(trc):
    if not trc:
        return trc
    result = trc.copy()
    sort_1(result, 0, 0, len(result) - 1)
    return result   
""" def TRC_sort(trc):
    if Hi is None:
        hi = len(trc) - 1
    Lo = 0
    Mid = 0
    Hi = len(trc) - 1
    if Mid > Hi:
        return trc
    
    if trc[Mid] == 0:
        trc[lo], trc[Mid] = trc[Mid], trc[lo]
        return TRC_sort(trc, lo + 1, Mid + 1, hi)
    elif trc[Mid] == 1:
        return TRC_sort(trc, lo, Mid + 1, hi)
    else:  # trc[Mid] == 2
        trc[Mid], trc[hi] = trc[hi], trc[Mid]
        return TRC_sort(trc, lo, Mid, hi - 1)    """
    
print(TRC_sort([0,2,1]))
print(TRC_sort([0,1,2,1,0,2]))
print(TRC_sort([]))
