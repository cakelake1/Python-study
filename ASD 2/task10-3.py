#main_test:

#возможность добавления отсутствующего элемента и невозможность добавления присутствующего в множестве элемента с помощью put()
s = PowerSet()
print(s.size())
s.put(100)
print(s.size())
print(s.get(100))
s.put(100)
print(s.size())

#удаление элемента с помощью remove()
s.put(200)
print(s.size())
s.remove(200)
print(s.get(200))
print(s.size())
#пересечение множеств intersection(), чтобы в результате получались как пустое, так и непустое множества;
set1 = PowerSet()
set2 = PowerSet()
set1.put(1)
set1.put(2)
set1.put(3)
set2.put(2)
set2.put(3)
set2.put(4)

print(list(set1.storage.keys()))
print(list(set2.storage.keys()))
    # непустое пересечение
result = set1.intersection(set2)
print(result.size())
print(list(result.storage.keys()))

    # пустое пересечение
set3 = PowerSet()
set3.put(5)
set3.put(6)
result = set1.intersection(set3)
print(result.size())
print(result.size() == 0)
#объединение union(), когда оба параметра непустые, и когда один из параметров -- пустое множество;
    # объединение непустых множеств
result = set1.union(set2)
print(result.size())
print(list(result.storage.keys()))
    # объединение с пустым множеством
empty = PowerSet()
result = set1.union(empty)
print(result.size())
print(list(result.storage.keys()))

#разница difference(), чтобы в результате получались как пустое, так и непустое множества
set4 = PowerSet()
set5 = PowerSet()
set4.put(10)
set4.put(20)
set4.put(30)
set4.put(40)
set5.put(20)
set5.put(40)
set5.put(50)
print(list(set4.storage.keys()))
print(list(set5.storage.keys()))
    # непустая разность
result = set4.difference(set5)
print(result.size())
print(list(result.storage.keys()))
    # пустая разность
set6 = PowerSet()
set7 = PowerSet()
set6.put(1)
set7.put(2)
set7.put(1)
set7.put(2)
set7.put(3)
result = set6.difference(set7)
print(result.size())
print(result.size() == 0)
#подмножество issubset() -- рассмотрите три случая (все элементы параметра входят в текущее множество, все элементы текущего множества входят в параметр, не все элементы параметра входят в текущее множество);
main_set = PowerSet()
main_set.put(1)
main_set.put(2)
main_set.put(3)
main_set.put(4)
main_set.put(5)
print(main_set.storage.keys())
    # все элементы параметра входят в M
subset = PowerSet()
subset.put(2)
subset.put(4)
print(list(subset.storage.keys()))
result = main_set.issubset(subset)
print(result)
    # не все элементы параметра входят в M
not_subset = PowerSet()
not_subset.put(3)
not_subset.put(6)
print(list(not_subset.storage.keys()))
result = main_set.issubset(not_subset)
print(result)
    # параметр содержит все элементы M и еще один
bigger = PowerSet()
bigger.put(1)
bigger.put(2)
bigger.put(3)
bigger.put(4)
bigger.put(5)
bigger.put(6)
print(list(bigger.storage.keys()))
result = main_set.issubset(bigger)
print(result)

#равенство equals() -- проверка, равно ли текущее множество параметру;
set1 = PowerSet()
set2 = PowerSet()
set3 = PowerSet()
set4 = PowerSet()
set1.put(1)
set1.put(2)
set1.put(3)
set2.put(3)
set2.put(2)
set2.put(1)  
set3.put(1)
set3.put(2)
set3.put(4)  
set4.put(1)
set4.put(2) 
print(list(set1.storage.keys()))
print(list(set2.storage.keys()))
print(list(set3.storage.keys()))
print(list(set4.storage.keys()))
print(et1.equals(set2))
print(set1.equals(set3))
print(set1.equals(set4))
    # проверка двух пустых множеств
empty1 = PowerSet()
empty2 = PowerSet()
print(empty1.equals(empty2))

# быстродействие (операции над множествами из десятков тысяч элементов укладываются в пару секунд).
big_set1 = PowerSet()
big_set2 = PowerSet()
for i in range(30000):
    big_set1.put(i)
for i in range(5000, 15000):
    big_set2.put(i)
print(big_set1.size())
print(big_set2.size())
    # время перечения, размер
start = time.time()
result = big_set1.intersection(big_set2)
intersection_time = time.time() - start
print(intersection_time, result.size()) 
    # время обьединения, размер
start = time.time()
result = big_set1.union(big_set2)
union_time = time.time() - start
print(union_time, result.size()) 
    # время Разности, размер
start = time.time()
result = big_set1.difference(big_set2)
difference_time = time.time() - start
print(difference_time, result.size())
    # время проверки на подмножества
start = time.time()
result = big_set1.issubset(big_set2)
issubset_time = time.time() - start
print(issubset_time, result)
    # время на проверку совпадающих множеств, у нас не равны
start = time.time()
result = big_set1.equals(big_set2)
equals_time = time.time() - start
print(equals_time, result)
    # макисмальное время из всех проверок
print(max(intersection_time, union_time, difference_time, issubset_time, equals_time))