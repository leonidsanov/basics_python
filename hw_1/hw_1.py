'''
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
'''
a = float(input("Введите сторону a: ")) 
b = float(input("Введите сторону b: ")) 
c = float(input("Введите сторону c: ")) 
 
if a >= b + c or b >= a + c or c >= a + b:
    print("Треугольника с такими сторонами не существует") 
else: 
    print("Треугольник существует")
    if a != b != c:
        print('Треугольник разностороний')
    elif a == b != c or a == c != b or a != b == c:
        print('Треугольник равнобедренный')
    else:
        a == b == c
        print('Треугольник равностороний')