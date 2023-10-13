"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

decimal_num = int(input('Введите число в десятичной системе: '))
print(f'Встроенная функция hex: {hex(decimal_num)}')


def decimal_to_hex(decimal_number):
    hex_digits = "0123456789abcdef"
    result = ""
    
    while decimal_number > 0:
        remainder = decimal_number % 16
        result = hex_digits[remainder] + result
        decimal_number = decimal_number // 16
    
    return '0x' + result

hex_num = decimal_to_hex(decimal_num)
print(f'Пользовательская функция decimal_to_hex: {hex_num}')


"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions
"""
import fractions

def add_fractions(fraction1, fraction2):
    num1, den1 = map(int, fraction1)
    num2, den2 = map(int, fraction2)

    result_num = (num1 * den2) + (num2 * den1)
    result_den = den1 * den2

    return f"{result_num}/{result_den}"

def multiply_fractions(fraction1, fraction2):
    num1, den1 = map(int, fraction1)
    num2, den2 = map(int, fraction2)

    result_num = num1 * num2
    result_den = den1 * den2

    return f'{result_num}/{result_den}'

# Ввод дробей
fraction1 = input('Введите первую дробь в виде "a/b": ').split('/')
fraction2 = input('Введите вторую дробь в виде "a/b": ').split('/')

sum_of_fractions = add_fractions(fraction1, fraction2)
product_of_fractions = multiply_fractions(fraction1, fraction2)

print(f'Сумма дробей составляет: {sum_of_fractions}')
print(f'Произведение дробей равно: {product_of_fractions}')

print(f'Проверяем через модуль fractions')
f1 = fractions.Fraction(int(fraction1[0]), int(fraction1[1]))
print(f'Первая дробь: {f1}')
f2 = fractions.Fraction(int(fraction2[0]), int(fraction2[1]))
print(f'Вторая дробь: {f2}')
print(f'Сложение дробей: {f1 + f2}')
print(f'Произведение дробей: {f1 * f2}')
