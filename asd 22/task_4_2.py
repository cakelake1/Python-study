# Рефлексия. 
# Рекомендации
#2. Метод, который нахождит все пути от корня к листьям, длина которых равна заданной величине.
#3. Метод, который находит все пути от корня к листьям, чтобы сумма значений узлов на этом пути была максимальной.
#Можно (лучше) в подобных случаях объединить обе проверки в один рекурсивный алгоритм обхода дерева, а логику конкретных проверок делегируем автономным функциям (передаются этому алгоритму как параметры, если язык программирования это позволяет). Такой паттерн называется параморфизм.

#Выводы
# Значит мне нужно сделать отдельный метод, назовем его walk,который будет присутствовать в двух методах выше
# узнаем,  что параморфизм также является аккумулятором (acc) в параметрах
#добавляем метод
def walk(self, fn, acc=None):
    def dfs(node, path, acc):
        if node is None:
            return acc
        path.append(node)
        if node.LeftChild is None and node.RightChild is None:
            acc = fn(node, path.copy(), acc)
        else:
            acc = dfs(node.LeftChild, path, acc)
            acc = dfs(node.RightChild, path, acc)
        path.pop()
        return acc
    if self.Root is not None:
        return dfs(self.Root, [], acc)
    return acc

# добавляю метод walk в свое решение:
def Paths(self, path_length):
    result = []
    def check_sum(node, path, acc):
        if len(path) - 1 == path_length:
            acc.append(path)
        return acc
    self.walk(check_sum, result)
    return result

def CountMaxSumPaths(self):
    max_sum = float('-inf')
    count = 0
    def calc_sum(node, path, acc):
        nonlocal max_sum, count
        cur_sum = 0
        for n in path:
            cur_sum += n.NodeValue
        if cur_sum > max_sum:
            max_sum = cur_sum
            count = 1
        elif cur_sum == max_sum:
            count += 1
        return acc
    self.walk(calc_sum, None)
    return count

# 4. Симметрично ли дерево относительно своего корня.
# Рекомендации:
#Рекурсивно сравниваем левое поддерево текущего узла с правым поддеревом соседнего узла, и наоборот. - Сравнил
#Проверяем также зеркальность расположения узлов по их значениям. - проверил
#Если у дерева корень с одним узлом, оно считается несимметричным. - не добавил проверку на дерево с одним корнем
# достаточно добавить такую проверку:
if self.Root.LeftChild is None or self.Root.RightChild is None:
    return False
# Если хоть одного узла нет - дерево нессиметрично


#2.* Поиск наименьшего общего предка (LCA). Напишите метод, который находит наименьшего общего предка двух узлов в текущем дереве, представленном в виде массива. 
def LCA(self, key1, key2):
        idx_1 = self.FindKeyIndex(key1)
        idx_2 = self.FindKeyIndex(key2)
        if idx_1 is None or idx_2 is None or idx_1 < 0 or idx_2 < 0:
            return None
        while idx_1 != idx_2:
            if idx_1 > idx_2:
                idx_1 = (idx_1 - 1 ) // 2
            else:
                idx_2 = (idx_2 - 1) // 2
        return self.Tree[idx_1]

#Объясните, как индексы в массиве могут быть использованы для упрощения поиска, по сравнению с классической рекурсивной реализацией.

# Индексы в массиве итеративны и легче для понимания, чем рекурсная реализация(уменьшается время понимания кода =))
# Вычисление происходит моментально, в рекурсии нужжно обойти в глубину все дерево.
# и конечно сам поиск упрощается за счёт уменьшения сложности O(n) - рекурсия, О(log n) - поиск индекса в массиве.

# 3 задание без *, но по логике его также нужно сюда добавить
# Переделайте метод обход дерева в ширину, оптимизируя его за счёт прямого доступа к элементам массива.
def WideMethod(self):
        result = []
        for i in range(len(self.Tree)):
            if self.Tree[i] is not None:
                result.append(self.Tree[i])
        return result