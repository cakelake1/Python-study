import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1
5.1
    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Индекс вне диапазона')
        if i == self.count:
            self.append(itm)
            return
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        
        for j in range(self.count-1, i-1,-1):
            self.array[j+1] = self.array[j]
        self.array[i] = itm
        self.count += 1
5.2
    def delete(self, i):
        self.__getitem__(i)
        for j in range(i, self.count - 1):
            self.array[j] = self.array[j+1]
        self.count -= 1
        if (self.count < self.capacity / 2) and self.capacity > 16:
            new_capacity = max(16, self.capacity // 2)
            self.resize(new_capacity)
5.3 Сложность обоих методов О(n) в худшем случае и О(1) в лучшем.
Рефлексия по предыдущей задаче
8. Функция суммирования двух связанных списков.
Два списка с исключением я не стал делать, а заранее отсортировал и сравнил поэлементно, минимальные значения из двух списков добавил в начало, все остальные в конец.

*5.5 Я делаю простую версию, где можно отследить, что при каждом добавлении в банк я прибавляю три монеты, вычитаю одну монету за каждое копирование и вычитаю за реолокацию каждые n монет.
import ctypes

class DynArrayBank:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)
        self.bank = 0  

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        if new_capacity < self.capacity:
            self.bank -= int(self.count * 0.1)  # 10%* N
        else:
            self.bank -= self.count
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        self.bank += 3  
        if self.count == self.capacity:
            self.bank -= self.count  
            self.resize(2 * self.capacity)
        self.bank -= 1  
        self.array[self.count] = itm
        self.count += 1

    def bank_info(self):
        print(f"count {self.count}, capacity {self.capacity}, BANK {self.bank}")
da = DynArrayBank()
for i in range(20):
    da.append(i)
    if i % 2 == 0:
        da.bank_info
da.bank_info()

 5.6 Затрудняюсь с этой задачей, возможно смогу увидеть подсказку в рефлексии, но я примерно представляю как ее решить  
Реализуйте многомерный динамический массив: произвольное количество измерений, при этом каждое измерение может внутри масштабироваться по потребности. В конструкторе задаётся число измерений и размер по каждому из них. Обращаться к такому массиву надо как к обычному многомерному, например: myArr[1,2,3].

# Рефлексия task1 *8
# Стоит немного подправить по подсказке, добавим исключение в проверку длин списка
def sum_linked_lists(list1, list2):
    if list1.len() != list2.len():
        raise ValueError("Списки имеют разную длинну")
    result = LinkedList()
    node1, node2 = list1.head, list2.head
    while node1:
        result.add_in_tail(Node(node1.value + node2.value))
        node1, node2 = node1.next, node2.next
    return result