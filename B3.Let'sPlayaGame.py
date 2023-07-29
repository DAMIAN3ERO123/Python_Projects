print('''
0================================================0
|'.                    (|)                     .'|
|  '.                   |                    .'  |
|    '.                |O|                 .'    |
|      '. ____________/===\_____________ .'      |
|        :            `\"/`  ______     :     .. |
|        :     mmmmmmm  V   |--%%--|    :   .'|| |
|        :     |  |  |      |-%%%%-|    :  |  || |
|        :     |--|--| @@@  |=_||_=|    :  I  || |
|        :     |__|__|@@@@@ |_\__/_|    :  |  || |
|        :             \|/   ____       :  |  || |
|        :;;       .'``(_)```\__/````:  :  |  || |
|        :||___   :================:'|  :  | 0+| |
|        :||===)  | |              | |  :  |  || |
|        ://``\\__|_|______________|_|__:  I  || |
|      .'/'    \' | '              | '   '.|  || |
|    .'           |                |       '. || |
|  .'                                        '|| |
|.' Damian                                     '.|
0================================================0
''')
print("Welcome to Damian's House.")
print("Your mission is to find the exit.") 
answer1 = input("Do you have de key? Yes o No ").lower()
if answer1 == "yes":
    answer2=input("Do you want a lamp or a candle? ").lower()
    if answer2 == "lamp":
        answer3 = input("Great, the door is open? Yes, No or Maybe ").lower()
        if answer3 == "maybe":
            print("Congratulations!! you win the game, now, don't say nothing")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
