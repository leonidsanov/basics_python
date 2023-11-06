"""Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.
"""


import random
import string
import os


def fill_file_with_random_pairs(filename, num_lines):
    with open(filename, "a") as file:
        for _ in range(num_lines):
            int_num = random.randint(-1000, 1000)
            float_num = round(random.uniform(-1000, 1000), 2)
            line = f"{int_num}|{float_num}\n"
            file.write(line)


"""Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
Полученные имена сохраните в файл.
"""


def generate_pseudo_names(filename, num_names):
    vowels = "AEIOU"
    consonants = "".join(set(string.ascii_uppercase) - set(vowels))
    names = []
    
    while len(names) < num_names:
        name_length = random.randint(4, 7)
        name = random.choice(consonants)
        
        for _ in range(name_length-1):
            if len(name) == name_length-1 and len(set(name) & set(vowels)) == 0:
                name += random.choice(vowels)
            else:
                name += random.choice(string.ascii_uppercase)
        
        names.append(name)
    
    with open(filename, "w") as file:
        for name in names:
            file.write(f"{name}\n")


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


def create_files_with_extension(extension: list[str], min_name_length=6, max_name_length=30, min_file_size=256, max_file_size=4096, num_files=42, directory='./hw_7/hw_files/'):
    # Create the directory if it doesn't exist
    # directory = './lesson_7/random_files/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    for _ in range(num_files):
        # Generate a random file name with the specified length
        file_name_length = random.randint(min_name_length, max_name_length)
        file_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(file_name_length)) + str(extension)

        # Generate a random file size between the specified min and max size
        file_size = random.randint(min_file_size, max_file_size)

        # Create the file
        with open(f'{directory}/{file_name}', 'wb') as file:
            # Generate random bytes to write to the file
            bytes_to_write = os.urandom(file_size)
            file.write(bytes_to_write)

        print(f"Created '{file_name}' with size {file_size} bytes.")


"""Доработаем предыдущую задачу.
Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи.
"""


from random import randint, choice
from os import mkdir

def gen_random_files(
    min_len_name: int = 6,
    max_len_name: int = 30,
    min_count_bytes: int = 256,
    max_count_bytes: int = 4096,
    files_count: int = 42,
    extensions: list[str] = None,
    path: str = './hw_7/hw_files/',
):

    for _ in range(files_count):
        extension = choice(extensions)
        filename = create_files_with_extension(min_len_name, max_len_name, directory=path)
        try:
            write_to_file(path, filename, extension, min_count_bytes, max_count_bytes)
        except FileNotFoundError:
            mkdir(path)
            write_to_file(path, filename, extension, min_count_bytes, max_count_bytes)


def gen_random_files_with_extensions(
    extensions: list[str], num_files: int, path: str = './hw_7/hw_files/'
):
    gen_random_files(extensions=extensions, files_count=num_files, path=path)


def write_to_file(path, filename, extension, min_count_bytes, max_count_bytes):
    with open(f"{path}/{filename + extension}", "w") as file:
        data = bytes(
            randint(1, 255) for _ in range(randint(min_count_bytes, max_count_bytes))
        )
        file.write(str(data))


gen_random_files_with_extensions(
    extensions=[".txt", ".md", ".csv", ".json"], num_files=12
)


"""Дорабатываем функции из предыдущих задач.
Генерируйте файлы в указанную директорию — отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""


def create_random_filename(min_len_name=6, max_len_name=30):
    name_length = random.randint(min_len_name, max_len_name)
    random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=name_length))
    return random_name


def write_to_file(directory, filename, extension, min_count_bytes=256, max_count_bytes=4096):
    file_path = os.path.join(directory, f"{filename}.{extension}")
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as file:
            count_bytes = random.randint(min_count_bytes, max_count_bytes)
            file.write(os.urandom(count_bytes))


def generate_files_with_extension(extensions, files_count, **kwargs):
    for extension, count in zip(extensions, files_count):
        for _ in range(count):
            filename = create_random_filename()
            write_to_file(kwargs["directory"], filename, extension)


# Example usage
extensions = ['txt', 'jpg', 'png']
files_count = [5, 10, 3]
kwargs = {
    "min_len_name": 6,
    "max_len_name": 30,
    "min_count_bytes": 256,
    "max_count_bytes": 4096,
    "directory": "./hw_7/hw_files/"
}


"""Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""

from os import listdir, mkdir, chdir, replace
from pathlib import Path


def get_exts(exts: list[str]) -> list[str]:
    exts = set(map(lambda x: x.split('.')[-1], exts))
    return list(exts)


def sort_files(working_dir: str = './hw_7/hw_files/'):
    exts = get_exts(listdir(Path(working_dir)))
    chdir(Path(working_dir))
    for ext in exts:
        try:
            mkdir(ext)
        except FileExistsError:
            pass
    for file in filter(lambda x: x.find('.') != -1, listdir()):
        prev = Path(file)
        prev.replace(Path.cwd() / file.split('.')[-1] / prev)


if __name__ == "__main__":
    fill_file_with_random_pairs("./hw_7/hw_files/data.txt", 10)
    generate_pseudo_names("./hw_7/hw_files/names.txt", 10)
    multiply_numbers_and_names("./hw_7/hw_files/data.txt", "./hw_7/hw_files/names.txt", "./hw_7/hw_files/output.txt")
    create_files_with_extension(".txt")
    gen_random_files_with_extensions(extensions=[".txt", ".md", ".csv", ".json"], num_files=12)
    sort_files()
