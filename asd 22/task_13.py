#Заключительное
# 12.1 Подсчитать общее число треугольников в графе.
# мой код рекомендациям не соответствует, испрвляем в несколько шагов
    # использовать счётчик для хранения треугольников.
    # далее нужно пройтись по всем узлам, проверить есть ли соседние узлы.
    # для каждый пары сдлеать проверку на соединение(1)
    # 
def CountTriangles(self):
    n = self.max_vertex
    count = 0
    for i in range(n):
        list_result = []
        for j in range(n):
            if self.m_adjacency[i][j] == 1:
                list_result.append(j)
        m = len(list_result)
        for k in range(m):
            for z in range(k + 1, m):
                u = list_result[k]
                v = list_result[z]
                if i < u and self.m_adjacency[u][v] == 1:
                    count += 1
    return count
# 12.2 Поиск узлов, не входящих ни в один треугольник в графе.
# мой код не соответствует рекомендациям
# беру предыдущий метод, добавляю туда список и отдельный метод с циклом делаю( с одним?)
# втором методе получаю список
# собираю все вершины, которые входят в треугольники и отбираю все, которых нет в списке треугольников.
def CountTrianglesList(self):
    n = self.max_vertex
    tr_list = []
    for i in range(n):
        list_result = []
        for j in range(n):
            if self.m_adjacency[i][j] == 1:
                list_result.append(j)
        m = len(list_result)
        for k in range(m):
            for z in range(k + 1, m):
                u = list_result[k]
                v = list_result[z]
                if i < u and self.m_adjacency[u][v] == 1:
                    tr_list.append((i,u,v))
    return tr_list
def NoOneWeakVertices(self):
    tr_list = self.CountTrianglesList()
    vertex_triangle = []
    for i in tr_list:
        for j in i:
            if j not in vertex_triangle:
                vertex_triangle.append(j)
    result = []
    for i, j in enumerate(self.vertex):
        if j is not None and i not in vertex_triangle:
            result.append(j)
    return result

