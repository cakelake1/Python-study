def MisterRobot(N, data):
    invers = 0
    even =(N % 2 == 1)
    if even:
        return True
    for i in range(N):
        for j in range(i+1,N):
            if data[i] > data[j]:
                invers +=1
    result = (invers % 2 == 0)
    return result