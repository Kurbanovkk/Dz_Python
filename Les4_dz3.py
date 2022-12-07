"""3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором."""
import random

li = []
temp = 0

for i in range(30):
    li.append(random.randint(1, 10))

print(li)

for i in range(len(li) - 1):
    k = i
    for j in range(i + 1, len(li)):
        if li[j] < li[k]:
            k = j
    li[i], li[k] = li[k], li[i]

print(li)
