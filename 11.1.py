# 1. Задание Добавьте в какой-нибудь свой код логирование и assert-ы.
# Логирование выполняйте с помощью стандартной библиотеки
import logging
logging.basicConfig(filename="app.log", level = logging.INFO, format="%(asctime)s - %(levelname)s - %(module)s - %(message)s")


class Animal:
    
    def __init__(self, a, w, s):
        self.age = a # возраст, полных лет
        self.weight = w # масса, кг   
        self.speed = s # скорость, км/ч   
        
    def run(self, new_speed):
        self.speed = new_speed
        logging.info("method run is working") # выводится в отдельный лог информация, о том что данный метод(модуль) работает
        assert new_speed > 0 # скорость должна быть больше 0
        assert new_speed < 1000 # скорость должна быть меньше 1000    
        
    def stop(self):
        self.speed = 0
class Cat(Animal):    
    
    def __init__(self, n,a,w,s):
        super().__init__(a,w,s)
        self.name = n
        self.fq = 100
        
    
    def purr(self, freq):
        self.fq = freq
        logging.info("method purr is working") # выводится в отдельный лог информация, о том что данный метод(модуль) работает
        assert freq < 100 # мурчание не должно быть выше 100 значений        
bars = Cat("Барсик", 1, 3.5, 20)
bars.run(999)

bars.purr(99)
print(bars.speed, bars.fq)
