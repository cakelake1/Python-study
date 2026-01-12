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

# Добавление другого нового ключа

test_1.put("age", "21")
print(test_1.get('age'))
print()

# Проверка присутствующего ключа
print(test_1.is_key('age'))

# Проверка отсутствующего ключа
print(test_1.is_key('height'))

# Извлечение значения по существующему ключу
print(test_1.get('age'))
print(test_1.get('name'))

# Извлечение значения по отсутствующему ключу
print(test_1.get('height'))
