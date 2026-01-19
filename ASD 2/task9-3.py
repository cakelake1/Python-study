# Сделайте тесты, проверяющие, как работают put(), is_key() и get():
    # добавление значения по новому ключу

test_1 = NativeDictionary(10)
    
    # Добавление значения по новому ключу
test_1.put("name", "Иван")
print(test_1.get('name'))
print(test_1.is_key('name'))
print()

    # Добавление значения по уже существующему ключу

test_1.put("name", "Ваня")
print(test_1.get('name'))
print(test_1.is_key('name'))
print()

    # Добавление  нового ключа

test_1.put("age", "21")
print(test_1.get('age'))
print()

    # Проверка ключа
print(test_1.is_key('age'))

    # Проверка отсутствующего ключа
print(test_1.is_key('height'))

    # Извлечение значения по ключу
print(test_1.get('age'))
print(test_1.get('name'))

    # Извлечение значения по пустому ключу
print(test_1.get('height'))

# 5*
test_1 = NativeDictionary(10)
    
    #Добавление значения по новому ключу
test_1.put("name", "Иван")
print(test_1.get('name'))
print(test_1.is_key('name'))
print()

    # Добавление значения по уже существующему ключу
test_1.put("name", "Ваня")
print(test_1.get('name'))
print(test_1.is_key('name'))
print()

# Добавление другого нового ключа
test_1.put("age", "21")
print(test_1.get('age'))
print()

# проверка присутствующего ключа
print(test_1.is_key('age'))
# проверка отсутствующего ключа
print(test_1.is_key('height'))
# извлечение значения по существующему ключу
print(test_1.get('age'))
print(test_1.get('name'))
# извлечение значения по отсутствующему ключу
print(test_1.get('height'))
print()
#дополнительные тесты для проверки сортировки
test_2 = NativeDictionary(10)
test_2.put("banana", "желтый")
test_2.put("apple", "красный")
test_2.put("cherry", "вишневый")
print(test_2.get('apple'))
print(test_2.get('banana'))
print(test_2.get('cherry'))
print()
print(test_2.is_key('apple'))
print(test_2.is_key('banana'))
print(test_2.is_key('cherry'))
print(test_2.is_key('date'))


# 6 *
# Добавление значения по новому ключу
dict1.add(123, "Иван")
print(dict1.get(123))
print(dict1.find(123))
print()

# Добавление значения по уже существующему ключу
dict1.add(123, "Ваня")
print(dict1.get(123))
print(dict1.find(123))
print()

# Добавление другого нового ключа
dict1.add(456, "21")
print(dict1.get(456))
print()

# Проверка присутствующего ключа
print(dict1.find(456))

# Проверка отсутствующего ключа
print(dict1.find(789))

# Извлечение значения по существующему ключу
print(dict1.get(456))
print(dict1.get(123))

# Извлечение значения по отсутствующему ключу
print(dict1.get(789))
print()

# Тест удаления
print("Удаляем ключ 123:")
print(dict1.remove(123))
print("После удаления:")
print(dict1.find(123))
print(dict1.get(123))
print()

# Тест удаления несуществующего ключа
print("Удаляем несуществующий ключ 999:")
print(dict1.remove(999))
print()