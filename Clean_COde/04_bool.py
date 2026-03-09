# 7.1. Приведите пять примеров правильного именования булевых переменных в вашем коде в формате "было - стало".
    # 1.flag = True - is_same_digit = True(состоит ли указанное число из одинаковых цифр)
    # 2. has_seven = True - is_descending = True (проверка на убывание цифр)
    # 3. flag = False - is_even = True
    # 4. flag= False - has_duplicates = True
    # 5. flag= False - is_palindrome = True
# 7.2. Найдите несколько подходящих случаев, когда в вашем коде можно использовать типичные имена булевых переменных.
    # 1.
        # students = ["Рафик", "Спанч Боб", "Геральт", "Глобус"]
        # search_name = "Глобус"
        # flag = False
        # for student in students:
        #     if student == search_name:
        #         flag = True
        #         break
        # if flag:
        #     print("Студент найден")
            # стало
        # students = ["Рафик", "Спанч Боб", "Геральт", "Глобус"]
        # search_name = "Глобус"
        # found  = False
        # for student in students:
        #     if student == search_name:
        #         found  = True
        #         break
        # if found :
        #     print("Студент найден")
    # 2. 
        # if len(password) < 8:
        #     print("Пароль слишком короткий")
        #     correct = False
        # if not any(i.isdigit() for i in password):
        #     print("Пароль должен содержать цифру")
        #     correct = False
        # if correct:
        #     print("Пароль принят")
                # стало
        # password = input("Введите пароль: ")
        # ok = True 
        # if len(password) < 8:
        #     print("Пароль слишком короткий")
        #     ok = False
        # if not any(i.isdigit() for i in password):
        #     print("Пароль должен содержать цифру")
        #     ok = False
        # if ok:
        #     print("Пароль принят")
    # 3. 
        # numbers = [3, 7, 2, 9, 4, 1]
        # stop = False
        # i = 0
        # while i < len(numbers) and not stop:
        #     if numbers[i] % 2 == 0:
        #         print(f"Найдено чётное число: {numbers[i]}")
        #         stop = True
        #     i += 1
                    # стало
        # numbers = [3, 7, 2, 9, 4, 1]
        # done = False
        # i = 0
        # while i < len(numbers) and not done:
        #     if numbers[i] % 2 == 0:
        #         print(f"Найдено чётное число: {numbers[i]}")
        #         done = True
        #     i += 1
# 7.3. Проверьте, правильно ли вы даёте имена индексам циклов. Попробуйте найти случай, когда вместо i j k нагляднее использовать более выразительное имя.
    #1. Данный конкретный случай я могу взять из предыдущего задания, потому, что необходимо было указать переменные для контекста, он подходит.
        #def first_digit_of_factorial(number):
        #     product  = 1
        #     for factor in range(1, number + 1):
        #         product  = product  * factor 
        #         while product  >= 10:
        #             product  = product  / 10
        #     return int(product)
    #2. Табдица сложения
        # n = int(input())
        # for first_digit in range(1,n+1):
        #     for second_digit in range(1,10):
        #         print(str(first_digit),'+', str(second_digit),'=', first_digit + second_digit)
        #     print()
    #3. Задача на часы
        # n = int(input())
        # for hours in range(24):
        #     for minutes in range(60):
        #         if hours**n == minutes:
        #             print(f'{hours:02d}:{minutes:02d}')
# 7.4. Попробуйте найти в своих решениях два-три случая, когда можно использовать пары имён - антонимы.
    #1. Возрастание и убывание
        #   def MadMaproduct (N, Tele):
        #     sorted_array = sorted(Tele)
        #     center = (N - 1) // 2
        #     ascending_part = sorted_array[:center]
        #     descending_part = sorted_array[center:-1]
        #     descending_part.reverse()
        #     mid_maproduct _indeproduct  = [sorted_array[-1]]
        #     return ascending_part + mid_maproduct _indeproduct  + descending_part
    #2. Проверка email
        # email = input("Введите email: ")
        # valid = '@' in email and '.' in email
        # invalid = not valid
        # if valid:
        #     print("Email корректный")
        # else:
        #     print("Неправильный email")
#7.5. Всем ли временным переменным в вашем коде присвоены выразительные имена? Найдите несколько случаев, когда временные переменные надо переименовать, и поищите, возможно, от некоторых временных переменных вам получится вообще полностью избавиться.
    # 1.
        # def squirrel(N):
        #     x = 1
        #     for i in range(1, N + 1):
        #         x = x * i
        #         while x >= 10:
        #             x = x / 10
        #     return int(x)
                 # стало
        # def squirrel(number):
        #     first_digit = 1  
        #     for current_number in range(1, number + 1):
        #         first_digit = first_digit * current_number
        #         while first_digit >= 10:
        #             first_digit = first_digit // 10  
        #     return first_digit
    # 2.
        # n1 = [int(i) for i in input().split()]
        # summ_of_n1 = 0
        # n2 = []
        # for i in range(len(n1)):
        #     summ_of_n1 +=n1[i]
        #     n2.append(n1[i])
        # print(*n2, sep='+',end='=')
        # print(summ_of_n1)
            # стало(убрал одну временную переменную n2)
        # numbers = [int(x) for x in input().split()]
        # total = 0
        # for value in numbers:
        #     total += value
        # print(*numbers, sep='+', end='=')
        # print(total)
    # 3.
        # n1 = [int(i) for i in input().split()]
        # n2 = [int(i) for i in input().split()]
        # summ_of_two_lists = []
        # for i in range(len(n1)):
        #     summ_of_two_lists.append(n1[i] + n2[i])
        # print(*summ_of_two_lists)
                # стало
        # first_list = [int(x) for x in input().split()]
        # second_list = [int(x) for x in input().split()]
        # result_sums = []
        # for index in range(len(first_list)):
        #     result_sums.append(first_list[index] + second_list[index])
        # print(*result_sums)