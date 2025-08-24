""" Делаем национальный редактор "Лапоть"
В рамках проекта тотального импортозамещения решено полностью с нуля переписать весь офисный софт в стране. Вы получили подряд с бюджетом миллион рублей по созданию оригинального текстового редактора "Лапоть". Закодируйте его максимально компактно!
"Лапоть" поддерживает пять операций:
1. Добавить(S) -- в конец текущей строки (исходно пустая) добавляется строка S;
2. Удалить(N) -- удалить N символов из конца текущей строки. Если N больше длины текущей строки, удаляем из неё все символы;
3. Выдать(i) -- выдать i-й символ текущей строки (индексация начинается с нуля) в формате строки (строковый тип). Если индекс за пределами строки, возвращайте пустую строку;
4. Undo() -- отмена последней операции 1 или 2; отмена должна уметь выполняться при необходимости неограниченное число раз;
5. Redo() -- выполнить заново последнюю отменённую с помощью Undo операцию; Redo должна уметь выполняться при необходимости неограниченное число раз.
Если после Undo выполняется операция 1 или 2, то
-- предыдущая цепочка операций для Undo обнуляется (откатить можно только последнюю операцию 1 или 2);
-- Redo более становится нечего откатывать.
На вход редактора подаётся одна строка, первый символ которой -- номер операции (1-5) и через пробел, при необходимости, параметр соответствующей операции.
Например:
1 Привет 
В текущей строке будет "Привет"
1  , Мир!
Привет, Мир!
1 ++ 
Привет, Мир!++
2 2
Привет, Мир!
4
Привет, Мир!++
4
Привет, Мир!
1 *
Привет, Мир!*
4
Привет, Мир!
4 
Привет, Мир!
4
Привет, Мир!
3 6
,
2 100
1 Привет 
Привет
1  , Мир!
Привет, Мир!
1 ++ 
Привет, Мир!++
4
Привет, Мир!
4
Привет
5
Привет, Мир!
4
Привет
5
Привет, Мир!
5
Привет, Мир!++
5
Привет, Мир!++
5
Привет, Мир!++
4
Привет, Мир!
4
Привет
2 2
Прив
4
Привет
5
Прив
5
Прив
5
Прив
Функция
string BastShoe(string command)          
получает на вход строку в формате "N параметр", где N -- код операции (1-5), и возвращает текущую строку, или символ в формате строки, если команда Выдать(), или пустую строку в случае её ошибки.
Например, BastShoe("1 Привет") = "Привет"
Если команда задана некорректно, Лапоть ничего не делает (просто возвращает текущую строку без изменений).
Подсказка. Тут, возможно, может смущать, как промежуточное состояние воспроизводить?
Для Python: Вы можете хранить в текущем модуле (в файле, где функция BastShoe() определена) текущую строку как отдельную переменную,
и также в другой переменной список всех её изменений (в виде например списка строк) для реализации Undo/Redo + переменную-позицию в этом списке. Такие глобальные переменные - за пределами определения функции BastShoe - в общем случае плохой стиль, не надо так делать в будущем, правильнее например определить отдельный класс, в котором будет храниться нужное состояние + набор операций, но в данном учебном случае допустимо. Внутри модуля "внешние" переменные во всех функциях, которые в этом модуле определены, нормально видны.
В других языках определяете дополнительные переменные как статические поля класса Level1.
как постить решение
Рефлексия:
    Сначала, конечно испугался такой задлачи, но глаза боятся - руки делают.
    Нам сразу даю подсказку про глобальные переменные(вне функции), с них и начнем.
    Зафиксируем г.п. в виде строки текущего состояния, истории изменений и указателя на текущую историю.
    добавим гп в функцию, далее нам надо разбить входящие значения по пробелу, где первая строка будет operator_code, а вторая это parameter, если параметр не задан - то параметр пустая строка.
    Проверяем, что operator_code это наша цифра от 1 до 5, если нет то возвращаем гп куррент_стат, если цифра, то переводим в число еще. 
    Дальше добавляем логику оператор код, пока можно просто без кода, что там что-то есть. С логикой мы позже жебаться будем.
    Итак я собрал основной скелет программы, очень много if(2шт) и elif(4шт.) в самом конце проверю, можно ли обойтись без них.
        Важно! а как работает вообще андо и редо, если мы сделали один и более раз андо, наш указатель текущего индекеса сместился и мы провели новую операцию, сответственно мы должны очистить будущую историю, чтобы Редо не сработало. и это будет проверятся в каждой и з 5 операций
        Теперь проходим по операциям.
        1. СТавим условие очистки истории, добавляем Строку к текущему состоянию и добавляем в глобальную историю новую текущую строку и указатель обновляем.
        2. Тут как раз из книги лутца в 3 части подходит проверка строки на числа и обработка ощибок с помощью try. аналогично обрезаем хвост, обновляем указатель, проверяем параметр на число, если это не числа, то возвращаем текушее состояние, если число, то удаляем n символов с конца строки. МОжет быть такое, что n будет больше самой строки и при срезе мы получим отрицательное число, от этого можно избавиться через запись max(0,n).
        3. По аналогии проверяем строку на число, но здесь мы будем возвращать не текущую строку в виде ошибки, а пустую строку и Андо и Редо здесь не будут работать, менять указатель, доавьлять в историю также не надо ничего. Просто получить индекс или пустую строку.
        4. Добавил отмену и вперед
        5. и неправильно у меня тесты проходили, часа два-три не мог поянть почему, оказалось, что в 1 и 2 операции вместо history = history[:current_index + 1] надо сделать  history = [history[current_index]]
 """
