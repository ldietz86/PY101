import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

WINNING_COMBOS = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["scissors", "rock"]
}

def prompt(message): 
    print(f"==> {message}")

def determine_winner(player_choice, computer):
    prompt(f"You chose {player_choice}, computer chose {computer}")

    if computer in WINNING_COMBOS[player_choice]:
        return "player"
    return "computer"

def get_user_choice():
    while True:
        prompt('''Choose: rock (r), paper (p), scissors (s),
        lizard (l), or spock (sp): ''')
        player_choice = input().lower()

        match player_choice:
            case "r":
                return "rock"
            case "p":
                return "paper"
            case "s":
                return "scissors"
            case "l":
                return "lizard"
            case "sp":
                return "spock"
            case "rock" | "paper" | "scissors" | "lizard" | "spock":
                return choice
            case _:
                prompt("Invalid choice. Please try again.")

player_score = 0
computer_score = 0

while True:
    choice = get_user_choice()

    computer_choice = random.choice(VALID_CHOICES)

    result = determine_winner(choice, computer_choice)

    if result == "player":
        player_score += 1
        prompt("You won this round!")
    elif result == "computer":
        computer_score += 1
        prompt("Computer won this round!")
    else:
        prompt("It's a tie!")

    prompt(f"Current score: {player_score} - {computer_score}")

    if player_score == 3:
        prompt("Congrats, you won the game!")
        break

    if computer_score == 3:
        prompt("Computer won the game!")
        break