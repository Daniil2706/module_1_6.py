class Animal:
    def __init__(self, name):
        self.alive = True #живой
        self.fed = False #накормленный
        self.name = name # индивидуальное название каждого животного.
        
class Plant:
    def __init__(self, name):
        self.edible = False #съедобность
        self.name = name #индивидуальное название каждого растения

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            fed = False
            
class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            fed = False

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True #отравлен    
    pass

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
