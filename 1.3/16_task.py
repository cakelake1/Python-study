def MaximumDiscount(N, price):
    price.sort(reverse = True)
    result = 0
    for i in range(2,N,3):
        result +=price[i]
    return result