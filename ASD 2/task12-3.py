# task 10 *4
set1 = PowerSet()
set1.put(1)
set1.put(2)
set2 = PowerSet()
set2.put('a')
set2.put('b')
set2.put('c')
result_1 = cartesian(set1, set2)
print(result_1)
set3 = PowerSet()
set3.put(1)
set3.put(2)
result_2 = cartesian(set3)
print(result_2)

# task 11-2 *3
bloom_filter_1 = BloomFilter3(f_len=32)
bloom_filter_1.add('1')
bloom_filter_1.add('2')
bloom_filter_1.add('3')
print(bloom_filter_1.is_value('1'))
print(bloom_filter_1.is_value('2'))
print(bloom_filter_1.is_value('3'))
print(bloom_filter_1.is_value('4')) # False
bloom_filter_1.remove('1')
print(bloom_filter_1.is_value('1')) # False
print(bloom_filter_1.is_value('2'))
bloom_filter_1.add('1')
print(bloom_filter_1.is_value('1')) # True