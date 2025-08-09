def UFO(N, data, octal):
    result = []
    while octal is True:
        for i in data:
            oct_number = int(str(i),8)
            result.append(oct_number)
        return result  
    while octal is False:
        for j in data:
            hex_number = int(str(j),16)
            result.append(hex_number)
        return result 