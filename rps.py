import random
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid input. Please enter rock, paper, or scissors.")
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "User wins"
    else:
        return "Computer wins"
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")
    print(winner)
def play_multiple_rounds():
    user_score = 0
    computer_score = 0
    while True:
        play_game()
        winner = determine_winner(get_user_choice(), get_computer_choice())
        if winner == "User wins":
            user_score += 1
        elif winner == "Computer wins":
            computer_score += 1
        print(f"Score-")
play_game()