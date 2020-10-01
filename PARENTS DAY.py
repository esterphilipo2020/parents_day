def arusha_science():
    """finds the parent's child name in the Arusha scince"""
    print(' Welcome to arusha science. ')
    child_name = input(' What is your child name? ')
    while True:
        try:
            guest_number = int(input(' How many guest have you come with? \n'))
        except ValueError:
            print(' Enter a valid number ')
        else:
            print(" *****Thank you for bringing some guests****. ")
            break
    print(child_name.title() + " is very lucky to come to Arusha science school." + ".\n")
    print(" Here is a simple task for you. ")

arusha_science()
secret_number = 6
while True:
    guess_number = int(input(" What is the secret number? Between 1 to 10. "))
    if guess_number > 8:
        print(" That is too high , try again. ")
    elif guess_number < 4:
        print(" That number is too low , try again. ")
    elif guess_number == 6:
        print(" Congratulations you have guessed successfully ")
        break
    else:
        print(" Sorry.Try again. ")
print('let us play a little game number')
print("Think of a number")
print('do not enter your number in the terminal ')
print('press enter to continue in every step')
while True:
    ans = input('press y to continue ')
    if ans == 'y':
        step_2 = input('now double your answer ')
        step_3 = input('now add six')
        step_4 = input('divide your answer by two')
        step_5 = input('take away the original number')
        print('the answer is 3')
        break
    else:
        print('please follow the instructions')
