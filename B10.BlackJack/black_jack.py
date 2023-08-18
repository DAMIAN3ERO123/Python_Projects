import random
from replit import clear
from art import logo

def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(players_cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(players_cards) == 21 and len(players_cards) == 2:
    return 0
  if 11 in players_cards and sum(players_cards) > 21:
    players_cards.remove(11)
    players_cards.append(1)
    return sum(players_cards)
  return sum(players_cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, the opponent has BlackJack"
  elif user_score == 0:
    return "You win a BlackJack"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"

def play_game():

  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's fist card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:

      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"  Your final hand: {user_cards}, final_score: {user_score}")
  print(f"  Computer's final hand: {computer_cards}, final_score: {computer_score}")
  result = compare(user_score, computer_score)
  print(result)

while input("Do you want to play a game of BlackJack? Type 'y' or 'n' ") == 'y':
  clear()
  play_game()
  
