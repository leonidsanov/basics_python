"""Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
"""


from file_management_package import hw_func as hf

if __name__ == '__main__':
    print("Переименование txt файлов в каталоге data_files")
    files_cnt = hf.group_rename_files("_fn_", ".txt", path="./hw_7/hw_files/")
    print(f"Переименовано: {files_cnt}")