import random

user = input("Enter your choice(rock, paper, scissors): ")

random_choice = ["rock", "paper", "scissors"]

computer = random.choices(random_choice)
print("Computer Choice is: ",computer)

if user == computer:
    print(" It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("Rock beats scissors! You win!")
    else:
        print("Paper beats rock! Computer wins.")
elif user == "paper":
    if computer == "rock":
        print("Paper beats rock! You win!")
    else:
        print("Scissors beats paper! Computer wins.")
elif user == "scissors":
    if computer == "paper":
        print("Scissors beats paper! You win!")
    else:
        print("Rock beats scissors! Computer wins.")