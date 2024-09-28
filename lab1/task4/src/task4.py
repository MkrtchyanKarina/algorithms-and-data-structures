import random
import time

from lab1.src.verifications import data_verification4

start = time.time()


@data_verification4
def lineal_search(m, x):
    res = []
    for i in range(len(m)):
        if m[i] == x:
            res.append(i)
    count = len(res)
    if count == 0:
        return -1
    elif count == 1:
        return res
    else:
        return count, res


test_array = [random.randint(-10**3, 10**3) for i in range(10**3)]
test_x = test_array[random.randint(0, 10**3)]
res_test = lineal_search(test_array, test_x)
print(*res_test, sep=", ")
# L = ("Рак Кабан Козел Лемминг Черепаха Муравьед Нутрия Индюк Ягуар Хамелеон Коала Барсук Акула "
#      "Соболь Осьминог Лошадь Крыса Зебра Кошка Кашалот Крот Тюлень Индейка Верблюд Сурок Лисица Утка Заяц Бобр Суслик Аллигатор Варан Леопард "
#      "Игуана Овца Гиена Еж Ленивец Гадюка Крокодил Свинья Лось Курица Кенгуру "
#      "Дикобраз Хомяк Утконос Жираф Ондатра Бизон Скунс Обезьяна Газель Койот "
#      "Мышь Пингвин Осел Бурундук Тигр Олень Омар Пантера Пума Кролик Ехидна Жаба "
#      "Удав Кит Волк Морж Выхухоль Гепард Песец Енот Антилопа Лемур Медведь Выдра "
#      "Белка Гусь Гиппопотам Уж Рысь Зубр Куница Динозавр Лев Кобра Собака Носорог "
#      "Лягушка Хорек Корова Анаконда")
# print(lineal_search(L.split(" "), "Свинья"))
print(time.time() - start)

