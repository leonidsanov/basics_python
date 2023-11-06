"""Дорабатываем функции из предыдущих задач.
Генерируйте файлы в указанную директорию — отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""

import os
import random
import string


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
    "directory": "./lesson_7/files_for_task6"
}

generate_files_with_extension(extensions, files_count, **kwargs)
