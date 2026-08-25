name=input("what is your name? ")
print(f"Hi i am {name} your vehicle guide")
print("Hi chose a vehicle ")
print("for car choose 1 and for bike choose 2")
choice=int(input("Enter: "))

if choice==1:
    print("You have chosen a car")
    print("We serve 3 types of cars")
    print("1 for electric cars, 2 for hybrid car and 3 for petrol car")
    choice=int(input("Enter: "))
    if choice==1:
        print("You chosen a electric car")
        print("Average speed is 80 km/h ")
        print("Rent per month is 1l ")
    elif choice==2:
        print("You have chosen a hybrid car")
        print("Average speed is 100km/h")
        print("Rent per month is 2l")
    elif choice==3:
        print("You have chosen a petrol car")
        print("Average speed is 90km/h")
        print("Rent per mounth is 0.75l")
    else:
        print("Enter a valid number")
elif choice==2:
    print("You have chosen a bike")
    print("We serve 2 types of bikes")
    print("1 for mountain bike and 2 for scooty bike")
    choice=int(input("Enter: "))
    if choice==1:
        print("you have chosen a mountain bike")
        print("Average speed is 80km/h")
        print("Rent per month 200,000 ")
    elif choice==2:
        print("You have chosen a scooty bike ")
        print("Averge speed is 60km/h")
        print("Rent per month is 20,000")
    else:
        print("enter a valid number")
else:
    print("Enter a valid number.")

    

    

