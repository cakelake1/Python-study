# Рефлексия:

#3. Алгоритм инвертирования дерева.
# Испошльзовал рекурсивное инфвертирование post order - корректно

#4.Ищем уровень в дереве, сумма значений узлов на котором максимальна.
# Как я и предполагал нужно сделать из двух циклов - один:
def FindLevelMaxSum(self):
        cur_level = [self.Root]
        level = 0
        max_sum = float('-inf')
        max_level = 0
        while cur_level:
            level_sum = 0
            level_up = []
            for node in cur_level:
                level_sum += node.NodeValue
                if node.LeftChild is not None:
                    level_up.append(node.LeftChild)
                if node.RightChild is not None:
                    level_up.append(node.RightChild)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            cur_level = level_up
            level += 1
        return max_level, max_sum

#5. Восстановление оригинального дерева по префиксу и инфиксу.
# выполнил правильно, исходя из рекомендаций код работает корректно только для уникальных значений.