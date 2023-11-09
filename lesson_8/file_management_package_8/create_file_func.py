"""A function that fills a file (adds to the end) with random pairs of numbers.
The first int number and the second float number are separated by a vertical line.
The minimum number is -1000 and the maximum number is +1000.
The number of lines and file name are passed as function arguments.
"""


import random
import string


def fill_file_with_random_pairs(filename, num_lines):
    with open(filename, "a") as file:
        for _ in range(num_lines):
            int_num = random.randint(-1000, 1000)
            float_num = round(random.uniform(-1000, 1000), 2)
            line = f"{int_num}|{float_num}\n"
            file.write(line)


"""A function that generates pseudo-names.
The name starts with a capital letter, consists of 4-7 letters, among which there are vowels.
The generated names are saved to a file.
"""


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


"""A function that opens created files with numbers and names for reading.
Multiplies pairs of numbers.
It saves the name and product to the new file:
if the result of multiplication is negative, saves the name written in lowercase letters and the product modulo;
if the result of multiplication is positive, saves the name in capital letters and the product rounded to integer.
The resulting file has the same number of lines as the longer file.
When it reaches the end of the shorter file, it returns to its beginning.
"""


def multiply_numbers_and_names(numbers_file, names_file, output_file):
    with open(numbers_file, "r") as numbers_file, \
            open(names_file, "r") as names_file, \
            open(output_file, "w") as output_file:
        numbers = numbers_file.readlines()
        names = names_file.readlines()
        longer_length = max(len(numbers), len(names))

        for i in range(longer_length):
            number = numbers[i % len(numbers)].strip()
            name = names[i % len(names)].strip()
            
            num1, num2 = number.split('|')
            num1 = int(num1)
            num2 = float(num2)
            
            product = num1 * num2
            
            if product < 0:
                name = name.lower()
                product = abs(product) % 10
            else:
                name = name.upper()
                product = round(product)
                
            output_file.write(f"{name} {product}\n")


if __name__ == '__main__':
    fill_file_with_random_pairs('./lesson_8/generated_files/data.txt', 10)
    generate_pseudo_names("./lesson_8/generated_files/names.txt", 10)
    multiply_numbers_and_names("./lesson_8/generated_files/data.txt", "./lesson_8/generated_files/names.txt", "./lesson_8/generated_files/output.txt")
