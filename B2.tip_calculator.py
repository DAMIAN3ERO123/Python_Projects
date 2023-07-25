#Este programa calcula la propina de una cuenta, además, indica cuanto debe pagar cada persona si se divide la cuenta. 
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
ptip = int(input("What percentaje tip would you like to give? 10 12, or 15? "))
mpeople = input("How many people to split the bill? ")

bill = (bill * (ptip / 100) + bill) / int(mpeople)
#split = round(bill / int(mpeople),2)
bill = "{:.2f}".format(bill) 
print(f"Each person should pay: ${bill}")
