from replit import clear
import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo,stages
print(f"{logo}\n")
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
      print(f'You\'ve already guessed the letter "{guess}", choose other one')
    else:
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
  
      if guess not in chosen_word:
          print(f"The letter \"{guess}\" is not part of the word to be guessed")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print("You lose.")
      print(f"{' '.join(display)}")
  
      if "_" not in display:
          end_of_game = True
          print("You win.")
        
      print(stages[lives])

