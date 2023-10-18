"""
Создайте вручную кортеж содержащий элементы разных типов. 
Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
"""

data = (42, 73, 3.14, "Hello world!", None, True, "Text", 100500.2, False)
result = {}
for item in data:
    key = result.setdefault(type(item), list())
    key.append(item)

print(result)
