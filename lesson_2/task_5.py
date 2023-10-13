"""
Напишите программу, которая решает квадратные уравнения даже если 
дискриминант отрицательный. 
Используйте комплексные числа 
для извлечения квадратного корня.
"""

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

#a = 5
#b = -10
#c = -400
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(f'x1 = {x1}, x2 = {x2}')
elif d==0:
    x = -b / (2 * a)
    print(f'x = {x}')
else:
    d = complex(d)
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(f'x1 = {x1}, x2 = {x2}')

###
import cmath

def solve_quadratic_equation(a, b, c):
    # Вычисляем дискриминант
    discriminant = b**2 - 4*a*c

    # Вычисляем корни уравнения
    x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    x2 = (-b - cmath.sqrt(discriminant)) / (2*a)

    return x1, x2

def main():
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))

    # Решаем квадратное уравнение
    solutions = solve_quadratic_equation(a, b, c)

    print("Корни квадратного уравнения:")
    print(f"x1 = {solutions[0]}")
    print(f"x2 = {solutions[1]}")


if __name__ == "__main__":
    main()