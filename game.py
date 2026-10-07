import random

number = random.randint(1, 10)

guess = int(input("Угадай число от 1 до 10: "))

if guess == number:
    print("Ты угадал!")
else:
    print("Не угадал. Было число:", number)
