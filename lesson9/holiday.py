print("HI WELCOME TO HOLIDAY PLANNER")
choice=int(input("Choose 1 for beach holidays or 2 for mountain holidays: "))

if choice==1:
    print("You have chosen beach holidays")
    choice=input("Do you want to do swimming or build your own sandcastles: ").strip().lower()
    if "sandcastles" in choice or "sandcastle" in choice:
        print("You have chosen sandcastles!")
        print("Good choice! Especially while going to the beach.")
    elif "swimming" in choice or "swim" in choice:
        print("You have chosen swimming!")
        print("Relaxing for a hot summer day.")
    else:
        print("Enter a valid activity")

elif choice==2:
    print("You have chosen mountain holidays")
    choice=input("Do you want to do Hiking or Camping.").strip().lower()
    if "camping" in choice:
        print("You have chosen camping!")
        print("Nice choice, i hope you enjoy your trip.")
    elif "hiking" in choice:
        print("You have chosen Hiking.")
        print("Good luck on find good scenery and BEE careful of the small rocks that you can slip and fall.")
    else:
        print("Enter a valid activity")

else:
    print("Enter a valid number")
    print("Choose 1 for beach holidays or 2 for mountain holidays.")

