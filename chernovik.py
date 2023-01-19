import numpy as np

np.array([1, 2, 3])
array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array1)
print(type(array1))
print()
np.ones(3)  # Создает массив из единиц на 3 элемента
print()
np.zeros(4)  # Создает массив из нулей на 4 элемента
print()
print(np.random.random(5))  # Массив из 5 случ чисел
print()
print(np.arange(10, 66, 7))
print()
print(np.linspace(0, 3, 5))  # мин макс и кол во элементов
print()
print(np.zeros([3, 2]))  # двумерный массив 3 / 2

a1 = np.zeros([3, 2])
print()
print(array1.ndim)  # ndim - количество измерений
print()
print(array1.shape)  # размер массива 3 * 3
print()
print(array1.size)  # количество элементов массива
print()
print(array1.dtype)  # из чего состоит массив (int, float  и т.д.)
print()
print(array1.itemsize)  # количество байт занимаем ячейкой массива

ar1 = np.array([1, 3, 5])
ar2 = np.array([5, 7, 9])
# можео совершать арифм действия просто. но массивы должны быть одинакового размера
print(ar1 + ar2)
print(ar1 * 2)  # можно умножать все элементы массива на какое-то число
print()

# можно обращаться по индексу и использовать срезы

print(array1[1])
print()
print(array1[1][2])
print()
print(array1[1:, 1:])
print()
print(ar1.min())  # работает и на макс
print()
print(ar1.sum())  # получаем сумму
print()
print(ar1.mean())  # среднее арифм
print()
print(ar1.prod())  # перемножение всех чисел
print()

temp = np.array([11, 23, 13, 42, 45, 55, 66, 62, 39, 95, 88, 55])
print(temp)
print(temp.shape)
print(temp.size)
print()
# преобразует в 6 строк и 2 столбца двумерного массива
print(temp.reshape(6, 2))
print()
# axis = 0 ищет  и выводит по столбцам axis = 1  ищет и выводит по строкам
print(temp.max(axis=0))
print()
num = np.linspace(5, 50, 24, dtype=int)
print(num)
print()
num = num.reshape(4, -1)  # если указано -1 вычисляет автоматически длину строк
print(num)
