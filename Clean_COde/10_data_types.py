# 1. (char == '=') -(char == WALKER_SYMBOL) убрал магический символ
# 2. if number_1 + number_2 == 10 - if number_1 + number_2 == SUM_TARGET: # убрал магическое число константой
# 3. correct_pairs.append(count == 3) - correct_pairs.append(count == COLLECT_WALKERS) # убрал магическое число Константой
#  Есть такой код:
# def squirrel(N):
#     x = 1
#     for i in range(1, N + 1):
#         x = x * i
#         while x >= 10:
#             x = x / 10
#     return int(x)
#  def squirrel(N):
#     if N <0: # 9 ну и проверку добавляем сразу на отрицательное 
#         raise ValueError('получено отрицательное число')
#     if N == 0: # 10 проверка если N == 0
#         return 1
#     result = 1 #4 избавляюсь от переменной х
#     for i in range(1, N + 1):
#         result *=  i
#         while result % 10== 0: # 5 избавляюсь от сравнения разных типов
#             result //= 10 # 6 избавляюсь от преобразования разных типов
#         result %= 10**10 # 7 переход на целые числа(отказ от вещественных)
#     return result % 10 # 8 нахожу последнюю цифру
#  код:
# for i in range(len(oksana)):
#         if i % 2 == 0:
#             speed = oksana[i]
#             time = oksana[i + 1]  # Опасность: если i последний, то i+1 выходит за границы.
#             full_speed = full_speed + speed * (time - past_time)
#             past_time = time

# for i in range(0, len(oksana), 2): #11 избавляемся от проверки на четность
#         speed = oksana[i]
#         time = oksana[i + 1]
#         if speed < 0: # 12 добавляем проверку на отрицательную скорость
#             raise ValueError('скорость отрицательная')
#         distance += speed * (time - prev_time)
#         prev_time = time