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