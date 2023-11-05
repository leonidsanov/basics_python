"""
Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
"""


from sys import argv
import guess as gn


if len(argv) != 4:
    print('Использование: python task_6-3.py <lower_bound> <upper_bound> <max_attempts>')
else:
    lower_bound = int(argv[1])
    upper_bound = int(argv[2])
    max_attempts = int(argv[3])

    res = gn.guess_number(lower_bound, upper_bound, max_attempts)
    if res:
        print('Vin')
    else:
        print('Game over')
