#3Реализуйте алгоритм инвертирования дерева: надо сделать так, чтобы слева от главного узла были значения больше него, а справа — меньше.
#

def InvertTreeNode(self):
        def rec_invert(node):
            if node is None:
                return
            rec_invert(node.LeftChild)
            rec_invert(node.RightChild)
            node.LeftChild, node.RightChild = node.RightChild, node.LeftChild
            if node.LeftChild is not None:
                node.LeftChild.Parent = node
            if node.RightChild is not None:
                node.RightChild.Parent = node
        rec_invert(self.Root)
        return self.Root
#4.* Добавьте метод, который находит уровень в текущем дереве, сумма значений узлов на котором максимальна. Подумайте, как оптимизировать решение, чтобы производительность была достаточной даже для больших деревьев.
def FindLevelMaxSum(self):
        cur_level = [self.Root]
        level = 0
        max_sum = float('-inf')
        max_level = 0
        while cur_level:
            level_sum = sum(node.NodeValue for node in cur_level)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            level_up = []
            for node in cur_level:
                if node.LeftChild is not None:
                    level_up.append(node.LeftChild)
                if node.RightChild is not None:
                    level_up.append(node.RightChild)
            cur_level = level_up
            level += 1
        return max_level, max_sum
# для оптимизации можно из двух циклов сделать один. Для дерева на 100-200 узлов разницы почти не будет, для 50000 и выше уже будет заметно.
#  
#5.* Учитывая результаты обхода дерева в префиксном и инфиксном порядке, разработайте функцию для восстановления оригинального дерева.
#Например,
#префиксный массив: [1,2,4,5,3,6,7] preorder
#инфиксный массив: [4,2,5,1,6,3,7] inorder
# нужно взять первый элемент preorder -корень
# левое дерево - все индексы до корня в Inorder, правое после корня.
# потом через срезы вытащить правое и левое дерево в preorder

def CreateTreeinpreorder(preorder, inorder):
    if not preorder or not inorder:
        return None
    main_root = preorder[0]
    root = BSTNode(main_root,'main_root', None)
    index_root = inorder.index(main_root)
    left_inorder = inorder[:index_root]
    right_inorder = inorder[index_root + 1:]
    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]
    root.LeftChild = CreateTreeinpreorder(left_preorder, left_inorder)
    root.RightChild = CreateTreeinpreorder(right_preorder, right_inorder)
    if root.LeftChild is not None:
        root.LeftChild.Parent = root
    if root.RightChild is not None:
        root.RightChild.Parent = root
    return root
#Объясните, почему обязательно нужны оба обхода для однозначного построения дерева.
# Префиксный подход показывает поочередность позиции узлов, а инфиксный показывает расположение слева или справа
# только с одним обходом у нас не будет полной информации, наример префиксный может быть
# 1-2-3 в очередь справа
# или  1
#    2   3
# вот как раз инфиксный обход нам укажет расположение, относительно корня.