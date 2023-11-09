"""Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
"""


import json
import csv

# Open the JSON file and load the users dictionary
with open("users.json", "r") as f:
    users = json.load(f)

# Open the CSV file and create a writer object
with open("users.csv", "w") as f:
    writer = csv.writer(f)

    # Write the header row with the column names
    writer.writerow(["Name", "ID", "Access Level"])

    # Loop through the users dictionary and write each user as a row
    for level, ids in users.items():
        for user_id, name in ids.items():
            writer.writerow([name, user_id, level])

    # Print a message about successful saving
    print("The users data has been saved to the CSV file.")
