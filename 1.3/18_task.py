def MisterRobot(N, data):
    invers = 0
    for i in range(N):
        for j in range(i+1,N):
            if data[i] > data[j]:
                invers +=1
    return invers % 2 == 0