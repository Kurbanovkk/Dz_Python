"""2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)"""
import random

a = int(input('Введите а: '))
b = int(input('Введите b: '))
list_ = []


for i in range(a):
    list_.append([0] * b)

for i in range(a):
    for j in range(b):
        list_[i][j] = random.randint(1, 10)

print(list_)

sum_ = 0
for i in range(a):
    for j in range(b):
        sum_ += list_[i][j]
    print(f'Среднее арифм {i} внутреннего списка равен {sum_ / b}')
