class aBST:

    def __init__(self, depth):
        tree_size = (2 ** (depth+1)) - 1
        self.Tree = [None] * tree_size
        self.depth = depth
	
    def FindKeyIndex(self, key):
        if self.Tree[0] is None:
            return None
        idx = 0
        while idx < len(self.Tree):
            if self.Tree[idx] is None:
                return -idx
            elif self.Tree[idx] == key:
                return idx
            elif key < self.Tree[idx]:
                idx = 2 * idx + 1
            else:
                idx = 2 * idx + 2
        return None
	
    def AddKey(self, key):
        if self.Tree[0] is None:
            self.Tree[0] = key
            return 0
        idx = 0
        while idx < len(self.Tree):
            if self.Tree[idx] is None:
                self.Tree[idx] = key
                return idx
            elif self.Tree[idx] == key:
                return idx
            elif key < self.Tree[idx]:
                idx = 2 * idx + 1
            else:
                idx = 2 * idx + 2
        return -1;

    def WideMethod(self):
        result = []
        for i in range(len(self.Tree)):
            if self.Tree[i] is not None:
                result.append(self.Tree[i])
        return result
    
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
        
# 1. Заполните полностью дерево глубины N значениями и проверьте тестами работу функций добавления и поиска, а также корректность значений в массиве, реализующем дерево.
# Проверим корректность значений на глубине 0,1,2,3, на гkубине 3 проверим добавление и поиск.
tree_0_depth = aBST(0) # 0 глубина
print(len(tree_0_depth.Tree)) # 1
index_d1 = tree_0_depth.AddKey(42)
print(index_d1) # 0
print(tree_0_depth.Tree) # 42
tree_1_depth = aBST(1) # 1 глубина
print(len(tree_1_depth.Tree)) # 3
tree_1_depth.AddKey(10)
tree_1_depth.AddKey(5)
tree_1_depth.AddKey(15)
print(tree_1_depth.Tree) # Выше
tree_2_depth = aBST(2) # 2 глубина
print(len(tree_2_depth.Tree)) # 7
tree_2_depth.AddKey(50)
tree_2_depth.AddKey(25)
tree_2_depth.AddKey(75)
tree_2_depth.AddKey(12)
tree_2_depth.AddKey(37)
tree_2_depth.AddKey(62)
tree_2_depth.AddKey(87)
print(tree_2_depth.Tree)
tree_3_depth = aBST(3) # 3 глубина
print(len(tree_3_depth.Tree)) # 15
tree_3_depth.AddKey(50) # 0
tree_3_depth.AddKey(25)
tree_3_depth.AddKey(75)
tree_3_depth.AddKey(12)
tree_3_depth.AddKey(37)
tree_3_depth.AddKey(62)
tree_3_depth.AddKey(87)
tree_3_depth.AddKey(6)
tree_3_depth.AddKey(18)
tree_3_depth.AddKey(31) # 9
tree_3_depth.AddKey(43)
tree_3_depth.AddKey(56)
tree_3_depth.AddKey(68)
tree_3_depth.AddKey(81)
tree_3_depth.AddKey(93)
print(tree_3_depth.Tree) # up

# поиск

print(tree_3_depth.FindKeyIndex(50)) # 0
print(tree_3_depth.FindKeyIndex(31)) # 9
print(tree_3_depth.FindKeyIndex(100)) # не должно быть
print(tree_3_depth.FindKeyIndex(1)) # не должно быть

# добавление сушествующего значения
print(tree_3_depth.AddKey(50)) # 0
print(tree_3_depth.AddKey(31)) # 9
# добавление в полное дерево
print(tree_3_depth.AddKey(94)) # -1
print(tree_3_depth.Tree) # up бех изменнений
# поиск в пустом дереве
tree_empty = aBST(2)
print(tree_empty.FindKeyIndex(10)) # none
# проверка глубины по значению 
print(len(aBST(0).Tree))
print(len(aBST(1).Tree))
print(len(aBST(2).Tree))
print(len(aBST(3).Tree))
print(len(aBST(4).Tree))
print(len(aBST(5).Tree))
# дерево с отрицательными и нулевыми значениями
tree_zero_minus = aBST(2)
tree_zero_minus.AddKey(0)
tree_zero_minus.AddKey(-5)
tree_zero_minus.AddKey(5)
tree_zero_minus.AddKey(-10)
tree_zero_minus.AddKey(-3)
tree_zero_minus.AddKey(3)
tree_zero_minus.AddKey(10)
print(tree_zero_minus.Tree)

#3. Переделайте метод обход дерева в ширину, оптимизируя его за счёт прямого доступа к элементам массива.\
# Обойдем наши деревья разной глубины, затем неполное дерево, пустое дерево и с отриц значениями
print(tree_0_depth.WideMethod()) # 42
print(tree_1_depth.WideMethod()) # [10, 5, 15]
print(tree_2_depth.WideMethod()) # [50, 25, 75, 12, 37, 62, 87]
print(tree_3_depth.WideMethod()) # [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93]
print(tree_zero_minus.WideMethod()) # [0, -5, 5, -10, -3, 3, 10]
print(tree_empty.WideMethod()) # []
tree_miss_elements = aBST(2)
tree_miss_elements.AddKey(10)
tree_miss_elements.AddKey(5)
tree_miss_elements.AddKey(15)
tree_miss_elements.AddKey(3)
tree_miss_elements.AddKey(7)
print(tree_miss_elements.Tree) # [10, 5, 15, 3, 7, None, None]
print(tree_miss_elements.WideMethod()) # [10, 5, 15, 3, 7]

# Тест  Поиск наименьшего общего предка (LCA).
# Проверим на разных глубинах, с несуществующими ключами и на пустом дереве
# 0 глубина
print(tree_0_depth.LCA(42,42))  # 42
# несуществубшие ключи
print(tree_0_depth.LCA(42,12))  # NOne
print(tree_0_depth.LCA(24,23))  # NONE
# 1 глубина
print(tree_1_depth.LCA(5,15))  # 10
print(tree_1_depth.LCA(10,5)) # 10
# 2 глубина
print(tree_2_depth.LCA(25,75)) # 50
print(tree_2_depth.LCA(12,37)) # 25
# 3
print(tree_3_depth.LCA(6,18)) # 12 В левой части
print(tree_3_depth.LCA(6,31)) # 25 В левой части
print(tree_3_depth.LCA(81, 93))  # 87 в правой части
print(tree_3_depth.LCA(68, 81))  # 75 в правой части
print(tree_3_depth.LCA(18, 56))  # 50 между левой и правой частями
print(tree_3_depth.LCA(31, 68))  # 50 между левой и правой частями
# тест в неполном дереве [10, 5, 15, 3, 7, None, None]
print(tree_miss_elements.LCA(3, 7))    # 5
print(tree_miss_elements.LCA(3, 15))  # 10
print(tree_miss_elements.LCA(5, 7))    # 5
print(tree_miss_elements.LCA(5, 15)) # 10