""" current_state = '' # сьолка текущего сотояния(пустая) 
history = [''] # История изменения(одна пустая строка)
current_index = -1 # указатель индекса в истории

def BastShoe(command):
    global current_state, history, current_index
    space_parts = command.split(' ', 1)
    operator_code = space_parts[0]
    parameter = space_parts[1] if len(space_parts) > 1 else ''
    if operator_code not in ('1', '2', '3', '4', '5'):
        return current_state
    
    if operator_code == '1' :
        if current_index < len(history) - 1: # проверям где указать, если не на полсднем месте - отрезаем
            history = [history[current_index]]
            current_index = 0
        
        current_state += parameter # в общем то только одна строка в это блоке на добавление столки +)
        history.append(current_state) # добавляем в историю
        current_index = len(history) - 1 # обновляем указатель
        return current_state

    elif operator_code == '2':
        try:
            n = int(parameter)
            
        except ValueError:
            return current_state
        if current_index < len(history) - 1: # проверям где указать, если не на полсднем месте - отрезаем
            history = [history[current_index]]
            current_index = 0
        current_state = current_state[:max(0, len(current_state) - n)]
        history.append(current_state) # добавляем в историю
        current_index = len(history) - 1 # обновляем указатель
        return current_state

    elif operator_code == '3':
        try:
            i = int(parameter)
        except ValueError:
            return ''
        if 0 <= i < len(current_state):
            return current_state[i]
        else: 
            return ''

    elif operator_code == '4':
        if current_index > 0 :
            current_index -= 1
            current_state = history[current_index]
        elif current_index == 0:
            pass
        return current_state

    elif operator_code == '5':
        if current_index < len(history) - 1:
            current_index += 1
            current_state = history[current_index]
        return current_state """
current_state = '' 
history = [] 
current_index = -1 

