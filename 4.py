# Рефлексия:
# 5.1  Сделал поля приватными, методы видимо зря сделал приватными, но зато разобрался, как их также можно сделать приватными.
# 5.2 Задача выполнена, не нравится только, что кратко не получилось.

# 4.1
class Engine:
  def __init__(self, v, p, t):
    self.motortype = t # 1 - бензиновый, 2 дизельный
    self.volume = v # объем двигателя
    self.power = p # мощность двигателя

  def check_p(self, new_power):
      if new_power < 2000:
        self.power = 2000
  
class v6(Engine):
    def __init__(self, v, p, t):
      super().__init__(v, p, t)

class v4(Engine):
    def __init__(self, v, p, t):
      super().__init__(v, p, t)
 
dvigv4 = v4(1.6, 2000, 2)
dvigv6 = v6(1.6, 2000, 1)
engines = [dvigv4, dvigv6]
for ani in engines:
  ani.check_p(1000)
class Car: # Автомобиль
  def __init__(self, n, m, t, s, engine:Engine):
    self.name = n # название модели автомобиля
    self.mass = m # масса автомобиля
    self.type = t #  тип авто : 1 - лимузин, 2 - универсал, 3 - спорткар
    self.speed = s # Скорость автомобиля
    self.engine = engine
    
  def speed_change(self, new_speed):
    self.speed = new_speed
  def new_kinetic_energy(self):
    self.kinetic_energy = 0.5 * self.mass * (self.speed ** 2)
  def max_speed(self):
    self.speed = ((2 * self.engine.power) / self.mass) ** 0.5
    return self.speed 
    

class Volvo(Car):
  def __init__(self, n, m, t, s, engine):
    super().__init__(n, m, t, s, engine)
    
class Porshe(Car):
  def __init__(self, n, m, t, s, engine):
    super().__init__(n, m, t, s, engine)
    
porshe_911 = Porshe("Порш 911", 85, 3, 190, 1000)
volvo_850 = Volvo("Вольво 850", 1000, 2, 100, 1000)
cars = [porshe_911, volvo_850]
for ani in cars:
    ani.speed_change(300)
print(porshe_911.speed, volvo_850.speed)
porshe_911.new_kinetic_energy()
print(porshe_911.kinetic_energy)
e = Engine(1,666,1)
c = Car('Porshe333',1,1,1, e)
c.max_speed()
print(c.max_speed())

# 4.2:
class Car2: # Автомобиль
  def __init__(self, n, t, s,):
    self.name = n # название модели автомобиля
    self.type = t #  тип авто : 1 - лимузин, 2 - универсал, 3 - спорткар
    self.speed = s # Скорость автомобиля
  def speed_change(self, new_speed):
    self.speed = new_speed
  def foo(self,new_name):
    self.name = new_name
class Volvo2(Car2):
  def __init__(self, n, t, s):
    super().__init__(n, t, s)
  def foo(self,new_name):
    self.name = "Уникальный Вольво"

class Porshe2(Car2):
  def __init__(self, n, t, s):
    super().__init__(n, t, s)
    
  def foo(self,new_name):
    self.name = "Уникальный Порш 912"
  
porshe_912 = Porshe2("222", 3, 300)
volvo_851 = Volvo2("333", 3, 300)
porshe_912.foo("111")
volvo_851.foo("111")
print(porshe_912.name, volvo_851.name)


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
