"""Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""


import json

# Open the JSON file if it exists, or create a new one
try:
    with open("users.json", "r") as f:
        users = json.load(f)
except FileNotFoundError:
    users = {}

# Function to check the uniqueness of the user ID
def is_unique_id(user_id):
    for level in users.values():
        if user_id in level:
            return False
    return True

# Function to request and add user information
def add_user():
    # Request name, ID and access level
    name = input("Enter name: ")
    user_id = input("Enter ID: ")
    access_level = input("Enter access level from 1 to 7: ")

    # Check the validity of the entered data
    if not name or not user_id or not access_level.isdigit():
        print("Invalid input format. Please try again.")
        return
    if not is_unique_id(user_id):
        print("This ID already exists. Please try again.")
        return
    if not 1 <= int(access_level) <= 7:
        print("Access level must be from 1 to 7. Please try again.")
        return

    # Add user information to the users dictionary
    if access_level not in users:
        users[access_level] = {}
    users[access_level][user_id] = name

    # Save the users dictionary to the JSON file
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

    # Print a message about successful addition
    print(f"User {name} with ID {user_id} and access level {access_level} successfully added.")

# Run an infinite loop to request and add user information
while True:
    add_user()
