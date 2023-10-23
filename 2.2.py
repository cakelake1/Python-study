
Рефлексия:
    
    1.2
    Вижу небольшие синтаксические ошибки, а также асбтрактные классы, без конкретной привязки.
    И насколько я вижу строковые значения используются только в имени и названии. пока сделаю пометку.
    Исправлено в задании ниже.
    
    1.3
    Тут у меня была похожая мысль сделать проще, но я зацепился за "побочный эффект" и сделал не так наглядно.
    Да и "если в руках меч, то урон режущий, иначе "неизвесто"" - также наглядный пример.
    
    

1.2.:
class Dwarf:
    def __init__(self, dwarf_name, 
                 dwarf_race, dwarf_skill, 
                 , dwarf_age,
                 dwarf_size, dwarf_strengh):
        self.name = dwarf_name # имя дварфа
        self.race = dwarf_race # раса дварфа (1 дварф, 2 темный дварф, 3 животное)
        self.skill = dwarf_skill # умение дварфа( 1 учеба, 2 спорт)
        self.size = dwarf_size # размер дварфа в кубических сантиметрах (1000 - 60000) 
        self.strengh = dwarf_strengh # Сила дварфа (1-360)
        self.age = dwarf_age # возраст дварфа (0-180)
    def High_age(self, new_age): # при получении нового возраста, сила возрастает
        self.age = new_age
        self.strengh = self.strengh * 1.2 
    def Sleep(self): # во сне дварф не двигается, у него нет сил и молодеет
        self.Stop()
        self.strengh = 0
        self.age -= -1
    def Strengh(self, new_strengh): # при получении новой силы, происходит перерасчет размера дварфа
        self.strengh = new_strengh
        self.size = self.strengh * self.age
    
   
    
class home_animal_alpaka:
    def __init__(self, alpaka_name, alpaka_race, 
                 alpaka_size, alpaka_biom, 
                 alpaka_price):
        self.name = alpaka_name # имя альпаки
        self.race = alpaka_race # раса альпаки (1 дварф, 2 темный дварф, 3 животное)
        self.size = alpaka_size # размер альпаки в кубических сантиметрах (1000 - 120000)
        self.biom = alpaka_biom # Место обитания альпаки (1 вальер, 2 зеленые луга)
        self.price = alpaka_price # стоимость альпаки
    def current_size_price(self, new_size):  # меняется размер - меняется и стоимость альпаки
        self.size = new_size
        self.price = (self.price * self.size) / 10
        
    name = "Василек" # название одомашненного животного
    race = 2 
    attributes = "Пастбищное" , "Доится" , "Стрижется" , "Разводимое" # аттрибуты
    size = 70,000 # размер, в кубических сантиметрах
    biom_place = "Вальер" # Место обитания
    price = 200 # Стоимость приобретения

class weapon:
    weapon_name = "Копье"
    weapon_type_damage = "Колющее"
    weapon_type_base = "Дерево"
                

dwarf1 = Dwarf()
dwarf1.name = "Борода"
dwarf1.age = 20
print("Дварф 1:", dwarf1.name, dwarf1.age, "Лет")

weapon1 = weapon()
weapon.weapon_name = "Меч"
weapon.weapon_type_damage = "Режущее"
weapon.weapon_type_base = "Сталь"
print("Оружие", weapon.weapon_name, ", Тип:", weapon.weapon_type_damage,
", Основа:", weapon.weapon_type_base)

alpaka1 = homeanimal()
homeanimal.name = "Альпака Пака"
homeanimal.price = 100
print("Имя альпаки:", homeanimal.name, ", Стоимость:", homeanimal.price)


1.3:
class Dwarf:
    name = "Дварф" # Имя дворфа
    race = "Гуманоид" #  вид рассы
    learnin_skill = "Учится" #  аттрибут обучения
    age = 0 # возраст, полных лет
    size = 60,000 # размер, в кубических сантиметрах   
    biom_place = "Дварфийские крепости" # Место обитания
    weapon_skill = "speardwarf" # Навык владения оружием - копье
    strenght = 1
    

def make_new_dwarf(dwarf, name):
    dwarf.name = name # Меняется имя переданного dwаrf'а, определенного вне функции
    					#потому что он передается по ссылке, а не по значению.
    return dwarf


d1 = Dwarf()
d1.name = "Bob"

d2 = make_new_dwarf(d1, "Kris")

print("d1.name = ", d1.name)
print("d2.name = ", d2.name)
