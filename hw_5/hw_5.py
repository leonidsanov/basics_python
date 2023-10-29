"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


import os

def parse_path(path):
    filepath, file_extension = os.path.splitext(path)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, file_extension)


# Example usage
file_path = "/path/to/file.txt"
details = parse_path(file_path)
print(details)


"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
"""


names = ["John", "Alice", "Bob"]
rates = [5, 7, 3]
premiums = ["10.25%", "8.50%", "12.75%"]

premium_dict = {name: rate * float(premium.strip("%")) / 100 for name, rate, premium in zip(names, rates, premiums)}

print(premium_dict)


"""
Создайте функцию генератор чисел Фибоначчи
"""


def fibonacci_generator(n):
    fib_numbers = [0, 1]

    for i in range(2, n):
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])

    return fib_numbers

# Example usage
n = 10
fib_sequence = fibonacci_generator(n)
print(fib_sequence)
