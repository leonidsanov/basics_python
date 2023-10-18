"""
Пользователь вводит данные.
Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
Целое положительное число
Вещественное положительное или отрицательное число
Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
Строку в верхнем регистре в остальных случаях
"""

data = input("Введите данные: ")

if data.isdecimal():
    result = int(data)
elif (
    data.replace(".", "").replace("-", "").isdecimal()
    and data.count(".") == 1
    and data.count("-") <= 1
    and data[1:].count("-") == 0
):
    result = float(data)
elif data != data.lower():
    result = data.lower()
else:
    result = data.upper()

print(f"{result = }")