def BastShoe(command):
    global current_state, history, current_index
    
    # Инициализация
    if current_index == -1:
        history = []  
        current_index = -1
        current_state = ''
    
    # Разбор команды
    space_parts = command.split(' ', 1)
    operator_code = space_parts[0]
    parameter = space_parts[1] if len(space_parts) > 1 else ''
    
    # Валидация кода операции
    if operator_code not in {'1', '2', '3', '4', '5'}:
        return current_state
    
    # Используем оператор match-case (Python 3.10+)
    match operator_code:
        case '1':
            # Добавление текста
            if current_index < len(history) - 1: 
                history = [history[current_index]]
                current_index = 0
            
            current_state += parameter 
            history.append(current_state) 
            current_index = len(history) - 1 
            return current_state
            
        case '2':
            # Удаление текста
            try:
                n = int(parameter)
            except ValueError:
                return current_state
                
            if current_index < len(history) - 1: 
                history = [history[current_index]]
                current_index = 0
                
            current_state = current_state[:max(0, len(current_state) - n)]
            history.append(current_state) 
            current_index = len(history) - 1 
            return current_state
            
        case '3':
            # Получение символа
            try:
                i = int(parameter)
            except ValueError:
                return ''
                
            if 0 <= i < len(current_state):
                return current_state[i]
            return ''
            
        case '4':
            # Отмена
            if current_index > 0:
                current_index -= 1
                current_state = history[current_index]
            return current_state
            
        case '5':
            # Повтор
            if current_index < len(history) - 1:
                current_index += 1
                current_state = history[current_index]
            return current_state
         

def reset_editor():
    global current_state, history, current_index
    current_state = ''
    history = []
    current_index = -1
# Тестируем команды из условия задачи

print("=== ТЕСТ 1: Основной сценарий ===")
print(BastShoe("1 Привет"))         # Должно вернуть "Привет"
print(BastShoe("1 ,Мир!"))        # Должно вернуть "Привет, Мир!"  ← убрали лишний пробел
print(BastShoe("1 ++"))             # Должно вернуть "Привет, Мир!++"
print(BastShoe("2 2"))              # Должно вернуть "Привет, Мир!"
print(BastShoe("4"))                # Undo - вернет "Привет, Мир!++"
print(BastShoe("4"))                # Undo - вернет "Привет, Мир!"
print(BastShoe("1 *"))              # Должно вернуть "Привет, Мир!*"
print(BastShoe("4"))                # Undo - вернет "Привет, Мир!"
print(BastShoe("4"))                # Undo - вернет "Привет, Мир!"
print(BastShoe("4"))                # Undo - вернет "Привет, Мир!"
print(BastShoe("цукцук"))                # Undo - вернет "Привет, Мир!"
print(BastShoe("3 6"))              # Должно вернуть ","
print(BastShoe("2 100"))            # Должно вернуть ""

print("\n=== ТЕСТ 2: Undo/Redo цепочка ===")
reset_editor()
print(BastShoe("1 Привет"))         # Должно вернуть "Привет"
print(BastShoe("1  , Мир!"))        # Должно вернуть "Привет, Мир!"
print(BastShoe("1 ++"))             # Должно вернуть "Привет, Мир!++"
print(BastShoe("4"))                # Undo - вернет "Привет, Мир!"
print(BastShoe("4"))                # Undo - вернет "Привет"
print(BastShoe("5"))                # Redo - вернет "Привет, Мир!"
print(BastShoe("4"))                # Undo - вернет "Привет"
print(BastShoe("5"))                # Redo - вернет "Привет, Мир!"
print(BastShoe("5"))                # Redo - вернет "Привет, Мир!++"
print(BastShoe("5"))                # Redo - вернет "Привет, Мир!++"
print(BastShoe("4"))                # Undo - вернет "Привет, Мир!"
print(BastShoe("4"))                # Undo - вернет "Привет"
print(BastShoe("2 2"))              # Должно вернуть "Прив"
print(BastShoe("4"))                # Undo - вернет "Привет"
print(BastShoe("5"))                # Redo - вернет "Прив"
print(BastShoe("5"))                # Redo - вернет "Прив"
print(BastShoe("5"))                # Redo - вернет "Прив" """

