import math
def TheRabbitsFoot(s, encode):
    while encode is True:
        s_no_space = s.replace(" ", "")
        N = len(s_no_space)
        matrix_row = math.isqrt(N)
        matrix_col = math.ceil(math.sqrt(N))
        while matrix_row * matrix_col < N:
            matrix_row += 1
        encryption_columns = []
        for j in range(matrix_col):
            col = []
            for i in range(matrix_row):
                index = i * matrix_col + j
                if index < N:
                    col.append(s_no_space[index])
            encryption_columns.append(''.join(col))
        return ' '.join(encryption_columns)
    while encode is False:
        groups = s.split()
        matrix_col = len(groups)
        matrix_row = max(len(group) for group in groups)
        decription_list = []
        for i in range(matrix_row):
            for j in range(matrix_col):
                if i < len(groups[j]):
                    decription_list.append(groups[j][i])
        return ''.join(decription_list)
