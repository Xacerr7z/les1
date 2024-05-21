import random

def get_player_choice():
    while True:
        choice = input("введите свой выбор (камень, ножнецы, бумага): ").lower()
        if choice in ("камень", "ножнецы", "бумага"):
            return choice
        else:
            print("Неверный выбор. Пожалуйста введите один из вариантов (камень, ножнецы бумага)")


def get_computer_choice():
    choices = ["камень", "ножнецы", "бумага"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Нечья"
    elif player_choice == "камень" and computer_choice == "ножницы":
        return "Победа игрока"
    elif player_choice == "камень" and computer_choice == "бумага":
        return "Победа кампьютара"
    elif player_choice == "ножнецы" and computer_choice == "бумага":
        return "Победа игрока"
    elif player_choice == "ножнецы" and computer_choice == "камень":
        return "Победа компьютера"
    elif player_choice == "бумага" and computer_choice == "камень":
        return "Победа игрока"
    else:
        return "Неверный выбор"

def play_game():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()


    print(f"вы выбрали {player_choice}")
    print(f"компьютер выбрал {computer_choice}")


    result = determine_winner(player_choice,computer_choice)
    print(result)

play_game()

















