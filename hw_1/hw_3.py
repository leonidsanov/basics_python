'''
Программа загадывает число от 0 до 1000.
Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
'''

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)
attempts = 10

for attempt in range(1, attempts + 1):
    # Предложить пользователю угадать
    guess = int(input("Attempt {}/{}: Guess the number between 0 and 1000: ".format(attempt, attempts)))
    # Проверьте, верно ли предположение
    if guess == num:
        print("Congratulations! You guessed the correct number in {} attempts.".format(attempt))
        break
    elif guess < num:
        print("The number is greater. Try again!")
    else:
        print("The number is smaller. Try again!")
    if attempt == attempts and guess != num:
        print("Sorry, you did not guess the correct number. The number was {}.".format(num))