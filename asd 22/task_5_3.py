# глубина 0 
arr_0 = [42]
result_0 = GenerateBBSTArray(arr_0)
print(len(result_0))  # 1
print(result_0)  # [42]
#глубина 1
arr_1 = [10, 5, 15]
result_1 = GenerateBBSTArray(arr_1)
print(len(result_1))  # 3
print(result_1)  # [10, 5, 15]
#глубина 2
arr_2 = [50, 25, 75, 12, 37, 62, 87]
result_2 = GenerateBBSTArray(arr_2)
print(len(result_2))  # 7
print(result_2)  # [50, 25, 75, 12, 37, 62, 87]
# неотсортированный массив
arr_unsorted = [10, 5, 15, 3, 7, 12, 18]
result_unsorted = GenerateBBSTArray(arr_unsorted)
print(len(result_unsorted))  # 7
print(result_unsorted)  # [10, 5, 15, 3, 7, 12, 18]
# массив без уникальных значений
arr_duplicate = [3, 1, 3, 2, 1, 2, 3]
result_duplicate = GenerateBBSTArray(arr_duplicate)
print(len(result_duplicate))  # 7
print(result_duplicate)  # [2, 1, 3, 1, 3, 2, 2]
# отриц значения и ноль
arr_negative = [0, -5, 5, -10, -3, 3, 10]
result_negative = GenerateBBSTArray(arr_negative)
print(len(result_negative))  # 7
print(result_negative)  # [0, -5, 5, -10, -3, 3, 10]
# обход в ширину
print(result_0)  # [42]
print(result_1)  # [10, 5, 15]
print(result_2)  # [50, 25, 75, 12, 37, 62, 87]
print(result_negative)  # [0, -5, 5, -10, -3, 3, 10]
print(GenerateBBSTArray([]))  # [] (пустой массив)