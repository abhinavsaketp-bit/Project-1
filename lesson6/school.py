print("I am a smart student planner ")
print("I will ask you 3 questions ")
day=input("what day is it today? ").lower()
weather=input("How is the weather today? (sunny or rainy)").strip().lower()
homework=input("have you done your homwork(yes or no)")
if day== "saturday" or  day=="sunday":
    print("It is the right time to go")
elif day== "monday" or day=="tusday":
    print("It is school time")
elif day in ("wednesday","thursday","friday"):
    print("It is still school day")
else:
    print("enter a valid day")
if weather=="sunny" and homework=="yes":
    print("Enjoy your trip outside.")
if not homework=="yes":
    print("Complete your homework first")
if weather=="sunny" and day in ("saturday","sunday"):
    print("Plan for a trip outside")
elif weather=="sunny" and homework=="yes" and day in ("saturday","sunday"):
    print("It is time to play with your friends")
elif weather=="rainy" and homework=="yes":
    print(" Have indoor free time.")
else:
    print("Best plan is to enjoy with your family.")
