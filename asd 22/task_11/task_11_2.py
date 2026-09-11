#Рефлексия по 9 заданию:
#1. Лес из чётных деревьев, из которого удалено максимально возможное количество рёбер
    # исходя из рекоменлаций по текущему заданию могу выделить два момента:
        #1. Добавить проверку на четные вершины, если они такие, то сразу вывести пустой список.
        # 2. Можно уменьшить сложность, не проходить проходить каждый раз дерево, а пройти один раз и собрать ребра для удаления. 
        # 3. Для этого я немного меняю у себя два метода EvenTrees и CountTrees.
def EvenTrees(self):
        result = []
        even = self.CountTrees(self.Root, result)
        if even % 2 != 0:
               return []
        return result
def CountTrees(self,node, result):
        count = 1 
        for child in node.Children:
            count += self.CountTrees(child, result)
        if count % 2 == 0 and node.Parent is not None:
               result.append(node.Parent)
               result.append(node)
        return count