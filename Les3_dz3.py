"""3.12 Вводим с клаиватуры строку. Необходимо вывести строку, где развернём подстроку между первой и последней буквой "о" из
исходной строки. Если она только одна или её нет - то сообщить, что буква "о" - одна или не встречается."""

stroka = input('Bведите любую строку: ')
a = None
b = None
c = - 1

for i in range(len(stroka)):
    if stroka[i] == 'о':
        a = i
        break
if a != None:
    for i in range(len(stroka) - 1, a, -1):
        if stroka[i] == 'о':
            b = i - 1

if (a == None and b != None) or (a != None and b == None):
    print('Буква "о" одна')
elif a == None and b == None:
    print('Буквы "о" нет')
else:
    print(stroka[b:a:c])
