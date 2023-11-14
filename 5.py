#Рефлексия:
# Заново вчитался в задание и увидел, что изначально я сделал не три класса, а только два.    
# По моему решению видно, что с классами и методами задания я разобрался, но отсутствуют
# хоть какие-нибудь интересные условия на изменение значений в методах, да и в целом мое решение большое, понятное, но немного
#  бестолковое(в хорошем смысле), отсутствует оригинальность и дополнительные интересные условия в классах и методах. Можно было бы сделать и проще, и интереснее. Для решения задания 5.1 я использую эталонное решение, а для 5.2 придумаю новое.
# 5.1 :
class Dwarf: # дварф

  def __init__(self, nam):
      self.__name = nam # имя
      self.__HP = 10; # здоровье, условные баллы
      self.__liters_drank = 0 # сколько выпито, литры
      self.__startWork__(0)

  def __get_name__(self):
      return self.__name

  def __get_hp__(self):
      return self.__HP

  def __drink__(self, liters):
      self.__liters_drank += liters
      if self.__liters_drank < 0:
          self.__liters_drank = 0
          
  def __get_liters_drank__(self):
      return self.__liters_drank

  def __startWork__(self, work):
      if work < 0 or work > 3:
          return
      self.__work_id = work # код текущей деятельности: 0-отдыхает, 1-выпивает, 
                       # 2-работает, 3-сражается

  def __get_work__(self):
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
    def __get_damage__(self, dist):
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
  def __get_name__(self):
    return self.__name
  def __eat__(self):
      self.__mass += 0.5
  def __get_eat__(self):
      return self.__mass
dwarf_worker = Dwarf("Боб");
dwarf_worker.__startWork__(2)
dwarf_worker.__drink__(2.5);
print(dwarf_worker.__get_name__(), dwarf_worker.__get_work__(), dwarf_worker.__get_liters_drank__())

dog = Animal("Тузик", 1)
dog.__eat__()
print(dog.__get_name__(), dog.__get_eat__())

bow = Weapon(2)
print( bow.__get_damage__(40) )


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
  def __init__(self, n,t,s):
    super().__init__(n,t,s)
    self.name = n
    self.type = 2
    self.speed = s
    self.weight = 2
    self.dopgruz = 1
  def fullspeed(self):
    self.speed /= self.weight
  def fullmassa(self):
    self.weight += self.dopgruz

class Porshe(Car):
  def __init__(self, n,t,s,aerod,loud):
    super().__init__(n,t,s)
    self.name = n
    self.type = 3
    self.aero = aerod
    self.speed = s
    self.loud = loud
  def rate(self,new_speed):
    self.speed = new_speed
    self.speed += self.speed * self.aero
  def volume(self,loud):
    self.loud += loud

porshe_911 = Porshe("911", 3, 300, 0.2, 20)
porshe_911.rate(340)
porshe_911.volume(80)
print(porshe_911.speed, porshe_911.loud)
volvo_850 = Volvo("850", 2, 200)
volvo_850.fullspeed()
volvo_850.fullmassa()
print(volvo_850.weight, volvo_850.speed)

class Engine:
  def __init__(self, v, p, t):
    self.motortype = t # 1 - бензиновый, 2 дизельный
    self.volume = v # объем двигателя
    self.power = p # мощность двигателя
class v4(Engine):
  def __init__(self, v, p, t, kd):
    super().__init__(v, p, t)
    self.motortype = 2
    self.kpddvig = kd # крутящий момент дизельного двигателя по отношению к бензиновому 
    self.cool = 0.3 # охлаждение двигателя
  def volvo_v4_diesel_kpd(self):
    self.power -= self.power * self.kpddvig
  def volvo_v4_diesel_p(self):
    if self.motortype == 2:
      self.volume += self.volume * self.cool
    elif self.motortype == 1:
      self.volume = self.volume
class v6(Engine):
  def __init__(self, v, p, t):
    super().__init__(v, p, t)
    self.motortype = 1
  def v6_turbo(self,turbo):
    self.volume = self.volume * turbo
  def v6_petrol(self):
    if self.motortype == 1:
       self.power += self.power * 0.3
      
diesel = v4(1.6, 2000, 2, 0.3)
diesel.volvo_v4_diesel_kpd()
diesel.volvo_v4_diesel_p()
print(diesel.power, diesel.volume)
petrol = v6(1.6, 2000, 1)
petrol.v6_turbo(1.4)
petrol.v6_petrol()
print(petrol.power, petrol.volume)
  
    

    