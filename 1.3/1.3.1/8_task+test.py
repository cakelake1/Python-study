def sum_elements(n, matrix):
    # Создаем префиксную матрицу размером (n+1) x (n+1) для упрощения вычислений
    list_prefix = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            list_prefix[i][j] = (matrix[i-1][j-1] + list_prefix[i-1][j] + list_prefix[i][j-1] - list_prefix[i-1][j-1])
    return list_prefix
def sum_matrix(list_prefix, row, col, size):
    # Используем координаты для префиксной матрицы (размер n+1)
    return (list_prefix[row+size][col+size] - list_prefix[row][col+size] - list_prefix[row+size][col] + list_prefix[row][col])
def army_communication_matrix(n, matrix):
    max_row = 0
    max_sum = None
    max_col = 0
    max_size = 2
    new_matrix = sum_elements(n, matrix)
    for size in range(2, n):
        for row in range(n - size + 1):
            for col in range(n - size + 1):
                current_sum = sum_matrix(new_matrix, row, col, size)
                if max_sum is None or current_sum > max_sum:
                    max_sum = current_sum
                    max_row, max_col, max_size = row, col, size
    return str(max_col) + " " + str(max_row) + " " + str(max_size)
# Тест 1: положительные числа
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Тест 1 (положительные):", army_communication_matrix(3, matrix1))
# Результат: "0 0 2" (правильно)

# Тест 2: отрицательные числа
matrix2 = [
    [-1, -2, -3],
    [-4, -5, -6],
    [-7, -8, -9]
]
print("Тест 2 (отрицательные):", army_communication_matrix(3, matrix2))
# Результат: "0 0 2" (НЕПРАВИЛЬНО!)
# Тест 1: положительные числа 4x4
matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print("Тест 1 (положительные 4x4):", army_communication_matrix(4, matrix1))
# Должно найти подматрицу 3x3: [6,7,8, 10,11,12, 14,15,16] = 99

# Тест 2: отрицательные числа 4x4
matrix2 = [
    [-1, -2, -3, -4],
    [-5, -6, -7, -8],
    [-9, -10, -11, -12],
    [-13, -14, -15, -16]
]
print("Тест 2 (отрицательные 4x4):", army_communication_matrix(4, matrix2))
# Найдет подматрицу с наименьшим отрицательным числом

# Тест 3: смешанные числа
matrix3 = [
    [1, -10, 3, 4],
    [-5, 20, -7, 8],
    [9, -10, 15, -12],
    [-13, 14, -15, 16]
]
print("Тест 3 (смешанные 4x4):", army_communication_matrix(4, matrix3))