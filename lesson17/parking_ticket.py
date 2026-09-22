def calculate_change(paid,price):
    change=paid-price
    return change

ticket_price=30
print("The cost of the ticket is", ticket_price)
print("We also only accept 1,5,10,or 25 rupees coins")

total_inserted=0
coins_inserted=0

while True:
    coin=int(input("Enter a coin: "))
    if coin==1 or coin==5 or coin==10 or coin==25:
        pass
    else:
        print("Enter a valid number!")
        continue

    total_inserted+=coin
    coins_inserted+=1
    print(f"Amount paid: {total_inserted} number of coins: {coins_inserted}")

    if total_inserted>=ticket_price:
        print("You have paid the right amount of money!")
        break
change_due=calculate_change(total_inserted,ticket_price)

if change_due==0:
    pass
else:
    print("Here is your change", change_due)

print("Ticket price:", ticket_price)
print("Number of coins given:", coins_inserted)
print("Total paid:", total_inserted)
print("Change:", change_due)

print("Printing ticket..... Please wait!")
print("Here is your ticket!")




