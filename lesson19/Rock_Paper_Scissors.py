import random
while True:
    choice=input("Enter 'Rock', 'Paper' or 'Scissors': ").strip().capitalize()
    possible_inputs="Rock","Paper","Scissors"
    engine=random.choice(possible_inputs)
    print(f"You chose {choice} and the computer chose {engine}.")
    if choice==engine:
        print(f"It is a tie! You chose {choice} and engine chose {engine}.")
        print("Try again")
        continue
    elif choice=="Rock" and engine=="Scissors" or choice=="Scissors" and engine=="Paper" or choice=="Paper" and engine=="Rock":
        print("Congrats you have defeated the computer!")
        print(f"You have chose {choice} and the computer chose {engine}.")
    
    else:
        print("You have lost :(.")
        print(f"You have chose {choice} and computer chose {engine}.")
        print("Better luck next time!")

    
    play_again=input("Do you want to play again yes/no : ")
    if play_again=="no":
        print("Alright i hope you play again!")
        break
    




    