def ShopOLAP(N, items):
    dict_sales = {}
    for line in items:
        lines = line.split()
        value = int(lines[-1])
        key = ' '.join(lines[:-1]) 
        dict_sales[key] = dict_sales.get(key, 0) + value
    new_items = []
    for key,value in dict_sales.items():
        new_items.append((key,value))
    new_items = sorted(new_items, key=lambda x:(-x[1], x[0]))
    result = []
    for key,value in new_items:
        result.append(f"{key} {value}")
    return result