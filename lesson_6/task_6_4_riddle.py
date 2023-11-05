"""
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
"""


def guess_riddle(riddle: str, ansvers: list[str], attempts_count: int) -> int:
    answer_number = 0
    print(f'Отгадай загадку: \n{riddle}')
    for i in range(1, attempts_count + 1):
        print(f'Попытка номер {i} осталось попыток {attempts_count - i}.')
        s = input().lower()
        if s in ansvers:
            answer_number = i
            break
    return answer_number
