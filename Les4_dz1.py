"""1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной 
позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 """

list_ = [12, 22, 4, 6, 1, 123, 765, 33, 44, 90]
sum_ = 0
print(list_)

for i in range(1, len(list_), 2):
    sum_ += list_[i]

print(sum_)