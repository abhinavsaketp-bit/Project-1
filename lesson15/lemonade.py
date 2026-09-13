def greet_customer():
    print("Hello wellcome to fresh lemonade stand!")
    name=input("What is your name: ")
    print("Hi nice to meet you", name)
def total_calculator(a,b):
    return a*b
def calculate_change(amount_paid,total):
    return amount_paid-total

greet_customer()

price_per_cup=float(input("Enter the price per cup: "))
cups=int(input("How many cups do you wan to have: "))
t=total_calculator(price_per_cup,cups)
print("The total price is: " , total_calculator(price_per_cup,cups))

amount_paid=float(input("Pay the total amount for the lemonade: "))

print(calculate_change(amount_paid,t))


