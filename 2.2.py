
#Рефлексия:
    
#   1.2
#  Вижу небольшие синтаксические ошибки, а также асбтрактные классы, без конкретной привязки.
# И насколько я вижу строковые значения используются только в имени и названии. пока сделаю пометку.
    #Исправлено в задании ниже.
    
    #1.3
    #Тут у меня была похожая мысль сделать проще, но я зацепился за "побочный эффект" и сделал не так наглядно.
    #Да и "если в руках меч, то урон режущий, иначе "неизвесто"" - также наглядный пример.
    
    

#1.2.:
class Dwarf:
    def __init__(self, dwarf_name, 
                 dwarf_race, dwarf_skill, 
                 dwarf_age,
                 dwarf_size, dwarf_strengh):
        self.name = dwarf_name # имя дварфа
        self.race = dwarf_race # раса дварфа (1 дварф, 2 темный дварф, 3 животное)
        self.skill = dwarf_skill # умение дварфа( 1 учеба, 2 спорт)
        self.size = dwarf_size # размер дварфа в кубических сантиметрах (1000 - 60000) 
        self.strengh = dwarf_strengh # Сила дварфа (1-360)
        self.age = dwarf_age # возраст дварфа (0-180)
    def stop(self):
        self.strengh = 0
    def high_age(self, new_age): # при получении нового возраста, сила возрастает
        self.age = new_age
        self.strengh = (self.strengh * self.age) / 2 
    def sleep(self): # во сне дварф не двигается, у него нет сил и молодеет
        self.stop()
        self.age -= 1
    def strengh_up(self, new_strengh): # при получении новой силы, происходит перерасчет размера дварфа
        self.strengh = new_strengh
        self.size = self.strengh * self.age * 10

   
    
class home_animal_alpaka:
    def __init__(self, alpaka_name, alpaka_race, 
                 alpaka_size, alpaka_biom, 
                 alpaka_price):
        self.name = alpaka_name # имя альпаки
        self.race = alpaka_race # раса альпаки (1 дварф, 2 темный дварф, 3 животное)
        self.size = alpaka_size # размер альпаки в кубических сантиметрах (1000 - 120000)
        self.biom = alpaka_biom # Место обитания альпаки (1 вальер, 2 зеленые луга)
        self.price = alpaka_price # стоимость альпаки
    def stop(self):
        self.price = 0
    def current_size_price(self, new_size):  # меняется размер - меняется и стоимость альпаки
        self.size = new_size
        self.price = (self.price * self.size) / 2000
    def transport(self): # альпака останавливается и полностью обесценивается, затем перемещается на зеленые луга на небеса.
        self.stop()
        self.biom = 2
    def disguise(self): # альпака останавливается и перед нами не альпака, а уже темный дварф, начало новой истории
        self.stop()
        self.race = 2       
                
alpaka_1 = home_animal_alpaka("Алькатара", 3, 2000, 1, 200 )
alpaka_2 = home_animal_alpaka("Франческа", 3, 5000, 2, 400 )
alpaka_3 = home_animal_alpaka("Янтарная", 3, 4000, 1, 350 )
alpaka_1.current_size_price(5000)
alpaka_2.transport()
alpaka_3.disguise()
print("Новая стоимость "+ alpaka_1.name,+ alpaka_1.price)
print("Новая локация для " + alpaka_2.name," - " , alpaka_2.biom)
print("Перерождение "+ alpaka_3.name, " в расу номер -  ", alpaka_3.race)

dwarf_1 = Dwarf("Дварф - нахлебник", 1, 1, 20, 20000, 10 )
dwarf_1.strengh_up(200)  
dwarf_2 = Dwarf("Дварф - стражник", 1, 2, 20, 60000, 10)
dwarf_2.high_age(50)  
dwarf_3 = Dwarf("Дварф - сновидец", 1, 1, 20, 30000, 30)
dwarf_3.sleep()


print(dwarf_1.name, " меняет свой размер на " ,dwarf_1.size)
print("У ",dwarf_2.name, "меняется возраст и сила становится равна ", dwarf_2.strengh)
print(dwarf_3.name , " засыпает" , "его сила становится равна", dwarf_3.strengh, ", а возраст падает до ", dwarf_3.age)



