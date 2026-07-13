# Exercises from module1 day02
# 1
tempe = int(input("What is the Temperature in degree celicius?"))
if tempe < 15:
    print('cold')
elif 15 < tempe and tempe < 28:
    print('warm')
else:
    print('hot')


print('\n')
# 2
for receipt in range(1,11):
    print(f'Receipt #{receipt}')

print('\n')
# 3
for even_num in range(1, 21):
    if even_num % 2 == 0:
        print(even_num)

print('\n')
# 4
def apply_discount(price, percent=10):
    percent /= 100
    new_price = price * percent
    return new_price

print(apply_discount(100))
print(apply_discount(100, 20))
    
print('\n')
# 5
num = 5
while num > 0:
    print(num)
    num -= 1
print('Liftoff!')


