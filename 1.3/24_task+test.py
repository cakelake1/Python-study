""" Матрица: Вращение
К сожалению, никто не может объяснить, что такое Матрица.
Ты должен сам увидеть это.
На вход поступает Матрица размером MxN:
1 2 3 4 5 6 
2 3 4 5 6 7
3 4 5 6 7 8
4 5 6 7 8 9
Ты должен научиться вращать Матрицу относительно её центра по часовой стрелке.
Например, вращение на один шаг:
2 1 2 3 4 5 
3 4 3 4 5 6
4 5 6 7 6 7
5 6 7 8 9 8
Функция
void MatrixTurn(string Matrix[], int M, int N, int T)
получает на вход (по ссылке) массив строк (M строк, каждая длиной N; M >= 2, N >= 2), и вращает его относительно центра по часовой стрелке на T шагов (T >= 1), как описано выше.
То есть результат поворота (повёрнутая матрица) оказывается в исходном массиве Matrix, переданном в функцию по ссылке как аргумент.
Для питонистов: void просто означает, что данная функция ничего не возвращает своим значением (внутри неё не должно быть return).
Минимальное значение из чисел M,N обязательно чётно.
Пример вызова:
MatrixTurn(["123456", "234567", "345678", "456789"], 4,6, 3)
В целом, стиль изменения параметров функции изнутри неё плохой (функция допускает неочевидные побочные эффекты), никогда не надо так делать, но на практике такое к сожалению возможно из-за того, что объекты/коллекции передаются по ссылке, и это надо всегда учитывать.
рефлексируем: """
""" прибавление значений сразу отметаем, по ощущениям здесь должно быть какое то простое решение, толи граничные случаи сначала переместить, толи центр определить и его переставить.
Либо же все делать по порядку, учитывая границы. Сейчас поизучаю похожие перестановки в двумерных массивах.
    Погнали:
1. Матрица у нас в виде строк - нужно перевести в двумерный список
2. Каждая строка в матрице имеет длину N
3. Мы будет вращать матрицу послойно, начинать лучше не из центра, а с внешнего слоя.
4. Каждый слой обрабатывается отдельно
5. Общее количество слоев К = min(M,N) // 2 по условию.
6.Слой это 
верхняя строка [k][k] до [k][N-1],
правый столбец [k+1][N-1-k] до [M-2-k][N-1-k],
нижняя строка [M-1-k][N-1-k] до [M-1-k][k], 
левыйстолбец [M-2-k][k] до [k+1][k]:
k от 0 до K-1:
    ring_list - записываем в одномерный список каждый слой
Дальше мы должны сдвинуть все элементы в ring_list на Т позиций вправо( T mod len(ring_list))
Записать обратно в слой
7. выполнить п.6.   для каждого слоя матрицы
ИИ рекомендует вычислить Т эффективнео, я же думаю в данной задаче можно просто менять индексы местами в правильно последовательности через циклы и чтобы у нас не потерялся первый индекс - временно записывать его и переносить в конец в конце цикла.
Нужно ли вычислить эффективное количество шагов?
Использовать срезы?
Как меняется исходный массив по ссылке? """
""" def MatrixTurn(Matrix, M, N, T):
    matrix_list = [list(Matrix[i]) for i in range(M)]
    K = min(M, N) // 2
    for k in range(0, K - 1): # p.6
        ring_list = []
        for j in range(k+1,N-k):
            ring_list.append(matrix_list[k][j]) # top
        for i in range(k+1, M-k-1):
            ring_list.append(matrix_list[i][N-k-1])
        for j in range(N-k-1, k-1,-1):
            ring_list.append(matrix_list[M - k - 1][j])
        for i in range(M-k-2,k,-1):
            ring_list.append(matrix_list[i][k])
 """
""" def MatrixTurn(Matrix, M, N, T):
    # Преобразуем массив строк в двумерный список символов
    matrix_list = [list(s) for s in Matrix]
    # Определяем количество слоев
    K = min(M, N) // 2
    for _ in range(T):  # Выполняем T полных вращений
        for k in range(K):  # Для каждого слоя
            # Сохраняем первый элемент текущего слоя
            temp = matrix_list[k][k]
            # Вращаем верхнюю строку (слева направо)
            for j in range(k, N - k - 1):
                matrix_list[k][j] = matrix_list[k][j + 1]
            # Вращаем правый столбец (сверху вниз)
            for i in range(k, M - k - 1):
                matrix_list[i][N - k - 1] = matrix_list[i + 1][N - k - 1]
            # Вращаем нижнюю строку (справа налево)
            for j in range(N - k - 1, k, -1):
                matrix_list[M - k - 1][j] = matrix_list[M - k - 1][j - 1]
            # Вращаем левый столбец (снизу вверх)
            for i in range(M - k - 1, k, -1):
                matrix_list[i][k] = matrix_list[i - 1][k]
            # Восстанавливаем сохраненный элемент
            matrix_list[k + 1][k] = temp
    # Обновляем исходный массив Matrix
    for i in range(M):
        Matrix[i] = ''.join(matrix_list[i])
    return Matrix """
