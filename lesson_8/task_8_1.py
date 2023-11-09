"""Вспоминаем задачу 3 из прошлого семинара.
Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""


import json
from file_management_package_8.create_file_func import multiply_numbers_and_names as mnn
from file_management_package_8.create_file_func import fill_file_with_random_pairs as ffp
from file_management_package_8.create_file_func import generate_pseudo_names as gpn


# def convert_to_json(file_path, output_file_path):
#     with open(file_path, 'r') as file:
#         data = []
#         for line in file:
#             name, number = line.strip().split(':')
#             capitalized_name = name.capitalize()
#             data.append({'Name': capitalized_name, 'Number': int(number)})

#     with open(output_file_path, 'w') as output_file:
#         json.dump(data, output_file, indent=4)

# # Example usage
file_path = './lesson_8/generated_files/output.txt'  # Replace with your file's path
output_file_path = './lesson_8/generated_files/output_file_json.json'  # Replace with your desired output file path

# def create_new_file(old_file, new_file):
#     # open the old file in read mode
#     with open(old_file, "r") as f:
#         # load the data as a dictionary
#         data = json.load(f)
#     # open the new file in write mode
#     with open(new_file, "w") as f:
#         # iterate over the key-value pairs in the data
#         for key, value in data.items():
#             # capitalize the key and the value
#             key = key.capitalize()
#             #value = value.capitalize()
#             # write the pair on a new line, separated by a colon
#             f.write(f"{key}: {value}\n")

# Import the json module
#import json

# Define the function
def create_new_file(old_file, new_file):
    # Open the old file in read mode
    with open(old_file, "r") as f:
        # Load the data as a dictionary
        data = dict(map(lambda x: tuple(x.split()),
                          f.read().split('\n')))
        data = json.load(f)
    # Open the new file in write mode
    with open(new_file, "w") as f:
        # Loop through the data items
        for key, value in data.items():
            # Capitalize the names
            key = key.title()
            #value = value.title()
            # Write the pair on a new line
            f.write(f"{key}: {value}\n")
    # Return a message
    return f"New file {new_file} created successfully."

# Example usage
#create_new_file("old.json", "new.txt")


# def txt_json(src_file: str = 'text.txt',
#              out_file: str = 'text.json'):
#     """Импорт данных из .txt в .json"""
#     with open(src_file, 'r') as file:
#         names = dict(map(lambda x: tuple(x.split()),
#                          file.read().split('\n')))

#     with open(out_file, 'w') as file:
#         json.dump(names, file, indent=4)


if __name__ == '__main__':
    print("Генерируем псевдоимена и сохраняем их в файл names.txt")
    pseudo_names = gpn("./lesson_8/generated_files/names.txt", 10)
    print("Создаём пары чисел")
    random_pairs = ffp('./lesson_8/generated_files/data.txt', 10)
    print('Создаём файл с числами и именами')
    multiply_numbers = mnn("./lesson_8/generated_files/data.txt", "./lesson_8/generated_files/names.txt", "./lesson_8/generated_files/output.txt")
    print("Создание файла в формате JSON")
    # convert_to_json(file_path, output_file_path)
    create_new_file(file_path, output_file_path)
    #txt_json(file_path, output_file_path)


