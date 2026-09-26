valid=False

while not valid:
    try:
        bill_amount,discount_percentage,people=input("Enter the bill amount,discount percentage and the number of people. Use commas to separate: ").split(",")
        bill_amount=float(bill_amount)
        discount_percentage=float(discount_percentage)
        people=int(people)
        if bill_amount<=0 or discount_percentage<0 or people<0:
                raise ValueError

        discount_amount= bill_amount * discount_percentage/100
        final_amount=bill_amount-discount_amount

        amount_per_person=final_amount/people
    except ValueError:
         print("Invalid input! enter numbers")

    except ZeroDivisionError:
         print("Number of people can not be zero.")
    else:
         print("Bill:", bill_amount)
         print("Discount percentage:", discount_percentage)
         print("Discount amount:", discount_amount)
         print("Final amount:", final_amount)
         print("Amount per person", amount_per_person)
         # Add (break) here to stop the code from repeating after a customer is done.
    finally:
         print("The billing for this attempt is done!")




        



