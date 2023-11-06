"""Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
Полученные имена сохраните в файл.
"""


import random
import string

def generate_pseudo_names(filename, num_names):
    vowels = "AEIOU"
    consonants = "".join(set(string.ascii_uppercase) - set(vowels))
    names = []
    
    # Generate pseudo names until the desired number is reached
    while len(names) < num_names:
        name_length = random.randint(4, 7)
        name = random.choice(consonants)
        
        # Build the rest of the name based on the randomly chosen length
        for _ in range(name_length-1):
            # Check if the name has reached the desired length and there are no vowels present
            if len(name) == name_length-1 and len(set(name) & set(vowels)) == 0:
                name += random.choice(vowels)
            else:
                name += random.choice(string.ascii_uppercase)
        
        # Add the generated name to the list
        names.append(name)
    
    # Write the generated names to a file
    with open(filename, "w") as file:
        for name in names:
            file.write(f"{name}\n")

# Generate 10 pseudo names and write them to a file called "names.txt"
generate_pseudo_names("./lesson_7/names.txt", 10)
