print("I am a smart student planner ")
print("I will ask you 3 questions ")
day=input("what day is it today? ").lower()
weather=input("How is the weather today? (Sunny or rainy)")
homework=input("have you done your homwork(yes or no)")
if day== "saturday" or  day=="sunday":
    print("It is the right time to go")
elif day== "monday" or day=="tusday":
    print("It is school time")
elif day== "wednesday" or day=="thursday" or day=="friday":
    print("It is still school day")
else:
    print("enter a valid day")
