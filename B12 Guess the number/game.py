from art import logo
import random
import replit

game_is_running = True

def game(number_attempts,random_number):
  is_attempts = True
  while is_attempts:
    print(f"You have {number_attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if random_number == guess:
      print(f"You got it! The answer is {random_number}")
      is_attempts = False
    elif random_number != guess and number_attempts != 0:
      number_attempts -= 1
      if guess > random_number:
        print("Too high")
        if number_attempts == 0:
          is_attempts = False
          print("You've run out of guesses, you lose.")
        else:
          print("Guess again")
      else:
        print("Too low.")
        if number_attempts == 0:
          is_attempts = False
          print("You've run out of guesses, you lose.")
        else:
          print("Guess again")
   
while game_is_running:
  print(logo)
  random_num = random.randint(1,100)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  #print(f"Pssst, the correct aswer is {random_num}")
  difficulty = input("Choose the difficulty, Type 'easy' or 'hard': ")

  if difficulty == 'easy':
    attempts = 10
    game(attempts,random_num)
    continue_game = input("Do you want to play again 'y' o 'n' ")
    if continue_game == 'n':
      game_is_running = False
    else:
      replit.clear()
  else:
    attempts = 5
    game(attempts,random_num)
    continue_game = input("Do you want to play again 'y' o 'n' ")
    if continue_game == 'n':
      game_is_running = False
    else:
      replit.clear()
