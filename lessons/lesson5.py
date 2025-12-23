class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @property.setter
    def price(self, value):
        if value < 0:
            return "The price cannot be less than 0"
        self.__price = value

iphone = Product("Iphone", 1200)
print(iphone.price)
