""" Миссия невыполнима: Красный портфель
Итан Хант с невероятным трудом пробирается в секретное хранилище данных Синдиката, в подводный бункер под электростанцией. На добытой им флешке хранятся детали банковских счетов верхушки Синдиката на сумму несколько миллиардов долларов, однако она закрыта "красным портфелем" -- очень сложной технологией шифрования.Ваша миссия: реализовать алгоритм шифрования "Красного портфеля", который не под силу даже специалистам MI-6.
На вход программы подаётся строка текста, состоящая из строчных букв и пробелов. Из строки удаляются все пробелы и определяется её длина N.
На основании N вычисляется размер матрицы, в которую будет упакован исходный текст: из N извлекается квадратный корень, и его нижняя граница берётся как число строк матрицы, а верхняя граница -- как число столбцов. Если их произведение меньше N, увеличивайте количество строк.
Например, есть строка текста
отдай мою кроличью лапку
Она преобразуется в
отдаймоюкроличьюлапку
Длина этой строки -- 21, квадратный корень -- 4.58.
21 элемент в матрицу размером 4x5 элементов не упаковывается, значит, берём матрицу 5x5:
отдай
моюкр
оличь
юлапк
у
И наконец выдаём зашифрованный результат, выдавая символы по столбцам сверху вниз и слева направо, и разделяя столбцы пробелами:
омоюу толл дюиа акчп йрьк
Напишите код, зашифровывающий текстовое сообщение, и декодировщик, расшифровывающий его.
Функция
string TheRabbitsFoot(string s, bool encode)
получает исходную строку s и либо зашифровывает её (encode = true), либо расшифровывает (encode = false), только конечно без исходных пробелов """

""" Итого как я вижу решение данной задачи:
while True - пишем код по зашифровке: 
                        1.удаляем их строки все пробелы и получаем длину N. по этой длине получаем корень числа.
                        2.НАДО ПОНЯТЬ как получить верхнюю и нижнюю границу извлеченного корня, затем сравниваем длину, если она >, то прибавляем единицу к строки или приравниваем к  значению столбца.
                        3. Уточнил, используем import math, math.isqrt 3.8+ и math.ceil
                        4. Получаем значение матрицы(строка, столбец) и вычисляем значения построчно и по столбцу, затем полученные значения объединяем и получаем зашифрованный код.
                        5. Для дешифровки мы используем сплит по пробелу """

import math
def TheRabbitsFoot(s, encode):
    while encode is True:
        s_no_space = s.replace(" ", "")
        N = len(s_no_space)
        matrix_row = math.isqrt(N)
        matrix_col = math.ceil(math.sqrt(N))
        while matrix_row * matrix_col < N:
            matrix_row += 1
        encryption_columns = []
        for j in range(matrix_col):
            col = []
            for i in range(matrix_row):
                index = i * matrix_col + j
                if index < N:
                    col.append(s_no_space[index])
            encryption_columns.append(''.join(col))
            print(col)
        print(encryption_columns)
        return ' '.join(encryption_columns)
    while encode is False:
        groups = s.split()
        matrix_col = len(groups)
        matrix_row = max(len(group) for group in groups)
        decription_list = []
        for i in range(matrix_row):
            for j in range(matrix_col):
                if i < len(groups[j]):
                    decription_list.append(groups[j][i])
        return ''.join(decription_list)
print(TheRabbitsFoot('отдай мою кроличью лапку', True))
            
print(TheRabbitsFoot('омоюу толл дюиа акчп йрьк', False))
print(TheRabbitsFoot("abcdefghi", True))
print(TheRabbitsFoot("adg beh cfi", False))
print(TheRabbitsFoot("abcdefgh", True))
print(TheRabbitsFoot("adg beh cf", False))
print(TheRabbitsFoot("abcdefghij", True))
print(TheRabbitsFoot("aei bfj cg dh", False)) 