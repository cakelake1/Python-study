def Football(F,N):
    return check_swap(F) or check_reverse(F)

def check_sorted(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True
def check_swap(array):
    if check_sorted(array):
        return True
    number_1 = -1
    number_2 = -1
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            number_1 = i
            break
    if number_1 == -1:
        return True
    for i in range(number_1 + 1,len(array)):
        if array[i] < array[number_1]:
            number_2 = i
    if number_2 != -1:
        temp_array = array.copy()
        temp_array[number_1], temp_array[number_2] = temp_array[number_2], temp_array[number_1]
        return check_sorted(temp_array)
    return False
def check_reverse(array):
    if check_sorted(array):
        return True
    start_number = -1
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            start_number = i
            break
    if start_number == -1:
        return True
    end_number = start_number
    for i in range(start_number + 1, len(array)):
        if i < len(array) - 1 and array[i] < array[i+1]:
            end_number = i
            break
        end_number = i
    temp_array2 = array.copy()
    temp_array2[start_number:end_number+1] = temp_array2[start_number:end_number+1][::-1]
    return check_sorted(temp_array2)