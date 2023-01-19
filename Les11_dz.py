"""Создать 2 массива NumPy
Один из случайных чисел, второй - использую arange Или linspace
После этого выполнить математические операции- сложить, перемножить, делить
Найти максимальный элемент в каждой строчке и столбце первого массива (из случайных чисел_
Найти максимальный элемент в из 2 массивов
Изменить форму массива"""

import numpy as np

array1 = np.random.random(8)
print(array1)
array2 = np.linspace(1, 5, 8)
print(array2)

print(f' сумма элементов массивов: {array1 + array2}')
print()
print(f' разность элементов массивов: {array1 - array2}')
print()
print(f' произведение элементов массивов: {array1 * array2}')
print()
print(f' частное элементов массивов: {array1 / array2}')
print()


a1 = array1.reshape(2, 4)
a2 = array2.reshape(2, 4)
print(a1)
print(a2)

print(f' максимальные числа по столбцам первого массива = {a1.max(axis=0)}')
print(f' максимальные числа по строкам первого массива = {a1.max(axis=1)}')
print(f' максимальные числа по столбцам второго массива = {a2.max(axis=0)}')
print(f' максимальные числа по строкам второго массива = {a2.max(axis=0)}')

array1_3 = a1.max(axis=0)
array1_4 = a1.max(axis=1)
array2_3 = a2.max(axis=0)
array2_4 = a2.max(axis=1)

print(array1_3.max())
print(array1_4.max())
print(array2_3.max())
print(array2_4.max())
