""" Вводим с клавиатуры целое число X и У.
Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3 """
x = int(input('Введите число х: '))
y = int(input('Введите число y: '))
count = 0

if x < y:
    for i in range(x, y):
        if i % 2 == 0 and i % 3 == 0:
            if i == 0:
                continue
            count += 1
elif x > y:
    for i in range(y, x):
        if i % 2 == 0 and i % 3 == 0:
            if i == 0:
                continue
            count += 1

print(f'количество чисел между {x} и {y} делящихся на 2 и 3 = {count}')
