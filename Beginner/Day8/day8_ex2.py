# Prime number checker
def prime_checker(number):
    for x in range(2, number):
        if number % x == 0:
            print("This is not a prime number.")
            quit()
    print("This is a prime number.")



n = int(input("Check this number: "))
prime_checker(number=n)