""" def MatrixTurn(Matrix, M, N, T):
    # Преобразуем массив строк в двумерный список символов
    matrix_list = [list(s) for s in Matrix]
    K = min(M, N) // 2  # Количество слоев
    
    for k in range(K):
        top = k
        bottom = M - 1 - k
        left = k
        right = N - 1 - k
        ring = []
        
        # Сбор верхней строки (слева направо, без последнего элемента)
        for j in range(left, right):
            ring.append(matrix_list[top][j])
        
        # Сбор правого столбца (сверху вниз, без последнего элемента)
        for i in range(top, bottom):
            ring.append(matrix_list[i][right])
        
        # Сбор нижней строки (справа налево, без последнего элемента)
        for j in range(right, left, -1):
            ring.append(matrix_list[bottom][j])
        
        # Сбор левого столбца (снизу вверх, без последнего элемента)
        for i in range(bottom, top, -1):
            ring.append(matrix_list[i][left])
        
        # Вычисление эффективного сдвига
        L = len(ring)
        if L == 0:
            continue
        T_eff = T % L
        if T_eff != 0:
            ring = ring[-T_eff:] + ring[:-T_eff]
        
        # Запись сдвинутого кольца обратно в матрицу
        index = 0
        for j in range(left, right):
            matrix_list[top][j] = ring[index]
            index += 1
        for i in range(top, bottom):
            matrix_list[i][right] = ring[index]
            index += 1
        for j in range(right, left, -1):
            matrix_list[bottom][j] = ring[index]
            index += 1
        for i in range(bottom, top, -1):
            matrix_list[i][left] = ring[index]
            index += 1
    
    # Обновление исходного массива
    for i in range(M):
        Matrix[i] = ''.join(matrix_list[i])
    return Matrix """
def MatrixTurn(Matrix, M, N, T):
    matrix_list = [list(s) for s in Matrix]
    K = min(M, N) // 2
    for k in range(K):
        ring = []
        # Верхняя строка
        for j in range(k, N - k):
            ring.append(matrix_list[k][j])
        # Правый столбец без углов
        for i in range(k + 1, M - k - 1):
            ring.append(matrix_list[i][N - k - 1])
        # Нижняя строка, если существуе
        for j in range(N - k - 1, k - 1, -1):
                ring.append(matrix_list[M - k - 1][j])
        for i in range(M - k - 2, k, -1):
                ring.append(matrix_list[i][k])
        L = len(ring)
        t = T % L
        if t == 0:
            continue
        new_ring = ring[L - t:] + ring[:L - t]
        index = 0
        # Заполняем верхнюю строку
        for j in range(k, N - k):
            matrix_list[k][j] = new_ring[index]
            index += 1
        # Заполняем правый столбец
        for i in range(k + 1, M - k - 1):
            matrix_list[i][N - k - 1] = new_ring[index]
            index += 1
        # Заполняем нижнюю строку
        for j in range(N - k - 1, k - 1, -1):
                matrix_list[M - k - 1][j] = new_ring[index]
                index += 1
        # Заполняем левый столбец
        for i in range(M - k - 2, k, -1):
                matrix_list[i][k] = new_ring[index]
                index += 1
    for i in range(M):
        Matrix[i] = ''.join(matrix_list[i])
    return Matrix
print(MatrixTurn(["123456", "234567", "345678", "456789"], 4,6, 3))
print(MatrixTurn(["123456", "234567", "345678", "456789"], 4,6, 1))
print(MatrixTurn(["12", "34"], 2, 2, 1))
# Ожидаемый результат: ['31', '42']
print(MatrixTurn(["1234", 
                  "5678", 
                  "9ABC", 
                  "DEFG"], 4, 4, 1))
# Ожидаемый результат: ['5123', '96A7', 'DEB8', 'EFGC']


