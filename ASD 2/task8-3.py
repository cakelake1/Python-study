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
print(ht.size)
ht = HashTable(4, 1)
print(ht.size)
test_data = ["test1", "test2", "test3", "test4", "test5"]
for i, value in enumerate(test_data):
    print(value)
    load_1 = ht.count / ht.size 
    print(load_1:.0%)
    index = ht.put(value)
    print(index)
    load_2 = ht.count / ht.size
    print(load_2:.0%)
    if i == 3:
        print("расширение таблицы")
print(ht.size)  

#5*
ht = HashTable(5, 2)
print(ht.salt)
test_data = ["test1", "test2", "test3", "test4", "test5"]
for v in test_data:
    idx = ht.put(v)
    print(v, idx)
for v in ["test1", "test3", "test10"]:
    idx = ht.find(v)
    if idx is not None:
        print(v,idx)
    else:
        print(v, ' не найден')
for i in range(ht.size):
    if ht.slots[i] is not None:
        print([i], {ht.slots[i]})