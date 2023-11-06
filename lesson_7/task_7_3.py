"""Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел.
В новый файл сохраните имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю;
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла, возвращайтесь в его начало.
"""


def multiply_numbers_and_names(numbers_file, names_file, output_file):
    with open(numbers_file, "r") as numbers_file, \
            open(names_file, "r") as names_file, \
            open(output_file, "w") as output_file:
        numbers = numbers_file.readlines()
        names = names_file.readlines()
        longer_length = max(len(numbers), len(names))

        for i in range(longer_length):
            number = numbers[i % len(numbers)].strip()
            name = names[i % len(names)].strip()
            
            num1, num2 = number.split('|')
            num1 = int(num1)
            num2 = float(num2)
            
            product = num1 * num2
            
            if product < 0:
                name = name.lower()
                product = abs(product) % 10
            else:
                name = name.upper()
                product = round(product)
                
            output_file.write(f"{name} {product}\n")


multiply_numbers_and_names("./lesson_7/data.txt", "./lesson_7/names.txt", "./lesson_7/output.txt")
