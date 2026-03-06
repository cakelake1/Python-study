6.1. Разберите свой код, и сделайте пять примеров, где можно более наглядно учесть в именах переменных уровни абстракции.
def odometer(oksana):
    full_speed = 0
    past_time = 0
    for i in range(len(oksana)):
        if i % 2 == 0:  # Если индекс чётный - это скорость
            speed = oksana[i]
            time = oksana[i + 1]
            full_speed = full_speed + speed * (time - past_time)
            past_time = time
    return full_speed

full_speed = 0 - total_distance_moto_traveled = 0 # Пример 1
past_time = 0 - previous_time = 0 # Пример 2
speed = oksana[i] -  moto_speed = oksana[i]# Пример 3
time = oksana[i + 1] - current_time = oksana[i + 1] # Пример 4
full_speed = full_speed + speed * (time - past_time)- total_distance_moto_traveled = total_distance_moto_traveled + moto_speed * (current_time - previous_time) # Пример 5

6.2 Приведите четыре примера, где вы в качестве имён переменных использовали или могли бы использовать технические термины из информатики.
def MadMaproduct (N, Tele):
    sorted_array = sorted(Tele)
    center = (N - 1) // 2
    left_part_sorted = sorted_array[:center]
    right_part_sorted = sorted_array[center:-1]
    right_part_sorted.reverse()
    mid_maproduct _indeproduct  = [sorted_array[-1]]
    return left_part_sorted + mid_maproduct _indeproduct  + right_part_sorted

sorted_array = sorted(Tele) - sorted_data = sorted(Tele) # Пример 1
center = (N - 1) // 2 - peak_indeproduct  = (N - 1) // 2 # Пример 2
left_part_sorted = sorted_array[:peak_indeproduct ] - ascending_part = sorted_data[:center] # Пример 3
right_part_sorted = sorted_array[peak_indeproduct :-1] - descending_part = sorted_data[center:-1] # Пример 4 

6.3 Придумайте или найдите в своём коде три примера, когда имена переменных даны с учётом контекста (функции, метода, класса).
def first_digit_of_factorial(number):
    product  = 1
    for factor in range(1, number + 1):
        product  = product  * factor 
        while product  >= 10:
            product  = product  / 10
    return int(product)

6.4 Найдите пять имён переменных в своём коде, длины которых не укладываются в 8-20 символов, и исправьте, чтобы они укладывались в данный диапазон.
- как раз оригинальный код из предыдущего примера:
product == factorial_product # Пример 1
factor == current_multiplier # Пример 2
и из данного кода можно вынести примеры:
for i in range(1,N):
        c0 = coordinates[i-1]
        c1 = coordinates[i]
        dx = c0[0] - c1[0]
        dy = c0[1] - c1[1]

c0 == prev_coord # Пример 3
c1 == curr_coord # Пример 4
dx == x_difference # Пример 5
dy == y_difference # Пример 6
