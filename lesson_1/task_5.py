"""
Нарисовать в консоли ёлку спросив 
у пользователя количество рядов. 
Пример результата:
Сколько рядов у ёлки? 5
    *
   ***
  *****
 *******
*********
"""

rows = int(input('Ввелите количество рядов: '))

for i in range(rows):
    spacenum = (rows - 1 - i)
    star_num = 2 * i + 1
    print(f'{" " * spacenum}{"*" * star_num}')


rows = int(input("Сколько рядов у ёлки? "))
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)