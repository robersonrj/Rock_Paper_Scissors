#called into the play_a_game.py file for the Rock, Paper, Scissors game

def play_game():

    from time import sleep           #needed for the sleep time delay for realistic feel
    import Rock_Paper_Scissors
    

    while True:

        play_a_game = str(input("Do you want to play? Y for yes, or N for No. \n"))
    
        if play_a_game.upper() == "Y" or play_a_game.upper() == "YES":
            print("\nLet's play!")
            sleep(1.5)
            #start game now
            Rock_Paper_Scissors.rock_paper_scissors()
                                                                                        
        
        elif play_a_game.upper() == "N" or play_a_game.upper() == "NO":
            print("\nMaybe some other time.")
            break
    
        else:
            print("\nInvalid choice. Please choose Y or N.", end= " ")
    
