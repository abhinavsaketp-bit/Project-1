def greet():
    name=input("Hello user, what is your name?")
    print(f"Hello {name}, welcome to vending machine!")
def ask():
    print("We sell four products.")
    print("1 for apple. This costs you 50")
    print("2 for choclate bar.This costs you 35")
    print("3 for ice cream. This costs you 50")
def change(amount,price):
    return amount-price
def choice():
    choice=int(input("Enter a number: "))
    if choice==1:
        print("You have choosen an apple.Pay me 50")
        amount=int(input("Enter you amount: "))
        print("The change is", change(amount,50))
    elif choice==2:
        print("You have choosen a choclate bar.Pay me 35")
        amount=int(input("Enter you amount: "))
        print("The change is", change(amount,35))
    elif choice==3:
        print("You have choosen an ice cream.Pay me 50")
        amount=int(input("Enter you amount: "))
        print("The change is", change(amount,50))
    else:
         print("Enter a valid choice")
         

while True:
    greet()
    ask()
    choice()

