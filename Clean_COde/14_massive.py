# 1. Пример 
# numbers = input().split()
# if len(numbers) > 0:
#     last = numbers[-1]
#     i = len(numbers) - 1
#     while i > 0:
#         numbers[i] = numbers[i - 1]
#         i = i - 1
#     numbers[0] = last
# for element in numbers:
#     print(element, end=' ')
# # без прямой индексации:    
# s =[int(i) for i in input().split()]
# last = s.pop()
# s.insert(0,last)
# print(*s)

# 2. Пример
# s =[int(i) for i in input().split()]
# count = 0
# for i in range(len(s)-1):
#     if s[i] < s[i+1]:
#         count+=1
# print(count)
# # без прямой индексации:
# u = [int(i) for i in input().split()]
# counter = -1
# n = 0
# for i in u:
#     if i > n:
#         counter += 1
#     n = i
# print(counter)

# 3. Пример
# n = int(input())
# f_half = 0
# s_half = 0
# th_half = 0
# l_half = 0
# for i in range(n):
#     data = input().split()
#     x = int(data[0])
#     y = int(data[1])
#     if x == 0 or y == 0:
#         continue
#     elif x < 0 and y < 0:
#         th_half += 1
#     elif x > 0 and y > 0:
#         f_half += 1
#     elif x < 0 and y > 0:
#         s_half += 1
#     else: 
#         l_half += 1
# print('Первая четверть:', f_half)
# print('Вторая четверть:', s_half)
# print('Третья четверть:', th_half)
# print('Четвертая четверть:', l_half)
# # без индексации:
# n = int(input())
# list_cor = []
# first, two, three, four = 0, 0, 0, 0
# for i in range(n):
#     inp_lst = input().split()
#     inp_lst = [int(i) for i in inp_lst]
#     list_cor.append(tuple(inp_lst))
# for x, y in list_cor:
#     if x != 0 or y != 0:
#         if x > 0 and y > 0:
#             first += 1
#         elif x > 0 and y < 0:
#             four += 1
#         elif x < 0 and y < 0:
#             three += 1
#         elif x < 0 and y > 0:
#             two += 1
#     else:
#         continue
# print(f'''Первая четверть: {first}
# Вторая четверть: {two}
# Третья четверть: {three}
# Четвертая четверть: {four}''')

# 4. Пример
# s =[int(i) for i in input().split()]
# for i in range(0,len(s)-1,2):
#     s[i],s[i+1] = s[i+1],s[i]
# print(*s)
# # без индексации:
# from collections import deque
# numbers = deque(int(x) for x in input().split())
# numbers.rotate(1)
# print(*numbers)

# 5. Пример
# numbers = input().split()
# counter = 1
# for i in range(len(numbers) - 1):
#     if numbers[i] != numbers[i + 1]:
#         counter += 1
# print(counter)
# # без индексации:
# s =[int(i) for i in input().split()]
# new_s = []
# for i in s:
#     if i not in new_s:
#         new_s.append(i)
# print(len(new_s))