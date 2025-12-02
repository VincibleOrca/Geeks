class Hero:
    #конструктор класса
    def __init__(self, name, lvl, hp):
        #атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def base_method(self):
        return f'base action {self.name}'

Kirito = Hero('Kirito', 100, 100)
asuna = Hero('Asuna', 101, 101)

#объект/экземпляр на основе класса
print(Kirito.base_method())
print(asuna.base_method())


class Cat:
   """
   Класс Кот — описывает домашних котов :)
   """
   def __init__(self, name, age, color):
       self.name = name         # кличка
       self.age = age           # возраст в годах
       self.color = color       # цвет шерсти
       self.hungry = True       # голодный ли кот

   def meow(self):
       """Кот мяукает"""
       return f"{self.name} говорит: Мяу-мяу!"

   def eat(self, food="корм"):
       """Кот ест и больше не голодный"""
       self.hungry = False
       return f"{self.name} съел {food} и теперь доволен!"

   def info(self):
       """Информация о коте"""
       status = "голодный" if self.hungry else "сытый"
       return f"Кот {self.name}, {self.age} лет, цвет: {self.color}, сейчас {status}"


# Создаём несколько котов и проверяем
cat1 = Cat("Барсик", 3, "серый")
cat2 = Cat("Мурка", 2, "чёрно-белая")
cat3 = Cat("Рыжик", 5, "рыжий")

# Проверяем методы
print(cat1.info())
print(cat1.meow())
print(cat1.eat("рыбу"))
print(cat1.info())

print("\n" + cat2.info())
print(cat2.meow())
print(cat2.eat())

print("\n" + cat3.info())
print(cat3.meow())