'''
Решите квадратное уравнение 5x2-10x-400=0 через дискриминант последовательно 
сохраняя переменные a, b, c, d, x1 и x2.
*Попробуйте решить уравнения с другими значениями a, b, c.
'''
a = 5
b = -10
c = -400
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(f'x1 = {x1}, x2 = {x2}')
elif d==0:
    x = -b / (2 * a)
    print(f'x = {x}')
else:
    print('Корней нет.')