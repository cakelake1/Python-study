
list1 = OrderedList(True)
print([node.value for node in list1.get_all()])

list1.add(3)
list1.add(1)
list1.add(2)
print([node.value for node in list1.get_all()])

node = list1.find(2)
print(f"{node.value if node else None}")

list1.delete(2)
print([node.value for node in list1.get_all()])

list2 = OrderedList(False)
list2.add(3)
list2.add(1)
list2.add(2)
print([node.value for node in list2.get_all()])

list3 = OrderedStringList(True)
list3.add("  арбуз  ")
list3.add("баобаб")
list3.add("скворешник")
list3.add("ябеда")
print([node.value for node in list3.get_all()])

list1.clean(False)
list1.add(3)
list1.add(1)
list1.add(2)
print([node.value for node in list1.get_all()])

print(list1.len())

print("добавление по возрастанию:")
list1 = OrderedList(True)
list1.add(5)
list1.add(1)
list1.add(3)
list1.add(7)
list1.add(2)
print([node.value for node in list1.get_all()])  #  [1, 2, 3, 5, 7]

print("\nдобавление по убыванию:")
list2 = OrderedList(False)
list2.add(5)
list2.add(1)
list2.add(3)
list2.add(7)
list2.add(2)
print([node.value for node in list2.get_all()])  #  [7, 5, 3, 2, 1]

print("\nпоиск по возрастанию:")
list3 = OrderedList(True)
list3.add(1); list3.add(3); list3.add(5); list3.add(7); list3.add(9)
print("Найден 5:", list3.find(5).value if list3.find(5) else None)  #  5
print("Не найден 4:", list3.find(4))  #  None
print("Не найден 10:", list3.find(10))  #  None

print("\nПоиск по убыванию:")
list4 = OrderedList(False)
list4.add(9); list4.add(7); list4.add(5); list4.add(3); list4.add(1)
print("Найден 5:", list4.find(5).value if list4.find(5) else None)  #  5
print("Не найден 6:", list4.find(6))  #  None
print("Не найден 0:", list4.find(0))  #  None

print("\nУдаление по возрастанию:")
list5 = OrderedList(True)
list5.add(1); list5.add(2); list5.add(3); list5.add(3); list5.add(4)
print("До удаления:", [node.value for node in list5.get_all()])
list5.delete(3)
print("После удаления первой 3:", [node.value for node in list5.get_all()])  #  [1, 2, 3, 4]

print("\nУдаление по убыванию:")
list6 = OrderedList(False)
list6.add(4); list6.add(3); list6.add(3); list6.add(2); list6.add(1)
print("До удаления:", [node.value for node in list6.get_all()])
list6.delete(3)
print("После удаления первой 3:", [node.value for node in list6.get_all()])  #  [4, 3, 2, 1]

print("\nУдаление несуществующего элемента:")
list7 = OrderedList(True)
list7.add(1); list7.add(2); list7.add(3)
print("До удаления:", [node.value for node in list7.get_all()])
list7.delete(5)  # Не существует
print("После удаления 5:", [node.value for node in list7.get_all()])  #  [1, 2, 3]

print("\nУдаление из пустого списка:")
list8 = OrderedList(True)
list8.delete(1)  # Не должно быть ошибки
print("Пустой список:", [node.value for node in list8.get_all()])  #  []

