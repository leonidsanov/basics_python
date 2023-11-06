"""Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
- расширение;
- минимальная длина случайно сгенерированного имени, по умолчанию 6;
- максимальная длина случайно сгенерированного имени, по умолчанию 30;
- минимальное число случайных байт, записанных в файл, по умолчанию 256;
- максимальное число случайных байт, записанных в файл, по умолчанию 4096;
- количество файлов, по умолчанию 42;
Имя файла и его размер должны быть в рамках переданного диапазона.
"""


import os
import random
import string

directory = './lesson_7/random_files/'

def create_files_with_extension(extension, min_name_length=6, max_name_length=30, min_file_size=256, max_file_size=4096, num_files=42, directory='./lesson_7/random_files/'):
    # Create the directory if it doesn't exist
    # directory = './lesson_7/random_files/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    for _ in range(num_files):
        # Generate a random file name with the specified length
        file_name_length = random.randint(min_name_length, max_name_length)
        file_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(file_name_length)) + extension

        # Generate a random file size between the specified min and max size
        file_size = random.randint(min_file_size, max_file_size)

        # Create the file
        with open(f'{directory}/{file_name}', 'wb') as file:
            # Generate random bytes to write to the file
            bytes_to_write = os.urandom(file_size)
            file.write(bytes_to_write)

        print(f"Created '{file_name}' with size {file_size} bytes.")

# Example usage
create_files_with_extension(".txt")
