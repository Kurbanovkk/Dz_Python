"""3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления. """

a = int(input('Введите число, которое нужно преоброзовать в шестнадцатиричную: '))
list_ = []

while a > 0:
    b = a % 16
    if b == 10:
        list_.append('A')
    elif b == 11:
        list_.append('B')
    elif b == 12:
        list_.append('C')
    elif b == 13:
        list_.append('D')
    elif b == 14:
        list_.append('E')
    elif b == 15:
        list_.append('F')
    else:
        list_.append(b)

    if a // 16 < 16:
        a = a // 16
        list_.append(a)
    a = a // 16

print(list_[::-1])
