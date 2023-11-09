"""Напишите функцию, которая ищет json файлы в указанной директории и
сохраняет их содержимое в виде одноимённых pickle файлов.
"""


import json
import pickle
import os

# Define a function that takes the directory name as an argument
def convert_json_to_pickle(directory):
    # Loop through the files in the directory
    for file in os.listdir(directory):
        # Check if the file has a .json extension
        if file.endswith(".json"):
            # Open the JSON file and load the data
            with open(os.path.join(directory, file), "r") as f:
                data = json.load(f)

            # Create a new file name with a .pickle extension
            new_file = file.replace(".json", ".pickle")

            # Open the pickle file and dump the data
            with open(os.path.join(directory, new_file), "wb") as f:
                pickle.dump(data, f)

            # Print a message about successful conversion
            print(f"The JSON file {file} has been converted and saved as {new_file}.")