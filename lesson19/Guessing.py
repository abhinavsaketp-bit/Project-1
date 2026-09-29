import random
random=random.randint(0,10)
counter=1
while True:
    
    choice=int(input("Enter a number for the guessing game:"))
    if counter==5:
        print("You have used all of your hearts.")
        break

    if choice==random:
        print("congrats you have guessed the number!")
        break

    print("Try again!")
    counter+=1