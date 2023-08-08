def prime_checker(number):
    i = 0
    for num in range(1,number+1):
        if number % num == 0:
            i += 1

    if i > 2:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")
      
n = int(input("Check this number: "))
prime_checker(number=n)
