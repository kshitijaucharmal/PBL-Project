import random


user_choice = input("Enter your choice: ")
computer_choice = random.choice(['r','p','s'])
    
if user_choice == computer_choice:
    print("Its a tie!!")
elif user_choice == 'r':
    if computer_choice == 'p':
            print("You lose!")
    else:
            print("You win!!")
elif user_choice == 'p':
    if computer_choice == 's':
         print("You lose!")
    else:
        print("You win!!")
elif user_choice == 's':
    if computer_choice == 'r':
        print("You lose!")
    else:
        print("You win!!")
        

           
        
        