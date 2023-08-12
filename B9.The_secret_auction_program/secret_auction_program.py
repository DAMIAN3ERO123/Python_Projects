from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

print("\nWelcome to the secret auction program.")

biders = {}
more_biders = "yes"

def add_biders(nombre,puja):
  biders[nombre] = puja 

def whowin():
  winer = ""
  amount = 0
  for person in biders:
    if biders[person] > amount:
      amount = biders[person]
      winer = person
  print(winer)
  
while more_biders == "yes":
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  more_biders = input('Are there any other biders? Type "yes" or "no". ')
  add_biders(name,bid)
  clear()


whowin()
