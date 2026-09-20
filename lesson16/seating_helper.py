def total_bill(bill_amount,tip_perc):
    total = bill_amount*(2*tip_perc)
    return total
def seating_arrangement(guest):
    """This is a a seating arrangement manager"""
    if guest==0 or guest==1:
        return 1
    else:
        return guest*seating_arrangement(guest-1)

print(total_bill(150,20))

print(seating_arrangement.__doc__)
#Look out for the change is the results in each one of them.
print("For seating arrangement for 1 guest: ", seating_arrangement(1))
print("For seating arrangement for 2 guest: ", seating_arrangement(2))
print("For seating arrangement for 3 guest: ", seating_arrangement(3))
print("For seating arrangement for 4 guest: ", seating_arrangement(4))
print("For seating arrangement for 5 guest: ", seating_arrangement(5))

