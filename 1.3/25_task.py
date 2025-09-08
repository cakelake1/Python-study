def S(massivea):
    B = []
    n = len(massivea)
    for i in range(n):
        for j in range(n - i):
            k = i + j
            max_value = max(massivea[j:k+1])
            B.append(max_value)
    return B
def TransformTransform(A, N):
    first_transform = S(A)
    transform_double = S(first_transform)
    result = sum(transform_double)
    return result % 2 == 0
