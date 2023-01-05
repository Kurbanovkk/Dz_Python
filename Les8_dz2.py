"""2)Нужно напистаь программу
В ней используем классы - имя студента name, номер группы group и список полученных оценок progress.
В самой программе вводим список всех студентов.
В программе нужно вывести список студентов, отсортированный по имени, А так же студентов, у которых низкие оценки"""


class Student:
    def __init__(self, name, group, progress):
        self.name = name
        self.group = group
        self.progress = progress

    def __str__(self):
        return f'Имя: {self.name}, группа: {self.group}, средняя оценка: {self.progress}'

    def info(self):
        return f'Имя: {self.name}, группа: {self.group}, средняя оценка: {self.progress}'


count1 = int(input('Какое количество студентов? '))
prog = 0
list_ = []
li = []
estimation = {
    1: 'Математика',
    2: 'Русский язык',
    3: 'Информатика',
    4: 'Английский'
}

for i in range(count1):
    name = input('Введите имя студента: ')
    li.append(name)
    gr = int(input('введите номер группы студента: '))
    li.append(gr)
    for j in estimation:
        prog += int(input(f'Введите оценку по {estimation[j]}: '))
    prog = prog / len(estimation)
    li.append(prog)
    list_.append(li)
    li = []
    prog = 0

list_neg = []
co = 0

for i in range(len(list_)):
    if list_[i][2] < 3:
        list_neg.append(list_[i])
        co += 1

for i in range(co):
    student = Student(list_neg[i][0], list_neg[i][1], list_neg[i][2])
    print(student.info())
