def MadMax(N, Tele):
    sorted_array = sorted(Tele)
    center = (N - 1) // 2
    left_part_sorted = sorted_array[:center]
    right_part_sorted = sorted_array[center:-1]
    right_part_sorted.reverse()
    mid_max_index = [sorted_array[-1]]
    return left_part_sorted + mid_max_index + right_part_sorted