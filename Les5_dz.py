# Игра морской бой


from random import randint

per = int(input('Здравствуй дорогой игрок, это игра морской бой, '
                'выберите сложность игры(размер поля) от 4 до 10: ')) + 1

li1 = []
li2 = []


def fill_bs(li1, li2):
    for i in range(per):
        for j in range(per):
            li2.append(str(0))
        li1.append(li2)
        li2 = []

    for i in range(1):
        for j in range(per):
            li1[i][j] = str(j)

    for i in range(per):
        for j in range(1):
            li1[i][j] = str(i)

    for i in range(1, per - 1):
        for j in range(1, per - 1):
            li1[i][j] = str(randint(0, 1))
    return li1


fill_bs(li1, li2)

flag_ = True
while flag_ == True:
    count_ = 0
    for i in range(len(li1)):
        for j in range(len(li1)):
            if li1[i][j] == '1':
                count_ += 1

    a = int(input('Введите номер строки, где может находиться корабль: '))
    b = int(input('Введите номер стобца, где может находиться корабль: '))
    if li1[a][b] == '1':
        print('поздравляем вы попали!!! ')
        li1[a][b] = '*'
        count_ -= 1
        print(f'осталось кораблей {count_ - 2}')
    else:
        print('Промах, попробуй еще')
    if count_ - 2 == 0:
        flag_ = False
        print('Поздравляем вы уничтожили все корабли')

for i in li1:
    print(i)
