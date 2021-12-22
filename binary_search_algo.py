import random

print ('Бинарный алгоритм поиска')
print ('Я загадал число от 1 до 100. Сможешь отгадать? ')

x = random.randint (1, 100)
y = 0
#print (x)

while y != x:
    y = input('Введите число от 1 до 100: ')
    y = int(y)
    if y > x:
        print (str(y) + ' больше загаданного ')
    elif y < x:
        print (str(y) + ' меньше загаданного ')
    else:
        print ('Вы угадали число!')
