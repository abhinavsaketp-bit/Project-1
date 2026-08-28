while True:
    print("Enter 1 to for clean your room")
    print("Enter 2 for cleaning the house")
    print("Enter 3 to Study ")
    print("Enter 4 to exit")
    value=int(input("Your input: "))
    if value==1:
        print("Clean your room")
    elif value==2:
        print("Clean the house")
    elif value==3:
        print("Time to study")
    elif value==4:
        print("Exiting...")
        break
    else:
        print("Enter a valid choise")
