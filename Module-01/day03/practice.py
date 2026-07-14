# Exercises from module1 day03
#1
city_names = ['Addis Ababa', 'Adama', 'Bishoftu', 'Gondor', 'Mekele', 'Adama', 'Dire Dawa', 'Addis Ababa']
unique = set(city_names)
print(unique) 
print(len(unique))

print('\n')
#2
grocery_items = {
    "Milk" : 100,
    "Bread" : 75,
    "Eggs" : 134,
    "Fruit" : 200,
    "Bevarage" :250
}

for item, price in grocery_items.items():
    print(f'{item}: {price} ETB')

print('\n')
#3
prices = [100, 250, 400, 80]
with_tax = [price + (price * 0.15) for price in prices]
print(with_tax)

print('\n')
#4
with_condition = [price for price in prices if price < 200]
print(with_condition)

print('\n')
#5
with open("names.txt", "w") as n:
    n.write("Biruk \n")
    n.write("Abera \n")
    n.write("Gelan \n")

with open("names.txt", "r") as n:
    for name in n:
        print(name.strip())

print('\n')

with open("names.txt", "r") as n:
    names = n.read()
    print(names)

print('\n')
#6
try:
    number = int(input("Enter a number:"))
    num = 1000 / number
except ValueError:
    print("Enter a number")
except ZeroDivisionError:
    print("Enter a number greater that zero")
else:
    print(num)