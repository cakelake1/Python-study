# Рефлексия по 10 заданию:
# 10.1. Будет ли неориентированный граф связным.
# как раз тут я не был до конца уверен, но выполнено все правильно
#10.2.Cамый длинный путь в ориентированном графе с циклами.
# решение верное
from itertools import combinations
# 12.1* Добавьте метод, подсчитывающий общее число треугольников в графе.
def CountTriangles(self):
        return self._count_triangles_recursive(0, [])
def _count_triangles_recursive(self, start, end):
    if len(end) == 3:
        a, b, c = end
        if (self.m_adjacency[a][b] == 1 and self.m_adjacency[a][c] == 1 and self.m_adjacency[b][c] == 1):
            return 1
        return 0
    count = 0
    for i in range(start, self.max_vertex):
        if self.vertex[i] is None:
            continue
        count += self._count_triangles_recursive(i + 1, end + [i])
    return count

# 12.2.* Реализуйте метод поиска узлов, не входящих ни в один треугольник в графе
def NoOneWeakVertices(self):
    result = []
    for i, node in enumerate(self.vertex):
        if node is None:
            continue
        list_result = []
        for j in range(self.max_vertex):
            if self.IsEdge(i, j):
                list_result.append(j)
        in_triangle = False
        for a, b in combinations(list_result, 2):
            if self.IsEdge(a, b):
                in_triangle = True
                break
        if not in_triangle:
            result.append(node)
    return result