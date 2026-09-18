def greet_customer():
    print("Hello welcome to the art supplies store")
    print("Get your artistic tools inside! They are limited so quick!")
def calculate_total(price,items):
    return price * items
def calculate_change(paid,total):
    return(paid-total)
def thank_you_message(item):
    if item>=5:
        return("Oh wow!!Looks like you bought the entire art shop!!.Have a great day doing some art.")
    else:
        return("Thanks for purchasing at art supplies! I hope you come back soon for some other limited artist tools.")
        


greet_customer()

price_of_item=float(input("Price of the item bought: "))
number_of_items=int(input("Number of item brought (and the item must be the same): "))

total=calculate_total(price_of_item,number_of_items)
print("The total amount: ", total)

paid=float(input("The amount paid: "))
change=(calculate_change(paid,total))
print("The change is: ", change)

print("BILLING...")
print("Item price: ", price_of_item)
print("Number items: ", number_of_items)
print("Total bill: ", total)
print("Amount paid:", paid)
print("Change: ", change)
print(thank_you_message(number_of_items))


