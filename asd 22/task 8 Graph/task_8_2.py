#Рефлексия по 6 задаче
#2. Проверка, правильно ли распределены значения в двоичном дереве.
#По все пунктам из рекомендаций, код подходит
#3. Проверка, сбалансировано ли двоичное дерево .
# по всем пунктам из рекомендаций прошелся - все хорошо.


# 2*Реализуйте направленный граф, представленный матрицей смежности, и добавьте метод проверки, будет ли он циклическим.
def DirectedGraph(self):
        result = []
        for i in range(self.max_vertex):
             if self.vertex[i] is not None and not self.CheckDirGraph(i):
                result.append(self.vertex[i])
        return result

def CheckDirGraph(self, check_index):
    directed = []
    for i in range(self.max_vertex):
        if self.m_adjacency[check_index][i] == 1 and self.vertex[i] is not None:
            directed.append(i)
    for i in range(len(directed)):
        for j in range(i + 1, len(directed)):
            if self.m_adjacency[directed[i]][directed[j]] == 1:
                return True
    return False