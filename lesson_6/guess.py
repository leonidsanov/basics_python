from random import randint


def guess_number(min_value, max_value, attempt_num):
    num = randint(min_value, max_value)
    i = 1
    while True:
        s = input(f'Попытка {i}. Укажите целое число от {min_value} до {max_value}: ')
        if s == 'q':
            break
        if not s.isdecimal():
            print(f'{s} - не является целым числом')
            continue
        v = int(s)
        if not (min_value <= v <= max_value):
            continue
        if v == num:
            print('Угадал')
            break
        else:
            print(f'{v} {"меньше " if v < num else "больше"} загаданного числа')
        i += 1
        if i > attempt_num:
            print(f'Количество попыток исчерпано. Не угадал.')
            break
