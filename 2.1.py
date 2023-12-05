

1.1 :
1) Банковское приложение:
        Класс: банковская карта
            Структура: - номер карты, срок действия, пин код, Имя карты, тип карты.
    2) Интернет-магазин:
        Класс : Товар(карточка товара)
            Структура: Стоимость, Изображение, Характеристики, Описание.

1.2.:
class Dwarf:
    name = "Дварф" # Имя дворфа
    race = "Гуманоид" #  вид рассы
    Learnin_skill = "Учится" #  аттрибут обучения
    age = 0 # возраст, полных лет
    size = 60,000 # размер, в кубических сантиметрах   
    biom_place = "Дварфийские крепости" # Место обитания
    weapon_skill = "speardwarf" # Навык владения оружием - копье
    strenght = 1
    
class homeanimal:
    name = "Альпака" # Название одомашненного животного
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
    Learnin_skill = "Учится" #  аттрибут обучения
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
