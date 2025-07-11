def squirrel(N):
    #if N == 0:
        #return 1
    x = 1
    for i in range(1, N + 1):
        x = x * i
        while x >= 10:
            x = x / 10
    return int(x)
# Ввод значения и вызов функции
if __name__ == '__main__':
    N = int(input("Введите число N: "))
    print(squirrel(N))