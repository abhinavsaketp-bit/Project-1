def billing(item_cost,amount):
    return(item_cost*amount)

item_cost=int(input("What is the price of the item you have brought? "))
amount=int(input("Enter the number of items you have brought: "))

print("The total amount of price you need to pay is: ", billing(item_cost,amount))

