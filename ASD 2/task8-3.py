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