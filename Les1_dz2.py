# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
from math import fabs


x = int(input('Введите чило  x: '))
y = int(input('Введите чило  y: '))
z = int(input('Введите чило  z: '))

for x in range(2):
    for y in range(2):
        for z in range(2):
            res = (not (x and y and z)) == (not x or not y or not z)
            print(res)
