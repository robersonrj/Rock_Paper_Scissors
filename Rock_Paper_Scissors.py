#called into play_a_game_question.py file for the Rock, Paper, Scissors game


def rock_paper_scissors():
 
    import random    #needed for random string array
    from time import sleep     #needed for the sleep time delay for realistic feel
    
#gets user's choice
    while True:    
        user_choice = str(input("Do you choose Rock, Paper, or Scissors?\nR for Rock, P for Paper, S for Scissors.\n"))
        
        if user_choice.upper() == "R":
            sleep(0.5)
            print("You chose Rock.")
            user_choice = "R"
            break
        elif user_choice.upper() == "P":
            sleep(0.5)
            print("You chose Paper.")
            user_choice = "P"
            break
        elif user_choice.upper() == "S":
            sleep(0.5)
            print("You chose Scissors.")
            user_choice = "S"
            break
        else:
            sleep(0.5)
            print("\nNot a valid choice.", end= " ")
        
        
#gets computer's random choice and displays
    x = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(x)
    sleep(1)
    print("The computer chose", computer_choice, end=".\n")
        
        
#compares user's choice to computer's choice
#method 1 (if loop - a little bit cleaner)

    if user_choice == "R":
        if computer_choice == "Rock":
            sleep(1)
            print("It's a tie!")
        elif computer_choice == "Paper":
            sleep(1)
            print("You Lose...")
        else:
            sleep(1)
            print("You win!")
    elif user_choice == "P":
        if computer_choice == "Paper":
            sleep(1)
            print("It's a tie!")
        elif computer_choice == "Scissors":
            sleep(1)
            print("You Lose...")
        else:
            sleep(1)
            print("You win!")
    else:
        if computer_choice == "Scissors":
            sleep(1)
            print("It's a tie!")
        elif computer_choice == "Rock":
            sleep(1)
            print("You Lose...")
        else:
            print("You win!")
            sleep(1)

#method 2, same sequence (using while loop)

#    while user_choice == "R":
#        if computer_choice == "Rock":
#            sleep(1)
#            print("It's a tie!")
#            break
#        elif computer_choice == "Paper":
#            sleep(1)
#            print("You Lose...")
#            break
#        else:
#            sleep(1)
#            print("You win!")
#            break
#
#    while user_choice == "P":
#        if computer_choice == "Paper":
#            sleep(1)
#            print("It's a tie!")
#            break
#        elif computer_choice == "Scissors":
#            sleep(1)
#            print("You Lose...")
#            break
#        else:
#            sleep(1)
#            print("You win!")
#            break
#            
#    while user_choice == "S":
#        if computer_choice == "Scissors":
#            sleep(1)
#            print("It's a tie!")
#            break
#        elif computer_choice == "Rock":
#            sleep(1)
#            print("You Lose...")
#            break
#        else:
#            print("You win!")
#            sleep(1)
#            break

