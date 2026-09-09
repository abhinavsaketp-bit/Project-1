print("PLease enter a value untile 1 to 10")
secret=int(input("Enter value1: "))

while True:
    choice=int(input("Enter a value: "))
    if choice==secret:
        print("Congrates you have guessed the secret number")
        break
    elif secret>choice:
        print("Hint: The word is higher than the number you entered.")
    elif choice>secret:
        print("Hint: The word is less than the number you have entered.")
    else:
        print("try again")
        continue
       
     

        
    

