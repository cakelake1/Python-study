from task_9 import SimpleTree, SimpleTreeNode
from task_9_2 import EvenBinaryTreeBalance,CheckOrder,BuildBalance,CountEven,CountEvenRecursive
SimpleTree.EvenBinaryTreeBalance = EvenBinaryTreeBalance
SimpleTree.CheckOrder = CheckOrder
SimpleTree.BuildBalance = BuildBalance
SimpleTree.CountEven = CountEven
SimpleTree.CountEvenRecursive = CountEvenRecursive

# Дерево с 6 вершинами    
root = SimpleTreeNode(1, None)
tree = SimpleTree(root)
node2 = SimpleTreeNode(2, root)
node3 = SimpleTreeNode(3, root)
root.Children = [node2, node3]
node4 = SimpleTreeNode(4, node2)
node5 = SimpleTreeNode(5, node2)
node2.Children = [node4, node5]
node6 = SimpleTreeNode(6, node3)
node3.Children = [node6]
# Подсчёт вершин
print(tree.Count(), end=" ")
edges = tree.EvenTrees()
print(len(edges), end=" ")
if len(edges) >= 2:
    print(edges[0].NodeValue, end=" ")
    print(edges[1].NodeValue)

# граничные случаи, 1 вершина и 0 вершин
root = SimpleTreeNode(10, None)
tree = SimpleTree(root)
print(tree.CountTrees(root))
root = SimpleTreeNode(None, None)
tree = SimpleTree(root)
print(tree.CountTrees(root))
result = []
tree.EvenFunc(root, result)
print(len(result))  # 0
# дерево с 2 вершинами
root = SimpleTreeNode(1, None)
tree = SimpleTree(root)
node2 = SimpleTreeNode(2, root)
root.Children = [node2]
result = []
tree.EvenFunc(root, result)
if len(result) >= 2:
    print(len(result), end=" ")  # 2
    print(result[0].NodeValue, end=" ")  # 1
    print(result[1].NodeValue)  # 2
else:
    print(len(result))
#2.* Добавьте метод, который сбалансирует чётное двоичное дерево.
def showtest(node, level = 0):
    print("  " * level + str(node.NodeValue))
    for child in node.Children:
        showtest(child, level + 1)
root = SimpleTreeNode(1, None)
tree = SimpleTree(root)
n2 = SimpleTreeNode(2, root)
n3 = SimpleTreeNode(3, root)
n4 = SimpleTreeNode(4, n2)
root.Children = [n2, n3]
n2.Children = [n4]
showtest(root)
tree.EvenBinaryTreeBalance()
showtest(tree.Root)
# 3.* Добавьте метод, который для любого заданного подузла текущего дерева определит общее количество чётных поддеревьев.
root2 = SimpleTreeNode(1, None)
tree2 = SimpleTree(root2)
node2 = SimpleTreeNode(2, root2)
node3 = SimpleTreeNode(3, root2)
node4 = SimpleTreeNode(4, node2)
node5 = SimpleTreeNode(5, node2)
node6 = SimpleTreeNode(6, node3)
node7 = SimpleTreeNode(7, node4)
node8 = SimpleTreeNode(8, node4)
root2.Children = [node2, node3]
node2.Children = [node4, node5]
node3.Children = [node6]
node4.Children = [node7, node8]
showtest(root2)
print(tree2.CountEven())
print(tree2.CountEven(node2))
print(tree2.CountEven(node3))
print(tree2.CountEven(node4))
print(tree2.CountEven(node5))
print(tree2.CountEven(node6))