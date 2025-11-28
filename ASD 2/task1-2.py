Задание.
Попробуйте оценить какие-нибудь свои или чужие программы, которые выполняют объёмную вычислительную работу -- какова мера их сложности, как сильно растёт время их работы по мере увеличения входных данных? Напишите небольшой отчёт.

Я беру свое последнее решение:

def sum_elements(n, matrix):
    list_prefix = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            list_prefix[i][j] = (matrix[i-1][j-1] + list_prefix[i-1][j] + list_prefix[i][j-1] - list_prefix[i-1][j-1])
    return list_prefix
def sum_matrix(list_prefix, row, col, size):
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

1. Арифметические операции с элементами матрицы О(1)
2. Создание матрицы префиксов О(n^2)
3. Поиск подматрицы О(n^3)

*1.8
# как я предполагаю мы используем данные остальные из задачи, тогда:
def sum_linked_lists(list1, list2):
    if list1.len() != list2.len():
        return None
    result = LinkedList()
    node1, node2 = list1.head, list2.head
    while node1:
        result.add_in_tail(Node(node1.value + node2.value))
        node1, node2 = node1.next, node2.next
    return result