import random

def play_guess_the_number():
    # Задаем минимальное и максимальное число 
    min_number = 1
    max_number = 1000


    # Компьютер загадывает число
    secret_number = random.randint(min_number, max_number)

    print(f"Я загадал случайное число от {min_number} до {max_number}! Попробуй его угадать!")

    while True:
        # получаем число игрока
        guess = int(input("Введите свое число: "))


        # проверяем в диапазоне ли число игрока
        if min_number <= guess <= max_number:
            # проверки на победу а так эе на больше меньше 
            if guess == secret_number:
                print("Поздравляю! Ты угадал число!")
                break
            elif guess < secret_number:
                print("Загаданное число больше!")
            elif guess > secret_number:
                print("Загаданное число меньше!")
        else: 
            print(f"Загаданное число должно быть в диапазоне от {min_number} до {max_number}")

if __name__ == "__main__":
    play_guess_the_number()



