# Тиаы функций:
# 1. Глобальные
# 2. Локальные (вложенные в другие функции)
# 3. Методы (функции, ассоциированные с каким-либо объектом)
# 4. Анонимные (не имеют имени и объявляются в месте использования - представлены лямбда-выражениями



def sum_of_cubes(x, y):  # Глобальная функция (1)

    # Локальная функция (2) (ее "видит" только код внутри sum_of_cubes())
    def cube(a):
        return a**3
    return cube(x) + cube(y)  # return возвращает результат выполнения тому,
                              # кто вызвал эту функцию

print(sum_of_cubes(2,4))

class Car:
    def move(self, x):  # Метод (3)
        self.x += x

lada = Car()
lada.x = 4;
lada.move(12)
print(lada.x)

players = [{"name": "Юрий", "rank": 5},
           {"name": "Сергей", "rank": 3},
           {"name": "Максим", "rank": 4}]

# Анонимная функция (4) (лямбда-выражение)
# В функции sorted() используется для определения порядка сортировки

print(sorted(players, key=lambda player: player["name"]))  # Сортировка по name
# [{'rank': 4, 'name': 'Максим'}, {'rank': 3, 'name': 'Сергей'}, {'rank': 5, 'name': 'Юрий'}]

print(sorted(players, key=lambda player: player["rank"]))  # Сортировка по rank
# [{'rank': 3, 'name': 'Сергей'}, {'rank': 4, 'name': 'Максим'}, {'rank': 5, 'name': 'Юрий'}]
