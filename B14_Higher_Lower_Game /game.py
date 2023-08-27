from art import logo,vs
from game_data import data
import random
from replit import clear

def choose_option():
  """Elige un elemento al azar de la lista data"""
  return random.choice(data)

def more_followers(followers_A,followers_B):
  """ Devuelte el elemento de la lista con mayores seguidores"""
  if followers_A['follower_count'] > followers_B['follower_count']:
    return followers_A
  else: 
    return followers_B

def wall(option_A,option_B):
  """ Imprime la presentación que se le da al jugador """
  print(f"Compare A: {option_A['name']}, a {option_A['description']}, from {option_A['country']}")
  print(vs)
  print(f"Compare B: {option_B['name']}, a {option_B['description']}, from {option_B['country']}")

def players_game(option_A,option_B):
  """ Le permite al jugar escoger su opción """
  player_choice=input("Who has more followers? Type 'A' or 'B': ").upper()
  if player_choice == 'A':
    player_choice = option_A
    return player_choice
  else:
    player_choice = option_B
    return player_choice

def play_game(option_A,option_B):
  """Inicial el juego principal"""
  print(logo)
  if score != 0:
    print(f"You're right! Current score: {score}")
  wall(option_A,option_B)
  player_choice_final = players_game(option_A,option_B)
  return player_choice_final


score = 0
continue_game = True
while continue_game:

  if score == 0:
    option_A = choose_option()
    option_B = choose_option()
    if option_A == option_B:
      option_B = choose_option()
    player_choice_final = play_game(option_A,option_B)
  else:
    option_A = option_B
    option_B = choose_option()
    if option_A == option_B:
      option_B = choose_option()
    player_choice_final = play_game(option_A,option_B)
    
  winner = more_followers(option_A,option_B)
  
  if player_choice_final['name'] == winner['name']:
    clear()
    score += 1
  
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    continue_game = False
