#Рефлексия по 9 заданию:
#9.1. Лес из чётных деревьев, из которого удалено максимально возможное количество рёбер
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
def CountTrees(self,node,result):
        count = 1 
        for child in node.Children:
            count += self.CountTrees(child, result)
        if count % 2 == 0 and node.Parent is not None:
               result.append(node.Parent)
               result.append(node)
        return count
# Сложность снизилась с O(n^2) до О(n), добавил в тесты проверку.
# *9.2 выполено корректно с рекурсией правой и левой половинами списка.
# *9.3 Для любого заданного узла определить общее количество чётных поддеревьев.
# ПО рекомендациям частично у меня правильно, остальной части нет. По сути нужен только один проход и вернуть размер наверх. ИСправляем:
def CountEven(self, node = None):
    if node is None:
        node = self.Root
    _size, count = self.CountEvenRecursive(node)
    return count
def CountEvenRecursive(self, node):
    size = 1
    count = 0
    for child in node.Children:
        s, c =  self.CountEvenRecursive(child)
        size += s
        count += c
    if size % 2 == 0:
        count += 1
    return size, count

# *11.2 Используя BFS, найдите два наиболее удалённых друг от друга узла
from collections import deque
def FindFarthestWay(self):
        VFrom = self._first_vertex()
        if VFrom == -1:
            return 0
        farthest_from_start, _ = self._bfsFarthest(VFrom)
        _, diameter = self._bfsFarthest(farthest_from_start)
        return diameter
def _first_vertex(self):
    for i in range(self.max_vertex):
        if self.vertex[i] is not None:
            return i
    return -1
def _bfsFarthest(self, VFrom):
    self._vertex_unvisited()
    self.vertex[VFrom].Hit = True
    i_deq = deque([[VFrom, 0]])
    return self._bfsFarthestRec(VFrom, 0, i_deq)
def _bfsFarthestRec(self, farthest_idx, farthest_dist, deq):
    if not deq:
        return farthest_idx, farthest_dist
    cur_idx, cur_dist = deq.popleft()
    if cur_dist > farthest_dist:
        farthest_dist = cur_dist
        farthest_idx = cur_idx
    for nearby_idx in range(self.max_vertex):
        if not self.m_adjacency[cur_idx][nearby_idx]:
            continue
        if self.vertex[nearby_idx].Hit:
            continue
        self.vertex[nearby_idx].Hit = True
        deq.append([nearby_idx, cur_dist + 1])
    return self._bfsFarthestRec(farthest_idx, farthest_dist, deq)



# *11.3 Добавьте метод, который находит все циклы в текущем (неориентированном) графе с использованием BFS
def FindAllresult(self):
    result = []
    for VFrom in range(self.max_vertex):
        if self.vertex[VFrom] is None:
            continue
        self._vertex_unvisited()
        parent = [-1] * self.max_vertex
        self.vertex[VFrom].Hit = True
        i_deq = deque([VFrom])
        while i_deq:
            cur_idx = i_deq.popleft()
            for nearby_idx in range(self.max_vertex):
                if not self.m_adjacency[cur_idx][nearby_idx]:
                    continue
                if not self.vertex[nearby_idx].Hit:
                    self.vertex[nearby_idx].Hit = True
                    parent[nearby_idx] = cur_idx
                    i_deq.append(nearby_idx)
                    continue
                if parent[cur_idx] == nearby_idx:
                    continue
                path = set()
                u, v = cur_idx, nearby_idx
                while u != -1:
                    path.add((min(u, parent[u]), max(u, parent[u])))
                    u = parent[u]
                while v != -1 and v not in path:
                    path.add((min(v, parent[v]), max(v, parent[v])))
                    v = parent[v]
                cycle = list(path)
                if cycle not in result:
                    result.append(cycle)
        return result
