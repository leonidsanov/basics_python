"""
Создайте несколько переменных разных типов. 
Проверьте к какому типу относятся созданные переменные.
"""

a = 5
b = 'abc'
c = True
d = [1, 2, 'acjhfjfh', True, [34, 6.8, 'jhg']]
e = {a:6, (b, 'text', False):{c:False}}
f = frozenset([1, 2, 'three'])

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
