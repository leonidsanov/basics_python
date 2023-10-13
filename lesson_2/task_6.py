"""
Напишите программу банкомат. 
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег
"""

amount = 0
op_count = 1

def main():
    global amount
    global op_count
    while True:
        s = input('Выберите операцию (1 - пополнить; 2 - снять; 3 - выход) : ')
        if s not in ('1', '2', '3'):
            continue
        if amount > 5 * 10 ** 6:
            amount = amount * 0.9
        if s == '1':
            fill()
        elif s == '2':
            withdraw()
        else:
            print_amount()
            break
        print_amount()


def print_amount():
    global amount
    print(f'На счете {amount} ед.')       


def fill():
    """
    Пополнение баланса
    """
    global amount
    global op_count
    while True:
        v = input('Укажиет сумму пополнения кратная 50 ед :')
        # if v == 'q':
        #     break
        try:
            s = int(v)
        except ValueError:
            continue
        if not s % 50 == 0:
            print(f'Сумма пополнения должна быть кратна 50 ед.')
            continue
        amount += s
        amount = amount + (percent(0.03) if op_count % 3 == 0 else 0)
        op_count += 1
        break
    

def withdraw():
    """
    Снятие
    """
    global amount
    global op_count
    while True:
        v = input('Укажите сумму снятия кратная 50 ед :')
        # if v == 'q':
        #     break
        try:
            s = int(v)
        except ValueError:
            continue
        if not s % 50 == 0:
            print(f'Сумма пополнения должна быть кратна 50 ед.')
            continue
        p = percent(0.015)
        # но не менее 30 и не более 600 у.е
        if p < 30:
            p = 30
        if p > 600:
            p = 600
        if amount < s + p:
            print(f'Недостаточно средств на счете.')
            break
        amount = amount - s - p
        amount = amount + (percent(0.03) if op_count % 3 == 0 else 0)
        op_count += 1
        break



def percent(procent):
    global amount
    return round(amount * procent, 2)


if __name__ == '__main__':
    main()