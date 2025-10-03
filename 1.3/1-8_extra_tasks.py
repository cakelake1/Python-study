def exponentiation(n,m):
    if m == 0:
        return 1
    else:
        return n * (exponentiation(n, m-1))
print(exponentiation(2,3)) # 8
print(exponentiation(2,10)) # 1024
print(exponentiation(3,10)) # 59049
print(exponentiation(3,0)) # 1
print(exponentiation(1.1414,2)) # 1.30279396
