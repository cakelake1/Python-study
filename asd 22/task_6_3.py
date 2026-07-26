tree = BalancedBST()
# граничные значения - пустой массив и отрицательные значения
tree.GenerateTree([])
print(tree.Root, end=" ")  
print(tree.IsBalanced(tree.Root)) 
tree.GenerateTree([0, -5, 5, -10, -3, 3, 10])
print(tree.Root.NodeKey, end=" ")  
print(tree.Root.LeftChild.NodeKey, end=" ")  
print(tree.Root.RightChild.NodeKey, end=" ")
print(tree.Root.LeftChild.LeftChild.NodeKey, end=" ")  
print(tree.Root.LeftChild.RightChild.NodeKey, end=" ")  
print(tree.Root.RightChild.LeftChild.NodeKey, end=" ")  
print(tree.Root.RightChild.RightChild.NodeKey, end=" ")  
print(tree.IsBalanced(tree.Root))
print(tree.IsCorrectTree(tree.Root))  # 2* задание
print(tree.IsBalancdeCorrect(tree.Root))  # 3* задание   
# 0,1,2 глубина
tree.GenerateTree([42])
print(tree.Root.NodeKey,end=" ") 
print(tree.Root.Level, end=" ")
print(tree.Root.LeftChild, end=" ")
print(tree.Root.RightChild, end=" ")
print(tree.IsCorrectTree(tree.Root))  # 2* задание 
print(tree.IsBalanced(tree.Root))
print(tree.IsBalancdeCorrect(tree.Root))  # 3* задание  
tree.GenerateTree([10, 5, 15])
print(tree.Root.NodeKey,end=" ")
print(tree.Root.LeftChild.NodeKey,end=" ")
print(tree.Root.RightChild.NodeKey,end=" ")
print(tree.Root.LeftChild.Level,end=" ")
print(tree.Root.RightChild.Level,end=" ")
print(tree.IsBalanced(tree.Root))
print(tree.IsCorrectTree(tree.Root))  # 2* задание 
print(tree.IsBalancdeCorrect(tree.Root))  # 3* задание  
tree.GenerateTree([50, 25, 75, 12, 37, 62, 87])
print(tree.Root.NodeKey,end=" ")
print(tree.Root.LeftChild.NodeKey,end=" ")
print(tree.Root.RightChild.NodeKey,end=" ")
print(tree.Root.LeftChild.LeftChild.NodeKey,end=" ")
print(tree.Root.LeftChild.RightChild.NodeKey,end=" ")
print(tree.Root.RightChild.LeftChild.NodeKey,end=" ")
print(tree.Root.RightChild.RightChild.NodeKey,end=" ")
print(tree.IsBalanced(tree.Root))
print(tree.IsCorrectTree(tree.Root))  # 2* задание
print(tree.IsBalancdeCorrect(tree.Root))  # 3* задание
# без сортировки
tree.GenerateTree([10, 5, 15, 3, 7, 12, 18])
print(tree.Root.NodeKey,end=" ")
print(tree.Root.LeftChild.NodeKey,end=" ")
print(tree.Root.RightChild.NodeKey,end=" ")
print(tree.Root.LeftChild.LeftChild.NodeKey,end=" ")
print(tree.Root.LeftChild.RightChild.NodeKey,end=" ")
print(tree.Root.RightChild.LeftChild.NodeKey,end=" ")
print(tree.Root.RightChild.RightChild.NodeKey,end=" ")
print(tree.IsBalanced(tree.Root))
print(tree.IsCorrectTree(tree.Root))  # 2* задание
print(tree.IsBalancdeCorrect(tree.Root))  # 3* задание 
# дубликаты и одинаковые значения
tree.GenerateTree([3, 1, 3, 2, 1, 2, 3])
print(tree.Root.NodeKey,end=" ")
print(tree.Root.LeftChild.NodeKey,end=" ")
print(tree.Root.RightChild.NodeKey,end=" ")
print(tree.Root.LeftChild.LeftChild.NodeKey,end=" ")
print(tree.Root.LeftChild.RightChild.NodeKey,end=" ")
print(tree.Root.RightChild.LeftChild.NodeKey,end=" ")
print(tree.Root.RightChild.RightChild.NodeKey,end=" ")
print(tree.IsBalanced(tree.Root))
print(tree.IsCorrectTree(tree.Root))  # 2* задание 
print(tree.IsBalancdeCorrect(tree.Root))  # 3* задание  
tree.GenerateTree([5, 5, 5, 5, 5])
print(tree.Root.NodeKey,end=" ")
print(tree.Root.LeftChild.NodeKey,end=" ")
print(tree.Root.RightChild.NodeKey,end=" ")
print(tree.Root.LeftChild.RightChild.NodeKey,end=" ")
print(tree.Root.RightChild.RightChild.NodeKey,end=" ")
print(tree.IsBalanced(tree.Root))
print(tree.IsCorrectTree(tree.Root))  # 2* задание 
print(tree.IsBalancdeCorrect(tree.Root))  # 3* задание  
# проверка несбаланисрованного дерева
root = BSTNode(5, None)
root.LeftChild = BSTNode(3, root)
root.LeftChild.LeftChild = BSTNode(2, root.LeftChild)
root.LeftChild.LeftChild.LeftChild = BSTNode(1, root.LeftChild.LeftChild)
print(tree.IsBalanced(root))
print(tree.IsCorrectTree(root)) # 2* задание  
print(tree.IsBalancdeCorrect(root))  # 3* задание  