# main quest:
bloom = BloomFilter(32)
test_str = [
    "0123456789", "1234567890", "2345678901", "3456789012", "4567890123",
    "5678901234", "6789012345", "7890123456", "8901234567", "9012345678" , "901rtr234567123"
]
fake_str = ["0000000000", "sdfsdgsdgs", "xXx", "bloom_bloom_baloon_bb"]
for s in test_str:
    bloom.add(s)
for s in test_str:
    if bloom.is_value(s):
        print('строка',s, 'есть')
    else:
        print('строки',s, 'нет')
for s in fake_str:
    if bloom.is_value(s):
        print('строка',s, 'есть')
    else:
        print('строки',s, 'нет')

# 2 *Напишите алгоритм слияния нескольких фильтров Блюма (одинакового размера и с одинаковым набором хэш-функций)
filter1 = BloomFilter2(32)
filter2 = BloomFilter2(32) 
filter3 = BloomFilter2(32)
filter1.add("один")
filter1.add("два")
filter2.add("три")
filter2.add("четыре")
filter3.add("четыре")
filter3.add("пять")
merged_filter = BloomFilter2(32)
merged_filter.merge([filter1, filter2, filter3])
test_numbers = ["один", 'два', "три", "четыре", "пять", "кекс"]
for item in test_numbers:
    if merged_filter.is_value(item):
        print(item, '- есть')
    else:
        print(item, '- нет в списке')

# 3 *
filter1 = BloomFilter3(32)
filter1.add("один")
filter1.add("два")
filter1.add("три")
filter1.add("пять")
print(filter1.remove('один'))
print(filter1.is_value('один'))
print(filter1.remove('кекс'))
filter1.add("четыре")
print(filter1.new_items)

# 4 * 
filter1 = BloomFilter4(32)
filter1.add("один")
filter1.add("два")
filter1.add("три")
check1 = ["один", "два", "три"]
check2 = ["один", "два"]
check3 = ["один", "четыре"]
check4 = ["четыре", "пять"]
print(filter1.analize_check(check1))
print(filter1.analize_check(check2))
print(filter1.analize_check(check3))
print(filter1.analize_check(check4))
list_check = ["один", "два", "три", "четыре", "пять", "шесть"]
print(filter1.potential_elements(list_check))
print(filter1.new_items)
filter2 = BloomFilter4(32)
print(filter2.is_value('один'))
print(filter2.analize_check(["один"]))
print(filter2.potential_elements(list_check))
print(filter2.new_items)