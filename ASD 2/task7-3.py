# main_test Добавьте тесты для добавления, удаления и поиска элемента по его значению -- каждый случай с учётом признака упорядоченности.
# тест на добавление по возрастанию
list1 = OrderedList(True)
list1.add(5)
list1.add(1)
list1.add(3)
list1.add(7)
list1.add(2)
print([node.value for node in list1.get_all()])  #  [1, 2, 3, 5, 7]

# тест на добавление по убыванию
list2 = OrderedList(False)
list2.add(5)
list2.add(1)
list2.add(3)
list2.add(7)
list2.add(2)
print([node.value for node in list2.get_all()])  #  [7, 5, 3, 2, 1]

# тест на поиск по возрастанию
list3 = OrderedList(True)
list3.add(1)
list3.add(3)
list3.add(5)
list3.add(7)
list3.add(9)
print("5", list3.find(5).value if list3.find(5) else None)  #  5
print("4", list3.find(4))  #  None
print("10", list3.find(10))  #  None

# тест на поиск по убыванию
list4 = OrderedList(False)
list4.add(9)
list4.add(7)
list4.add(5)
list4.add(3)
list4.add(1)
print("5", list4.find(5).value if list4.find(5) else None)  #  5
print("6", list4.find(6))  #  None
print("0", list4.find(0))  #  None

# тест на удаление по возрастанию
list5 = OrderedList(True)
list5.add(1)
list5.add(2)
list5.add(3)
list5.add(3)
list5.add(4)
print([node.value for node in list5.get_all()])
list5.delete(3)
print([node.value for node in list5.get_all()])  #  [1, 2, 3, 4]

# тест на удаление по убыванию
list6 = OrderedList(False)
list6.add(4)
list6.add(3)
list6.add(3)
list6.add(2)
list6.add(1)
print([node.value for node in list6.get_all()])
list6.delete(3)
print([node.value for node in list6.get_all()])  #  [4, 3, 2, 1]

# тест на удаление по граничного значения
list7 = OrderedList(True)
list7.add(1)
list7.add(2)
list7.add(3)
print([node.value for node in list7.get_all()])
list7.delete(5)  # Не существует
print([node.value for node in list7.get_all()])  #  [1, 2, 3]

# тест на удаление элемента в пустом списке
list8 = OrderedList(True)
list8.delete(1)  
print([node.value for node in list8.get_all()])  #  []


# 8* тест на удаление элемента дубликатов
ol = OrderedList(True)
for num in [1, 1, 2, 2, 2, 3, 4, 4, 5]:
    ol.add(num)
print([node.value for node in ol.get_all()])
ol.delete_duplicate()
print([node.value for node in ol.get_all()])
print(ol.len())


# 9 * Тест на списки по возрастанию
list1 = OrderedList(True)
for v in [1, 3, 5]: list1.add(v)
list2 = OrderedList(True)
for v in [2, 4, 6]: list2.add(v)
merged = list1.merge(list2)
print([n.value for n in merged.get_all()])
# Тест на списки по убыванию
list3 = OrderedList(False)
for v in [5, 3, 1]: list3.add(v)
list4 = OrderedList(False)
for v in [6, 4, 2]: list4.add(v)
merged2 = list3.merge(list4)
print([n.value for n in merged2.get_all()])

# Тест на списки c одинаковыми значениями
list7 = OrderedList(True)
for v in [1, 1, 1]: list7.add(v)
list8 = OrderedList(True)
for v in [1, 1]: list8.add(v)
merged4 = list7.merge(list8)
print([n.value for n in merged4.get_all()])

# * 10 Проверка наличия заданного упорядоченного под-списка в текущем списке.
list1 = OrderedList2(asc=True)
for num in [1, 2, 3, 4, 5, 6]:
    list1.add(num)
sublist1 = OrderedList2(asc=True)
for num in [2, 3, 4]:
    sublist1.add(num)
print(list1.sublist_contain(sublist1)) 
sublist2 = OrderedList2(asc=True)
for num in [3, 4, 6]:
    sublist2.add(num)
print(list1.sublist_contain(sublist2))

# 11.* Добавьте метод, который находит наиболее часто встречающееся значение в списке.
list1 = OrderedList2(asc=True)
for num in [1, 1, 2, 2, 2, 3]:
    list1.add(num)
print([n.value for n in list1.get_all()])
print(list1.hits_num())  
list2 = OrderedList2(asc=True)
for num in [5]:
    list2.add(num)
print([n.value for n in list2.get_all()])
print(list2.hits_num())
list3 = OrderedList2(asc=True)
for num in [1, 2, 3, 4, 5]:
    list3.add(num)
print([n.value for n in list3.get_all()])
print(list3.hits_num())
list4 = OrderedList2(asc=True)
print(list4.hits_num())

#12.* Добавьте в упорядоченный список возможность найти индекс элемента (параметр) в списке, которая должна работать за o(log N).
list_1 = OrderedList3(True)
for val in [10, 20, 30, 40, 50]:
    list_1.add(val)
print(list_1.find_index_bin(30))  
print(list_1.find_index_bin(10))  
print(list_1.find_index_bin(50))  
print(list_1.find_index_bin(25))  
list_2 = OrderedList3(False)
for val in [50, 40, 30, 20, 10]:
    list_2.add(val)
print(list_2.find_index_bin(30))  
print(list_2.find_index_bin(50))  
print(list_2.find_index_bin(10))  
print(list_2.find_index_bin(25))