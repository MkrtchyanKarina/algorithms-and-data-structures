import unittest
from lab1.task4.src.task4 import lineal_search
import psutil
import time
import random


class InsertionSortTestCase(unittest.TestCase):
    def test_lineal_search1(self):
        L = ("Рак Кабан Козел Лемминг Черепаха Муравьед Нутрия Индюк Ягуар Хамелеон Коала Барсук Акула "
             "Соболь Осьминог Лошадь Крыса Зебра Кошка Кашалот Крот Тюлень Индейка Верблюд Сурок Лисица Утка Заяц Бобр Суслик Аллигатор Варан Леопард "
             "Игуана Овца Гиена Еж Ленивец Гадюка Крокодил Свинья Лось Курица Кенгуру "
             "Дикобраз Хомяк Утконос Жираф Ондатра Бизон Скунс Обезьяна Газель Койот "
             "Мышь Пингвин Осел Бурундук Тигр Олень Омар Пантера Пума Кролик Ехидна Жаба "
             "Удав Кит Волк Морж Выхухоль Гепард Песец Енот Антилопа Лемур Медведь Выдра "
             "Белка Гусь Гиппопотам Уж Рысь Зубр Куница Динозавр Лев Кобра Собака Носорог "
             "Лягушка Хорек Корова Анаконда").split(" ")
        t_start = time.perf_counter()
        self.assertEqual(lineal_search(L, 'Свинья'), str(L.index('Свинья')))
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_lineal_search2(self):
        m = []
        t_start = time.perf_counter()
        self.assertEqual(lineal_search(m, 0), "-1")
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_lineal_search3(self):
        A = [random.randint(-10**3, 10**3) for i in range(10**3)]
        V = A[random.randint(0, 10**3)]
        res = str(A.index(V))
        t_start = time.perf_counter()
        if A.count(V) > 1:
            res = str(A.count(V)) + ' ' + ', '.join(str(i) for i in range(len(A)) if A[i] == V)
        self.assertEqual(lineal_search(A, V), res)
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

