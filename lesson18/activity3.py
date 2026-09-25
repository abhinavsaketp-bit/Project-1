while True:
    try:
        value=int(input("Enter a value to divided: "))
        while value%2==0:
            print("bye")
    except ValueError:
        print("Make sure value is integer")


              
