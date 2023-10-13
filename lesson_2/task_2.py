"""
Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок.
Для каждого элемента в цикле выведите:
порядковый номер начиная с единицы
значение
адрес в памяти
размер в памяти
хэш объекта
результат проверки на целое число только если он положительный
результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.
"""

import sys

data = [1, 2, 3, 4, 5, 'text', 5]

for i, el in enumerate(data, start=1):
    print(i, el, id(data[i - 1]), id(el), sys.getsizeof(el), hash(el),
          'Целое' if str(el).isdecimal() else '',
          'Строка' if isinstance(el, str) else '')
#    el = False
#    print(data[i - 1])
try:
    print(hash(el))
except TypeError:
    print('Не хешируется')



import  sys


data = [10, 3.14, 'Hello', True, [1, 2, 3]]

# Добавляем повторяющиеся элементы
data.append(10)
data.append(3.14)

for i, value in enumerate(data, start=1):
    print(f"Порядковый номер: {i}")
    print(f"Значение: {value}")
    print(f"Адрес в памяти: {id(value)}")
    print(f"Размер в памяти: {sys.getsizeof(value)} байт")
    print(f"Хэш объекта: {hash(value)}")

    if isinstance(value, int):
        if value > 0:
            print("Проверка на целое число: Да")
    elif isinstance(value, str):
        print("Проверка на строку: Да")

    print("-----------------------------------------")