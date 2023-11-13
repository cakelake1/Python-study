#Рефлексия:
    
# По моему решению видно, что с классами и методами задания я разобрался, но отсутствуют
# хоть какие-нибудь интересные условия на изменение значений в методах, да и в целом мое решение большое, понятное, но немного
#  бестолковое(в хорошем смысле), отсутствует оригинальность в классах и методах. Можно было бы сделать и проще, и интереснее. для решения задания 5.1 я возьму эталонное решение, а для 5.2 придумаю новое.
# 5.1 :
class Dwarf: # дварф

  def __init__(self, nam):
      self.__name = nam # имя
      self.__HP = 10; # здоровье, условные баллы
      self.__liters_drank = 0 # сколько выпито, литры
      self.startWork(0)

  def get_name(self):
      return self.__name

  def get_hp(self):
      return self.__HP

  def drink(self, liters):
      self.__liters_drank += liters
      if self.__liters_drank < 0:
          self.__liters_drank = 0
          
  def get_liters_drank(self):
      return self.__liters_drank

  def startWork(self, work):
      if work < 0 or work > 3:
          return
      self.__work_id = work # код текущей деятельности: 0-отдыхает, 1-выпивает, 
                       # 2-работает, 3-сражается

  def get_work(self):
      return self.__work_id                     

class Weapon: # оружие

    def __init__(self, knd):
        self.__kind = knd # код оружия: 1-меч, 2-лук, 3-посох
        if knd == 1:
            self.__name = "меч" # название
            self.__damage = 10 # сила поражения, баллы
            self.__range = 1 # дальность действия 
        elif knd == 2:
            self.__name = "лук"
            self.__damage = 2
            self.__range = 100
        elif knd == 3:
            self.__name = "посох"
            self.__damage = 4
            self.__range = 1

    # dist -- расстояние до цели
    def get_damage(self, dist):
        if dist < 0:
            return 0

        if self.__kind == 2 and dist > self.__range: 
            return 0 # цель вне диапазона поражения для лука

        if self.__kind == 2: 
           return (int)(self.__damage * (1 - dist * 1.0 / self.__range))

        if dist > 1:
            return 0 # для меча и посоха цель должна быть рядом
        return self.__damage
    
class Animal: # животное

  def __init__(self, nam, knd):
      self.__name = nam # кличка
      self.__kind = knd # вид животного: 0-кот, 1-пёс, 2-мул
      if knd == 0:
          self.__mass = 5 # масса существа, кг  
          self.__speed = 20 # скорость движения, км/ч
      elif knd == 1:
          self.__mass = 8 
          self.__speed = 30
      elif knd == 2:
          self.__mass = 250
          self.__speed = 3
  def get_name(self):
    return self.__name
  def eat(self):
      self.__mass += 0.5
  def get_eat(self):
      return self.__mass
dwarf_worker = Dwarf("Боб");
dwarf_worker.startWork(2)
dwarf_worker.drink(2.5);
print(dwarf_worker.get_name(), dwarf_worker.get_work(), dwarf_worker.get_liters_drank())

dog = Animal("Тузик", 1)
dog.eat()
print(dog.get_name(), dog.get_eat())

bow = Weapon(2)
print( bow.get_damage(40) )


# 5.2 :

class Car: # Автомобиль
  def __init__(self, n, t, s,):
    self.name = n # название модели автомобиля
    self.type = t #  тип авто : 1 - лимузин, 2 - универсал, 3 - спорткар
    self.speed = s # Скорость автомобиля
    if t == 1:
      self.speed = 100
      self.mass = 4
    elif t == 2:
      self.speed = 200
      self.mass = 3 
    elif t == 3:
      self.speed = 300
      self.mass = 1
  def massa_avto(self):
    self.mass += 0.25

class Volvo(Car):
  def __init__(self, n,t,s,gruz):
    super().__ini__(n,t,s)
    self.name = n
    self.type = 2
    self.speed = s
    self.weight = 2
    self.gruz = 1
  def fullspeed(self):
    self.speed /= self.weight
  def fullmassa(self):
    self.mass += self.gruz

class Porshe(Car):
  def __init__(self, n,t,s,aerod,loud):
    super().__init__(n,t,s)
    self.name = n
    self.type = 3
    self.aero = aerod
    self.speed = s
    self.loud = loud
  def rate(self,s):
    self.speed *= self.aero
  def volume(self,loud):
    self.loud += loud / self.speed

porshe_911 = Porshe("911", 3, 300, 0.2, 20)
porshe_911.rate(300)
porshe_911.volume(20)
print(porshe_911.speed, porshe_911.loud)

class Engine:
  def __init__(self, w, p):
    self.weight = w
    self.power = p
class v4(Engine):
  def __init__(self, w, p, light, cool):
    super().__init__(w, p)
    self.light = 0.6
    self.cool = 0.3
def volvo_v4(self):
    

    