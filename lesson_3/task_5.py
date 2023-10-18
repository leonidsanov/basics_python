"""
Создайте вручную список с повторяющимися целыми числами. 
Сформируйте список с порядковыми номерами нечётных элементов исходного списка. 
Нумерация начинается с единицы.
"""

data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
result = []

for i, item in enumerate(data, start=1):
    if item % 2 != 0:
        result.append(i)

print(f"{data = }\n{result = }")
