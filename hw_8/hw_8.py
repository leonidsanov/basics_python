"""Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
- Для дочерних объектов указывайте родительскую директорию.
- Для каждого объекта укажите файл это или директория.
- Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""


import os
import json
import csv
import pickle

# Define a function that takes a directory name as an argument
def traverse_directory(directory):
    # Create an empty list to store the results
    results = []

    # Loop through the files and subdirectories in the directory
    for entry in os.scandir(directory):
        # Create a dictionary to store the information about the entry
        info = {}

        # Store the name and the parent directory of the entry
        info["name"] = entry.name
        info["parent"] = entry.path

        # Check if the entry is a file or a directory
        if entry.is_file():
            # Store the type as "file" and the size in bytes
            info["type"] = "file"
            info["size"] = entry.stat().st_size
        elif entry.is_dir():
            # Store the type as "directory" and the size as zero
            info["type"] = "directory"
            info["size"] = 0

            # Recursively traverse the subdirectory and get the nested results
            nested_results = traverse_directory(entry.path)

            # Add the size of the nested files and directories to the current size
            for nested_info in nested_results:
                info["size"] += nested_info["size"]

            # Extend the results list with the nested results
            results.extend(nested_results)

        # Append the info dictionary to the results list
        results.append(info)

    # Return the results list
    return results

# Call the function with the directory name and get the results
results = traverse_directory("./hw_8/test")

# Save the results to a JSON file
with open("./hw_8/generated_files/results.json", "w") as f:
    json.dump(results, f, indent=4)

# Save the results to a CSV file
with open("./hw_8/generated_files/results.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "parent", "type", "size"])
    writer.writeheader()
    writer.writerows(results)

# Save the results to a pickle file
with open("./hw_8/generated_files/results.pickle", "wb") as f:
    pickle.dump(results, f)
