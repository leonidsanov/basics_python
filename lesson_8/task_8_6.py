"""Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""


import pickle
import csv

# Define a function that takes the pickle file name and the csv file name as arguments
def convert_pickle_to_csv(pickle_file, csv_file):
    # Open the pickle file and load the data
    with open(pickle_file, "rb") as f:
        data = pickle.load(f)

    # Check if the data is a list of dictionaries
    if isinstance(data, list) and all(isinstance(d, dict) for d in data):
        # Open the csv file and create a writer object
        with open(csv_file, "w") as f:
            writer = csv.writer(f)

            # Extract the dictionary keys for the header row
            header = list(data[0].keys())

            # Write the header row to the csv file
            writer.writerow(header)

            # Loop through the data list and write each dictionary as a row
            for d in data:
                # Extract the dictionary values for the row
                row = list(d.values())

                # Write the row to the csv file
                writer.writerow(row)

        # Print a message about successful conversion
        print(f"The pickle file {pickle_file} has been converted and saved as {csv_file}.")
    else:
        # Print a message about invalid data format
        print(f"The pickle file {pickle_file} does not contain a list of dictionaries.")
