import random

while True:
    choices = ["rock", "paper", "scizors"]

    computer = random.choice(choices)

    player = None

    try:
        while player not in choices:
            player = str(input("Rock, paper or scizors? ")).lower()
        print("You've chosen " + player )
    except Exception:
        print("Something went wrong :(\nPlease, try again")

    print("The computer has chosen " + computer)

    if player == computer:
        print("It's a tie.")
    elif player == "rock":
        if computer == "paper":
            print("Player defeated.")
        else:
            print("Computer defeated.")
    elif player == "scizors":
        if computer == "rock":
            print("Player defeated.")
        else:
            print("Computer defeated.")
    elif player == "paper":
        if computer == "scizors":
            print("Player defeated.")
        else:
            print("Computer defeated.")
    
    play_again = str(input("Play again? (yes/no) ")).lower()

    if play_again != "yes":
        break

print("Thanks for playing :)")