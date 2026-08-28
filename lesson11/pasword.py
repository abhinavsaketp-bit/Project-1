guess=int(input("Enter a password"))
passed=0

while True:
    gussed=int(input("Please enter a password.")) 
    if guess==gussed:
        print("The phone has been unlocked.")
        break
    if passed>5:
        print("The phone has been locked for 30 seconds.")
        break
    passed=passed+1

    print("Try again")

   
