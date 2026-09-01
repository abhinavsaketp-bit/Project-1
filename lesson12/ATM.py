while True:
    name=input("What is your name? ")
    print(f"hi {name} welcome to the atm machine ")
    amount=int(input("How much amount do you want to withdraw? "))
    note500=amount//500
    amount=amount%500
    note100=amount//100
    amount=amount%100
    note10=amount//10
    remainder=amount%10
    print("Amount of 500 notes is: ", note500)
    print("Amount of 100 notes is: ", note100)
    print("Amount of 10 notes is: ", note10)
    print("Remainder is: ", remainder)

    print("Thank you for using the ATM")
    print("Next user please")