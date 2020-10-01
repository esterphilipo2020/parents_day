# IMPORTING RANDINT FUNCTION FROM RANDOM MODULE (INBUILT).
from random import randint


def arusha_science():
    """finds the parent's child name in the Arusha science"""
    print("Welcome to arusha science.")
    child_name = input("What is your child name?")
    while True:
        try:
            guest_number = int(input("How many guest have you come with? \n"))
        except ValueError:
            print(' Enter a valid number ')
        else:
            print("*****Thank you for bringing some(", guest_number, ")guests****.")
            break
    print(child_name.title() + " is very lucky to come to Arusha science school." + ".\n")
    print("-->Here is a simple task for you<--")


arusha_science()
# secret_number = 6

# HERE RANDOM MODULE IS MORE HELPFUL AND FUN FOR THE USER.
# THE --secret_num-- ALWAYS CHANGES TO A RANDOM NUMBER EVERY TIME THE WHOLE PROGRAM RUNS.

secret_number = randint(1, 10)
while True:
    guess_number = int(input("What is the secret number? Between 1 to 10."))
    if guess_number > secret_number:
        print("That is too high, try again.")
    elif guess_number < secret_number:
        print("That number is too low, try again.")
    elif guess_number == secret_number:
        print("*****Congratulations you have guessed successfully!*****")
        break
    else:
        print(" Sorry. Try again!")
print("-->Let us play a little game number<--")
print("1.Think of a number")
print("2.Do not enter your number in the terminal")
print("*Press enter to continue in every step*")
while True:
    ans = input("-->Hit Enter-key to continue<--")
    if ans == "":
        step_2 = input("1.Now double your answer")
        step_3 = input("2.Now add six")
        step_4 = input("3.Divide your answer by two")
        step_5 = input("4.Take away the original number")
        print('The answer is "3"')
        break
    else:
        print("Please follow the instructions")
