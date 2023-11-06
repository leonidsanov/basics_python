"""Доработаем предыдущую задачу.
Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи.
"""


from task_7_4 import create_files_with_extension
from random import randint, choice
from os import mkdir

def gen_random_files(
    min_len_name: int = 6,
    max_len_name: int = 30,
    min_count_bytes: int = 256,
    max_count_bytes: int = 4096,
    files_count: int = 42,
    extensions: list[str] = None,
    path: str = './lesson_7/files_for_task5',
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
    extensions: list[str], num_files: int, path: str = './lesson_7/files_for_task5'
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
