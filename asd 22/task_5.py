def GenerateBBSTArray(a):
    if not a:
        return []
    s_a = sorted(a)
    n = len(s_a)
    result = [None] * n
    def recursive_tree(array, index):
        if not array:
            return None
        mid = len(array) // 2
        result[index] = array[mid]
        left_c_index = 2 * index + 1
        right_c_index = 2 * index + 2
        recursive_tree(array[:mid], left_c_index)
        recursive_tree(array[mid+1:], right_c_index)
    recursive_tree(s_a, 0)
    return result
