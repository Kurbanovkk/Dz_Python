"""1)
Написать программу, где создадим класс Soup (для определения типа супа), принимающий 1 аргумент - который отвечает за основной
продукт к выбираемому супу.
В этом классе создать метод show_my_soup(), выводящий на печать «Суп - {Основной продукт}» в случае наличия добавки
Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»"""


class Soup:
    def __init__(self):
        self.supplement = False

    def suppl(self):
        self.supplement = True

    def show_my_soup(self, ingredient):
        if self.supplement:
            print(f'суп - с {ingredient}')
        else:
            print('Обычный кипяток')


s = Soup()

soup_ = input(
    'Сегодня мы будем готовить суп, будем использовать ингредиенты? ')

if soup_ == 'да':
    s.suppl()
    ingredient = input('Какой ингредиент будем использовать? ')
else:
    ingredient = ''

s.show_my_soup(ingredient)