print("\n=== ТЕСТ 3: Граничные случаи ===")
reset_editor()
print(BastShoe("3 0"))              # Должно вернуть "" (пустая строка)
print(BastShoe("2 5"))              # Должно вернуть "" (удаление из пустой строки)
print(BastShoe("4"))                # Undo - вернет "Прив" (из предыдущего теста)
print(BastShoe("5"))                # Redo - вернет "" 
print(BastShoe("3 10"))             # Должно вернуть "" (индекс за пределами)
print(BastShoe("9"))                # Некорректная команда - вернет текущее состояние
print(BastShoe("3 abc"))            # Некорректный параметр - вернет ""
def test_scenario_1():
    """Первый сценарий из задачи"""
    print("=== ТЕСТ 1 ===")
    reset_editor()
    
    results = []
    results.append(BastShoe("1 Привет"))         # "Привет"
    results.append(BastShoe("1 , Мир!"))         # "Привет, Мир!"
    results.append(BastShoe("1 ++"))             # "Привет, Мир!++"
    results.append(BastShoe("2 2"))              # "Привет, Мир!"
    results.append(BastShoe("4"))                # "Привет, Мир!++"
    results.append(BastShoe("4"))                # "Привет, Мир!"
    results.append(BastShoe("1 *"))              # "Привет, Мир!*"
    results.append(BastShoe("4"))                # "Привет, Мир!"
    results.append(BastShoe("4"))                # "Привет, Мир!"
    results.append(BastShoe("4"))                # "Привет, Мир!"
    results.append(BastShoe("3 6"))              # ","
    results.append(BastShoe("2 100"))            # ""
    
    print("Результаты теста 1:")
    for i, result in enumerate(results, 1):
        print(f"{i}. '{result}'")
    return results

def test_scenario_2():
    """Второй сценарий из задачи"""
    print("\n=== ТЕСТ 2 ===")
    reset_editor()
    
    results = []
    results.append(BastShoe("1 Привет"))         # "Привет"
    results.append(BastShoe("1 , Мир!"))         # "Привет, Мир!"
    results.append(BastShoe("1 ++"))             # "Привет, Мир!++"
    results.append(BastShoe("4"))                # "Привет, Мир!"
    results.append(BastShoe("4"))                # "Привет"
    results.append(BastShoe("5"))                # "Привет, Мир!"
    results.append(BastShoe("4"))                # "Привет"
    results.append(BastShoe("5"))                # "Привет, Мир!"
    results.append(BastShoe("5"))                # "Привет, Мир!++"
    results.append(BastShoe("5"))                # "Привет, Мир!++"
    results.append(BastShoe("4"))                # "Привет, Мир!"
    results.append(BastShoe("4"))                # "Привет"
    results.append(BastShoe("2 2"))              # "Прив"
    results.append(BastShoe("4"))                # "Привет"
    results.append(BastShoe("5"))                # "Прив"
    results.append(BastShoe("5"))                # "Прив"
    results.append(BastShoe("5"))                # "Прив"
    
    print("Результаты теста 2:")
    for i, result in enumerate(results, 1):
        print(f"{i}. '{result}'")
    return results

# Запускаем тесты
if __name__ == "__main__":
    test_scenario_1()
    test_scenario_2()
def debug_test_1():
    print("=== ДЕБАГ ТЕСТ 1 ===")
    reset_editor()
    
    commands = [
        "1 Привет", "1 , Мир!", "1 ++", "2 2", "4", "4", 
        "1 *", "4", "4", "4"
    ]
    
    for i, cmd in enumerate(commands, 1):
        result = BastShoe(cmd)
        print(f"{i}. '{cmd}' -> '{result}'")
        if i >= 6:  # Печатаем отладочную информацию с 6-й команды
            print(f"   state='{current_state}', index={current_index}, history={history}")

debug_test_1()

def test_scenario_1_debug():
    """Первый сценарий с отладкой"""
    print("=== ТЕСТ 1 DEBUG ===")
    reset_editor()
    
    commands = [
        "1 Привет", "1 , Мир!", "1 ++", "2 2", "4", "4", 
        "1 *", "4", "4", "4", "3 6", "2 100"
    ]
    
    for i, cmd in enumerate(commands, 1):
        result = BastShoe(cmd)
        print(f"{i}. '{cmd}' -> '{result}'")
        if i in [3, 4, 5, 6, 7, 8, 9, 10]:  # После критических команд
            print(f"   state='{current_state}', index={current_index}, history={history}")

def reset_editor():
    global current_state, history, current_index
    current_state = ''
    history = []
    current_index = -1

# Запускаем тест
test_scenario_1_debug()

        