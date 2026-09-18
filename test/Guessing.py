secret=int(input("Enter a secret number: "))
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
name=input("Hello, what is your name?  ")
print(f"Hello {name}, welcome to Guess The Word.")
print("The objective is to just guess the word!")
print("But the number is up to 1-50")
print("Can you do it?")
print("Good luck!")

guess=0
lives=0
max_number=5
while lives<max_number and guess!=secret:
    guess=int(input("Enter your number: "))
    lives+=1
    
    
       
    if secret==guess:
        print("Well done!! you did it. ")
        print("You had the guts to complete it!")
        print("Congrats on your achievement🎉")
        break
    else:
        if guess>secret:
            diff=guess-secret
        else:
            diff=secret-guess
            if diff>=20:
               print("Get out of there! Your number is going to freeze.🧊")
            elif diff>=10:
               print("Your number is in the freezer!")
            elif diff>=5:
               print("Your number at room temp")
            else:
               print("You are next to the campfire! Just jump in it. Come on!")

remaining=max_number-lives

if remaining>0:
        print("Your remaining hearts are:", remaining)

if guess!=secret:
    print("You ran out of hearts!")
    print("Mabye, Better luck next time. Only if you play one more time")
    print("The secret number was",secret)
    print("Have a great day and Thank You for playing my game.")

    






