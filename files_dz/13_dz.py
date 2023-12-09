#Рефлексия:
# Не нашел предлагаемую функцию сортировки массивов, взял функцию нахождения минимального или максимального значения в массиве.
# Вижу, что мог бы сделать еще тест на "странные" значения и на почти пустой массив.

# Задание:
# 3.1. Программно создайте 10 файлов с именами 1.txt, 2.txt, ..., 10.txt, и в каждый запишите три случайных числа, каждое с новой строки:
import random
for i in range(1,11):
    fo = "{}.txt".format(i)
    with open(fo, "w") as f:
        f.write(f"{(random.randint(1,10))}\n")
        f.write(f"{(random.randint(1,10))}\n")
        f.write(f"{(random.randint(1,10))}")

# 3.2 :
def opentwo_and_summ():
    x1 = int(random.randint(1,10))
    x2 = int(random.randint(1,10))
    f1 = open(str(x1)+".txt", "rt")
    f2 = open(str(x2)+".txt", "rt")
    d=0
    try:
        for s in f2:
            d +=int(s.rstrip())
        for s in f1:
            d +=int(s.rstrip())
        print(d)    
    except ValueError:
        print("Содержимое файла испорчено")
    finally:
        f1.close()
        f2.close()
opentwo_and_summ()

# 3.3

rc = open("classes.txt", "rt", encoding="utf-8")
class Cats:
    def __init__(self, name, weight, fq):
        self.name = name
        self.weight = weight
        self.fq = fq

    def __repr__(self):
        return f"{str(self.name)} : весом {float(self.weight)} кг : мурчание {int(self.fq)} \n"
s = rc.readline()  
cats_list = [] 
try:
    while s !="":
      r = s.split()
      r1 = r[0]
      r2 = r[1]
      r3 = r[2]
      cats_list.append(Cats(str(r1), float(r2), int(r3)))
      s = rc.readline()  
except:
    ValueError
    ("В файле classes присутствуют ошибки значений, проверьте цифры"  )         
      
finally:
    rc.close()
print(cats_list)


        