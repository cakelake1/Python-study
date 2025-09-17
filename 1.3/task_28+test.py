""" Мастер ключей
заключительное
По совету Оракула, Нео освобождает из замка Меровингена системную программу-изгнанника -- Мастера ключей. Только Мастер ключей поможет Избранному найти Архитектора и положить конец войне.
Однако у них совсем мало времени -- армия Агентов Смитов уже совсем близко. Нео требуется знать лишь набор секретных дверей, но они будут выявлены только после того, как Мастер ключей будет открывать и закрывать двери по определённому алгоритму.
Помогите Избранному -- вычислите заранее двери, которые будут открыты по окончании работы Мастера ключей.
Имеется k дверей (например, массив из k логических элементов). Каждая дверь может быть либо открыта, либо закрыта. Исходно все двери закрыты.
Мастер ключей выполняет k манипуляций над дверями. На первом шаге он открывает все двери. На втором шаге он закрывает каждую вторую дверь. На третьем шаге он проверяет каждую третью дверь, открывает её если она закрыта, и закрывает если открыта.
Далее, на n-м шаге он таким образом "переключает" каждую n-ю дверь.
Соответственно, на последнем шаге n=k он "переключит" только самую последнюю дверь. Нео должен знать, сколько и каких дверей после k таких манипуляций будут открыты.
Задание.
1. Напишите программу, которая моделирует работу Мастера ключей.
2. Поэкспериментируйте с разными значениями k, постарайтесь выявить закономерность, от чего зависят номера открытых дверей.
3. Попробуйте объяснить эту закономерность математически.
Пункты 2 и 3 расскажите преподавателю в чате (бонус до +1000 золотых).
Функция
string Keymaker(int k)
получает на вход количество дверей k и возвращает строку длиной k символов, где 1 в i-й позиции означает открытую i-ю дверь, а 0 -- закрытую i-ю дверь.
как постить решение
 """
def Keymaker(k):
    doors = ["0"] * k
    for i in range(1, k + 1):
        for j in range(i - 1, k , i):
            if doors[j] == '0':
                doors[j] = '1'
            else:
                doors[j] = '0'
    return ''.join(doors)
print(Keymaker(1))
print(Keymaker(2))
print(Keymaker(3))
print(Keymaker(4))
print(Keymaker(5))
print(Keymaker(6))
print(Keymaker(7))
print(Keymaker(8))
print(Keymaker(9))
print(Keymaker(10))
print(Keymaker(11))
print(Keymaker(12))
print(Keymaker(13))
print(Keymaker(14))
print(Keymaker(15))
print(Keymaker(16))
print(Keymaker(17))
print(Keymaker(18))
print(Keymaker(19))
print(Keymaker(20))
print(Keymaker(21))
print(Keymaker(22))
print(Keymaker(23))
print(Keymaker(24))
print(Keymaker(25))
print(Keymaker(26))
print(Keymaker(27))
print(Keymaker(28))
print(Keymaker(29))
print(Keymaker(30))
print(Keymaker(31))
print(Keymaker(32))
print(Keymaker(33))
print(Keymaker(34))
print(Keymaker(35))
print(Keymaker(36))
print(Keymaker(37))
print(Keymaker(38))
print(Keymaker(39))
print(Keymaker(40))
print(Keymaker(41))
print(Keymaker(42))
print(Keymaker(43))
print(Keymaker(44))
print(Keymaker(45))
print(Keymaker(46))
print(Keymaker(47))
print(Keymaker(48))
print(Keymaker(49))
print(Keymaker(50))
print(Keymaker(51))
print(Keymaker(52))
print(Keymaker(53))
print(Keymaker(54))
print(Keymaker(55))
print(Keymaker(56))
print(Keymaker(57))
print(Keymaker(58))
print(Keymaker(59))
print(Keymaker(60))
print(Keymaker(61))
print(Keymaker(62))
print(Keymaker(63))
print(Keymaker(64))
print(Keymaker(65))
print(Keymaker(66))
print(Keymaker(67))
print(Keymaker(68))
print(Keymaker(69))
print(Keymaker(70))
print(Keymaker(71))
print(Keymaker(72))
print(Keymaker(73))
print(Keymaker(74))
print(Keymaker(75))
print(Keymaker(76))
print(Keymaker(77))
print(Keymaker(78))
print(Keymaker(79))
print(Keymaker(80))
print(Keymaker(81))
print(Keymaker(82))
print(Keymaker(83))
print(Keymaker(84))
print(Keymaker(85))
print(Keymaker(86))
print(Keymaker(87))
print(Keymaker(88))
print(Keymaker(89))
print(Keymaker(90))
print(Keymaker(91))
print(Keymaker(92))
print(Keymaker(93))
print(Keymaker(94))
print(Keymaker(95))
print(Keymaker(96))
print(Keymaker(97))
print(Keymaker(98))
print(Keymaker(99))
print(Keymaker(100))
 