import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator!")
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

total_char = nr_letters + nr_symbols + nr_numbers

password = ""

for char in range (total_char,0, -1):
    rand_selection = random.randint(1,3)
    if rand_selection == 1 and nr_letters > 0:
        rand_letter = random.randint(0,51)
        password += letters[rand_letter] 
        nr_letters -= 1      
    elif rand_selection == 2 and nr_symbols > 0:
        rand_symbol = random.randint(0,8)
        password += symbols[rand_symbol]
        nr_symbols -= 1
    else:
        rand_number = random.randint(0,9)
        password += numbers[rand_number]
        nr_numbers -= 1

print(f"\n{password}") 
