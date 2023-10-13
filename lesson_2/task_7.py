def deposit(balance: float, amount: float) -> float:
    balance += amount
    return balance


def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        print("Ошибка: недостаточно средств на счете")
        return balance

    withdrawal_fee = max(30, min(amount * 0.015, 600))
    balance -= amount + withdrawal_fee
    return balance


def calculate_interest(balance: float) -> float:
    interest = balance * 0.03
    balance += interest
    return balance


def calculate_wealth_tax(balance: float) -> float:
    wealth_tax = balance * 0.1
    balance -= wealth_tax
    return balance


def main():
    balance = 0
    action_count = 0

    while True:
        action = input("Введите действие (пополнить, снять, выйти): ")

        if action == "пополнить":
            amount = int(input("Введите сумму для пополнения: "))
            if amount % 50 != 0:
                print("Ошибка: некорректная сумма пополнения, надо число кратное 50ти")
                continue

            balance = deposit(balance, amount)
            action_count += 1

        elif action == "снять":
            amount = int(input("Введите сумму для снятия: "))
            if amount % 50 != 0:
                print("Ошибка: некорректная сумма снятия")
                continue

            if balance >= 5_000_000:
                balance = calculate_wealth_tax(balance)

            balance = withdraw(balance, amount)
            action_count += 1

        elif action == "выйти":
            break

        else:
            print("Ошибка: некорректное действие")
            continue

        if action_count % 3 == 0:
            balance = calculate_interest(balance)

        print(f"Текущий баланс: {balance}")


if __name__ == "__main__":
    main()