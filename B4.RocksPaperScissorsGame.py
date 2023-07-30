import random

player=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
Scissors=('''\n    -------\n---'   ____)____\n           _____)\n       __________)\n      (_____)\n---.__(___)''')
Rock=('''\n    -------\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)''')
Paper=('''\n    ______\n---'   ___)____\n       ________)\n       __________)\n       _________)\n---._______)''')

if player < 0 or player > 2:
    print("You lose, you choosed a invalid number")
else:
    Games_images=[Rock,Paper,Scissors]
    print(Games_images[player])

    computer=random.randint(0,2)
    print(f"\nComputer chose:\n{Games_images[computer]}")

    if computer == 0 and player == 2:
        print("\nYou lose")
    elif computer == 2 and player == 1:
        print("\nYou lose")
    elif computer == 1 and player == 0:
        print("\nYou lose")
    elif computer == player:
        print("\nWas a draw")
    else:
        print("\nCongratulations, you win")
