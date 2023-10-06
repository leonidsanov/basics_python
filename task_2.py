'''
Посчитайте сумму чётных элементов от 1 до n исключая кратные e. 
Используйте while и if. 
Попробуйте разные значения e и n.
'''
n = 10
i = 0
e = 3
s = 0

while i <= n:
    i += 1
    if i%2 == 0:
        if i%e == 0:
            continue
        else:
            s += i
print(s)


def sum_of_even_numbers(n, e):
    i = 1
    total_sum = 0

    while i <= n:
        if i % 2 == 0 and i % e != 0:
            total_sum += i
        i += 1

    return total_sum


n = int(input("Введите значение для n: "))
e = int(input("Введите значение для e: "))

result = sum_of_even_numbers(n, e)
print(f"Сумма четных чисел от 1 до {n}, исключая кратные {e}, равна: {result}")