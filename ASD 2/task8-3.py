#hash_fun
ht2 = HashTable(10, 3)
h1 = ht2.hash_fun("test")
h2 = ht2.hash_fun("test")
print(h1 == h2)
print(0 <= h1 < 10)

#seek_slot
ht3 = HashTable(5, 1)
slot = ht3.seek_slot("x")
print(slot is not None)
print(0 <= slot < 5)

#put
ht4 = HashTable(5, 2)
idx = ht4.put("cat")
print(idx is not None)
print(ht4.slots[idx] == "cat")

#find
ht5 = HashTable(5, 2)
ht5.put("cat")
found_idx = ht5.find("cat")
print(found_idx is not None)
print(ht5.slots[found_idx] == "cat")
print(ht5.find("dog") is None)

# 3,4*
ht = HashTable(4, 1)
print(f"Начальный размер: {ht.size}")
ht = HashTable(4, 1)
print(ht.size)
test_data = ["test1", "test2", "test3", "test4", "test5"]
for i, value in enumerate(test_data):
    print(value)
    print(f"заполнение_начало: {ht.count}/{ht.size} = {ht.count/ht.size:.0%}")
    index = ht.put(value)
    print(index)
    print(f"заполнение_конец: {ht.count}/{ht.size} = {ht.count/ht.size:.0%}")
    if i == 3:
        print("Видим расширение таблицы")
print(ht.size)  

#5*
ht = HashTable(5, 2)
print(f"Создана таблица с солью: {ht.salt}")
test_data = ["test1", "test2", "test3", "test4", "test5"]
for v in test_data:
    idx = ht.put(v)
    print(f" '{v}' {idx}")
for v in ["test1", "test3", "test10"]:
    idx = ht.find(v)
    if idx is not None:
        print(f" '{v}' найден в {idx}")
    else:
        print(f" '{v}' не найден")
for i in range(ht.size):
    if ht.slots[i] is not None:
        print(f"  [{i}]: '{ht.slots[i]}'")