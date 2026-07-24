# Рефлексия
# 4.2 Поиск наименьшего общего предка (LCA). Напишите метод, который находит наименьшего общего предка двух узлов в текущем дереве, представленном в виде массива. 
# Я сделал не рекурсивно, исправим:
def LCA(self, key1, key2):
        def recursive_LCA(idx):
            if self.Tree[idx] is None:
                 return None
            if self.Tree[idx] == key1 or self.Tree[idx] == key2:
                  return self.Tree[idx]
            left = recursive_LCA(2 * idx + 1)
            right = recursive_LCA(2 * idx + 2)
            if left is not None and right is not None:
                return self.Tree[idx]
            if left is not None:
                return left
            if right is not None:
                return right
            return None
        return recursive_LCA(0)

# 3. Оптимизированный метод обхода дерева в ширину.
# мой метод просто проходит по индексам, а не по узлам дерева, не является сетодом обхода в ширену, переделаю:
def WideMethod(self):
    if not self.Tree:
        return None
    result = []
    queue = [0]
    head = 0
    while head < len(queue):
        idx = queue[head]
        head += 1
        if self.Tree[idx] is not None:
            result.append(self.Tree[idx])
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left < len(self.Tree):
                queue.append(left)
            if right < len(self.Tree):
                queue.append(right)
    return result