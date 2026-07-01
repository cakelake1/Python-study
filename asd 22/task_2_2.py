# Задания
#1.* Добавьте метод, проверяющий, идентично ли текущее дерево дереву-параметру.

def IsIdenticalTrees(self, new_tree):
        def recursive_idl(tree1, tree2):
            if tree1 is None or tree2 is None:
                return False
            if tree1.NodeKey != tree2.NodeKey or tree1.NodeValue != tree2.NodeValue:
                return False
            left_idl = recursive_idl(tree1.LeftChild, tree2.LeftChild)
            right_idl = recursive_idl(tree1.RightChild, tree2.RightChild)
            if left_idl and right_idl:
                return True
            else:
                return False
        return recursive_idl(self.Root, new_tree.Root)

#2.* Добавьте метод, который нахождит все пути от корня к листьям, длина которых равна заданной величине.
# Длина пути - количество ущлов - 1

def Paths(self, path_length):
        result = []
        def recursive_paths(node, cur_path):
            if node is None:
                return
            cur_path.append(node)
            if node.LeftChild is None and node.RightChild is None:
                if len(cur_path) - 1 == path_length:
                    result.append(cur_path.copy())
            recursive_paths(node.LeftChild, cur_path)
            recursive_paths(node.RightChild, cur_path)
            cur_path.pop()
        if self.Root is not None:
            recursive_paths(self.Root, []) 
        return result

#3.* Добавьте метод, который находит все пути от корня к листьям, чтобы сумма значений узлов на этом пути была максимальной.
# Посчитать количество путей с максимальной суммой

def CountMaxSumPaths(self):
        max_sum = float('-inf')
        count = 0
        def recursive_paths(node, cur_sum):
            nonlocal max_sum, count
            if node is None:
                return
            cur_sum += node.NodeValue
            if node.LeftChild is None and node.RightChild is None:
                if cur_sum > max_sum:
                    max_sum = cur_sum
                    count = 1
                elif cur_sum == max_sum:
                    count += 1
            recursive_paths(node.LeftChild, cur_sum)
            recursive_paths(node.RightChild, cur_sum)
        recursive_paths(self.Root, 0)
        return count

#4.* Добавьте метод проверки, симметрично ли дерево относительно своего корня.
# Правая и левая часть должны совпадать

def SymmTrees(self):
        def recursive_symm(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True
            if tree1.NodeKey != tree2.NodeKey or tree1.NodeValue != tree2.NodeValue:
                return False
            left_symm = recursive_symm(tree1.LeftChild, tree2.RightChild)
            right_symm = recursive_symm(tree1.RightChild, tree2.LeftChild)
            if left_symm and right_symm:
                return True
            else:
                return False
        return recursive_symm(self.Root.LeftChild, self.Root.RightChild)