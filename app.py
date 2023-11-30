import random

game = True

score =  0

options = {
    "r":"rock", 
    "p":"paper", 
    "s":"scissors"
}

while game:

    # Game code

    # rock, paper, scissors
    # get user input
    user = input("rock (r), paper (p) or scissors (s)? ")

    if user not in list(options.keys()):
        # invalid input
        print("Invalid input, try again.")
        continue

    # get computer input
    computer = random.choice(list(options.keys()))

    print("You chose", options[user], "and the computer chose", options[computer])
    # compare user and computer input
    if user == computer:
        print("It's a tie!")
    elif user == "r" and computer == "s":
        print("You win!")
        score = score + 1
    elif user == "p" and computer == "r":
        print("You win!")
        score = score + 1
    elif user == "s" and computer == "p":
        print("You win!")
        score = score + 1
    else:
        print("You lose!")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n) ")

    if play_again == "n":
        game = False

print("Your score is", score)
