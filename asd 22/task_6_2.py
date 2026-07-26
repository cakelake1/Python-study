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
# конец рефлексии

#Задания:
# 2.* Добавьте метод проверки, действительно ли дерево получилось правильным
# дерево правильное, если:
#   1. ключ левого потомка меньше ключа родителя
#   2. ключ правого потомка больше или равен ключу родителя
def IsCorrectTree(self, root_node):
        if root_node is None:
            return True
        def rec_check(node):
            if node is None:
                return True
            if node.LeftChild is not None and node.LeftChild.NodeKey > node.NodeKey:
                    return False
            if node.RightChild is not None and node.RightChild.NodeKey < node.NodeKey:
                    return False
            left_side = rec_check(node.LeftChild)
            right_side = rec_check(node.RightChild)
            return left_side and right_side
        return rec_check(root_node)
# 3.* Добавьте метод проверки, действительно ли дерево получилось сбалансированным
# я думаю тут можно использовать проверку баланса поддеревьев частично с помощью основной проверки баланса всего дерева.
def IsBalancdeCorrect(self, root_node):
        if root_node is None:
            return True
        def get_depthTree(node):
            if node is None:
                return 0
            left_side = get_depthTree(node.LeftChild)
            right_side = get_depthTree(node.RightChild)
            result = 1 + max(left_side, right_side)
            return result
        left_depth = get_depthTree(root_node.LeftChild)
        right_depth = get_depthTree(root_node.RightChild)
        if abs(left_depth - right_depth) > 1:
            return False
        if not self.IsBalanced(root_node.LeftChild):
            return False
        if not self.IsBalanced(root_node.RightChild):
            return False
        return True