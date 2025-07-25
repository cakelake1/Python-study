def SumOfThe(N,data): 
    total = sum(data)
    result = 0
    for x in data:
        flag = (2 * x == total)
        result += x * flag
    return result