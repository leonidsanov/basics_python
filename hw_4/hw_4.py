"""
1. Напишите функцию для транспонирования матрицы.
"""

def transpose_matrix(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    columns = len(matrix[0])
    
    # Create a new transposed matrix with swapped dimensions
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(columns)]
    
    # Iterate over the elements of the original matrix and fill the transposed matrix
    for i in range(rows):
        for j in range(columns):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = transpose_matrix(matrix)
print(transposed)


"""
2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
используйте его строковое представление.
"""

def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set)):
            result[key] = value
        else:
            result[str(key)] = value
    return result


dictionary = create_dict(name="John", age=25, city="New York")
print(dictionary)


"""
3. Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.

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

from datetime import date

bank = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01


def add_bank(cash: float) -> None:
    global bank
    global count
    bank += cash
    count += 1
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начислены проценты в размере: ", percent_add * bank)


def take_bank(cash: float) -> None:
    global bank
    global count
    bank -= cash
    count += 1

    if cash * percent_take < 30:
        bank -= 30
        print("Списаны проценты за снятие: ", 30)
    elif cash * percent_take > 600:
        bank -= 600
        print("Списаны проценты за снятие: ", 600)
    else:
        bank -= cash * percent_take
        print("Списаны проценты за снятие: ", cash * percent_take)
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начислены проценты в размере: ", percent_add * bank)


def exit_bank():
    print("До свидания!\n")
    exit()


def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму опреации кратную 50\n"))
        if cash % 50 == 0:
            return cash


list_operation = []

while True:
    action = input(
        "1 - снять деньги\n2 - пополнить\n3 - баланс\n4 - вывести историю операций\n5 - выйти\n"
    )

    if action == "1":
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списан налог на богатство: ", bank * percent_tax)
        cash = check_bank()
        if cash < bank:
            take_bank(cash)

            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("Нет денег\n")
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списан налог на богатство: ", bank * percent_tax)
        print("Баланс = ", bank)
    elif action == "2":
        cash = check_bank()
        add_bank(cash)
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списан налог на богатство: ", bank * percent_tax)
        print("Баланс = ", bank)

        list_operation.append([str(date.today()), cash])

    elif action == "3":
        print("Баланс = ", bank)
    elif action == "4":
        print(list_operation)
    else:
        exit_bank()
