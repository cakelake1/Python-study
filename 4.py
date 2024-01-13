# Рефлексия:
# 5.1  Сделал поля приватными, методы видимо зря сделал приватными, но зато разобрался, как их также можно сделать приватными.
# 5.2 Задача выполнена, не нравится только, что кратко не получилось.

# 4.1
class Engine:
  def __init__(self, v, p, t):
    self.motortype = t # 1 - бензиновый, 2 дизельный, 3 гибридный
    self.volume = v # объем двигателя
    self.power = p # мощность двигателя

  def check_p(self, new_power):
      if new_power < 2000:
        self.power = 2000
  
class dvs(Engine):
    def __init__(self, v, p, t):
      super().__init__(v, p, t)

class hybrid(Engine):
    def __init__(self, v, p, t, em, b):
      self.electromotor = em
      self.battery = b
      super().__init__(v, p, t)
 
dvigv4 = dvs(1.6, 2000, 2)
dvigv6 = hybrid(1.6, 2000, 3, 3, 70000)
engines = [dvigv4, dvigv6]
for ani in engines:
  ani.check_p(1000)

class Car_Type: # Тип Автомобиля
  def __init__(self, n, m, t, s, engine:Engine):
    self.name = n # название модели автомобиля
    self.mass = m # масса автомобиля
    self.type = t #  тип авто : 1 - лимузин, 2 - универсал, 3 - спорткар, 4 - грузовой
    self.speed = s # Скорость автомобиля
    self.engine = engine
    
  def speed_change(self, new_speed):
    self.speed = new_speed
  def new_kinetic_energy(self):
    self.kinetic_energy = 0.5 * self.mass * (self.speed ** 2)
  def max_speed(self):
    self.speed = ((2 * self.engine.power) / self.mass) ** 0.5
    return self.speed 
    

class Car(Car_Type):
  def __init__(self, n, m, t, s, engine):
    super().__init__(n, m, t, s, engine)
    
class Truck(Car_Type):
  def __init__(self, n, m, t, s, engine, carrying, bw, bh, bl):
    self.body_width = bw
    self.body_height = bh
    self.body_lenght = bl
    self.carrying = carrying # Грузоподъемность
    super().__init__(n, m, t, s, engine)
    
MAN5 = Truck("МАН5", 8500, 4, 90, 3000, 10000, 2, 2, 3)
volvo_850 = Car("Вольво 850", 1000, 2, 100, 1000)
car_Types = [volvo_850]
for ani in car_Types:
    ani.speed_change(300)
print(MAN5.speed, volvo_850.speed)
MAN5.new_kinetic_energy()
print(MAN5.kinetic_energy)
e = Engine(1,666,1)
c = Car_Type('Porshe333',1,1,1, e)
c.max_speed()
print(c.max_speed())

# 4.2:
class Car_Type2: # Автомобиль
  def __init__(self, n, t, s,):
    self.name = n # название модели автомобиля
    self.type = t #  тип авто : 1 - лимузин, 2 - универсал, 3 - спорткар
    self.speed = s # Скорость автомобиля
  def speed_change(self, new_speed):
    self.speed = new_speed
  def foo(self,new_name):
    self.name = new_name
class Car2(Car_Type2):
  def __init__(self, n, t, s):
    super().__init__(n, t, s)
  def foo(self,new_name):
    self.name = "Уникальный Вольво"

class Truck2(Car_Type2):
  def __init__(self, n, t, s, carrying, bw, bh, bl):
    self.body_width = bw
    self.body_height = bh
    self.body_lenght = bl
    self.carrying = carrying # Грузоподъемность
    super().__init__(n, t, s)
    
  def foo(self,new_name):
    self.name = "Уникальный Порш 912"
  
MAN6 = Truck2("222", 3, 110, 9000,2 ,2 ,8 )
volvo_851 = Car2("333", 3, 300)
MAN6.foo("111")
volvo_851.foo("111")
print(MAN6.name, volvo_851.name)


import random
a = []
for i in range (0,500):
    if random.randint(0,1):
        new_obj = Volvo2("222", 3, 300)
    else:
        new_obj = Porshe2("222", 3, 300)
    a.append(new_obj)
for j in range (len(a)):
    a[j].foo
    print(a[j])

# Такой вывод, потому что мы хотим вывести объект, который состоит из ячеек памяти, и в каждой ячейке есть свое значение

# 4.3:
class Cat():
    def __init__(self, n):
        self.name = n
class Cyber_Cat():
    def __init__(self, n):
        self.name = n
cat1 = Cat("Tuzik")
cat2 = Cat("Grelka")
cat3 = Cyber_Cat(1)
cat4 = Cyber_Cat(2)
print(cat1.name + cat2.name)
print(cat3.name + cat4.name)
