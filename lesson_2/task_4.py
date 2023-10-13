"""
Напишите программу, которая вычисляет площадь 
круга и длину окружности по введённому диаметру. 
Диаметр не превышает 1000 у.е. 
Точность вычислений должна составлять 
не менее 42 знаков после запятой.
"""

import math
import decimal

decimal.getcontext().prec = 50

p = decimal.Decimal(math.pi)
diameter = decimal.Decimal(input('Введите диаметр, не превышающий 1000 у.е.: '))
s = p * (diameter / 2) ** 2
l = p * diameter
print(f'Площадь круга: {s}. Длина окружности: {l}. Количество знаков: {len(str(s))}')

import math
import decimal

decimal.getcontext().prec = 50

p = decimal.Decimal(math.pi)
diameter = decimal.Decimal(input('Введите диаметр не более 1000: '))

print('Площадь', p * (diameter / 2) ** 2, len(str( p * (diameter / 2) ** 2)))
print('длина окружности', p * diameter)