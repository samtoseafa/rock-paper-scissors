import random, sys

choices = ["rock", "paper", "scissors"]
sys.stdout.write(
    "*****************************************************************************\n"
)
sys.stdout.write("Welcome to Rock, Paper, Scissors!\n")
sys.stdout.write("To play, enter your choice: Rock, Paper, or Scissors\n")
sys.stdout.write(
    "If you win, you score 5 points, a tie is 1 point, and a loss is 2 points.\n"
)
sys.stdout.write("To quit, type in 'quit'\n")
sys.stdout.write("To see your score, type in 'score'\n")
sys.stdout.write(
    "*****************************************************************************\n"
)
score = 0

while True:
    user_choice = input("Type in your choice: ")
    computer_choice = random.choice(choices)
    # exit
    if user_choice.lower() == "quit":
        break
    # see score
    if user_choice.lower() == "score":
        sys.stdout.write(f"You have earned {score} points\n")
        continue
    # invalid input
    if user_choice.lower() not in choices:
        print("Please enter a valid choice.\n")
        continue
    # tied cases
    elif user_choice.lower() == computer_choice:
        score += 1
        sys.stdout.write(f"Computer chose {user_choice} as well- that's a tie!\n")
    # losing cases
    elif (
        (user_choice.lower() == "rock" and computer_choice == "paper")
        or (user_choice.lower() == "scissors" and computer_choice == "rock")
        or (user_choice.lower() == "paper" and computer_choice == "scissors")
    ):
        score -= 2
        sys.stdout.write(f"Computer chose {computer_choice}- you lose!\n")
    # winning cases
    elif (
        (user_choice.lower() == "paper" and computer_choice == "rock")
        or (user_choice.lower() == "rock" and computer_choice == "scissors")
        or (user_choice.lower() == "scissors" and computer_choice == "paper")
    ):
        score += 5
        sys.stdout.write(f"Computer chose {computer_choice}- you win!\n")

sys.stdout.write(
    "*****************************************************************************\n"
)
sys.stdout.write(f"You have earned {score} points overall!\n")
sys.stdout.write("Thanks for playing!\n")
sys.stdout.write(
    "*****************************************************************************\n"
)
