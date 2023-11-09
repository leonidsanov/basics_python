"""Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
"""


import json
import csv
import hashlib

# Define a function that takes the source and destination file names as arguments
def process_csv(source, destination):
    # Open the source CSV file and create a reader object
    with open(source, "r") as f:
        reader = csv.reader(f)

        # Skip the header row
        next(reader)

        # Create an empty list to store the processed records
        records = []

        # Loop through the reader object and process each row
        for row in reader:
            # Extract the name, ID and access level from the row
            name, user_id, access_level = row

            # Complete the ID up to 10 digits with leading zeros
            user_id = user_id.zfill(10)

            # Capitalize the first letter of the name
            name = name.capitalize()

            # Create a hash based on the name and ID using SHA256 algorithm
            hash = hashlib.sha256((name + user_id).encode()).hexdigest()

            # Create a dictionary with the processed fields
            record = {
                "Name": name,
                "ID": user_id,
                "Access Level": access_level,
                "Hash": hash
            }

            # Append the dictionary to the records list
            records.append(record)

    # Open the destination JSON file and write the records list
    with open(destination, "w") as f:
        json.dump(records, f, indent=4)

    # Print a message about successful processing
    print(f"The CSV file {source} has been processed and saved to the JSON file {destination}.")