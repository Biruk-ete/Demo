# Exercises from module1 day04
#1
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def describe(self):
        print(f'Title: {self.title} Author: {self.author} Pages: {self.pages}')

book1 = Book("Oromay", "Bealu Girma", 400)
book2 = Book("Megbat ena mewtat", "Bewketu Seyum", 300)

book1.describe()
book2.describe()

print('\n')
#2
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, n):
        self.quantity += n
        print(f'Total Restock: {self.quantity}')

    def sell(self, n):
        self.quantity -= n
        print(f'Total reserve: {self.quantity}')
    
product1 = Product("Oil", 2300, 5)
product2 = Product("cement", 700, 17)

product1.restock(11)
product1.sell(10)

product2.restock(9)
product2.sell(14)

print('\n')
#3, 4, 5
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("No negative balance")
        self.__quantity = value
    
    def restock(self, n):
        self.quantity += n
        print(f"{self.name} restocked to {self.quantity}")

    def sell(self, n):
        self.quantity -= n
        print(f"{self.name} remaining: {self.quantity}")

product1 = Product("onion", 230, 6)
product2 = Product("cake", 403, 8)
product3 = Product("Medicin", 860, 43)

product1.restock(10)
product1.sell(5)

product1.quantity = 2000
print(product1.quantity)
print(product2.quantity)
print(product3.quantity)