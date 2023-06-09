#I suck in programming
# randint(a,b) return a random integer from range (a,b+1)

import random

def guess_number(x):
    random_number  = random.randint(1,x)
    guess = 0
    guess_limit = 3
    while guess != random_number and guess_limit < 3:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Guess again, too low")
        elif guess > random_number:
            print("Guess again, too high")
        
    print(f"Congrats you've guessed the number {random_number} correctly ")
    
guess_number(11)

# now let the computer guess the number

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c" and low!=high:
        guess = random.randint(low,high)
        feedback = input(f'Is {guess} too high (H),too low(L), or correct(C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Congrats you dumbass you've guessed the {guess} number correctly! ")
    
computer_guess(11)

        
        
        
        
