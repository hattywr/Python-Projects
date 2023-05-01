import random

def guess(x):
    random_number =  random.randint(1,x)
    # found = True;
    guess = 0
    trys = 0
    while(guess != random_number):
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if (guess< random_number):
            trys += 1
            print("Little low, try a bit higher!")
        elif (guess > random_number):
            trys += 1
            print("Little high, try a bit lower!")
    trys += 1
    print(f"Congrats! You guessed the number {random_number} correctly after {trys} tries!")
    

guess(10)


    