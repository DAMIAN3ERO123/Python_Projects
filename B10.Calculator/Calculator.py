#Calculator
#Importamos la variable logo del archivo art.py
from art import logo

#Creamos las funciones que tendra nuestra calculadora, sólo las basicas
#add 
def add(num1,num2):
  return num1 + num2

#substract
def sub(num1,num2):
  return num1 - num2

#Multiply
def mul(num1,num2):
  return num1 * num2

#Divide
def div(num1,num2):
  if num2 == 0:
    return "You can't divide by 0"
  else: 
    return num1 / num2

# Creamos nuestro menu de operaciones mediante un diccionario cuyas llaves son los simbolos de las operaciones
calc_menu = {
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
}


#Creamos la funcion calculadora
def calc():
  #Imprimimos el logo importado
  print(logo)

  #Solicitamos el primer numero
  num1 = float(input("What's the first number?: "))

  #Presentamos las operaciones que puede elegir el usuario
  for key in calc_menu:
    print(key)

  
  go = True
  while go:
    operation_symbol = input("Pick an operation: ")
    next_num = float(input("What's the next number?: "))

    #Calculamos la respuesta de la operacion llamando a la función que hay en el diccionario a través del simbolo dado
    print(f"{num1} {operation_symbol} {next_num} = {calc_menu[operation_symbol](num1,next_num)}")
    answer = calc_menu[operation_symbol](num1,next_num)

    #Si el usuario quiere realizar una nueva operacion se llama nuevamente a la función calc()
    if input(f'Type "y" to continue calculating with {answer}, or type "n" to start a new calculation: ') == "n":
      go = False
      calc()
    else:
      num1 = calc_menu[operation_symbol](num1,next_num)

calc()
