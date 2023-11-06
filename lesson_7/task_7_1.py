"""Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.
"""


import random

def fill_file_with_random_pairs(filename, num_lines):
    with open(filename, "a") as file:
        for _ in range(num_lines):
            int_num = random.randint(-1000, 1000)
            float_num = round(random.uniform(-1000, 1000), 2)
            line = f"{int_num}|{float_num}\n"
            file.write(line)


fill_file_with_random_pairs('./lesson_7/data.txt', 10)
