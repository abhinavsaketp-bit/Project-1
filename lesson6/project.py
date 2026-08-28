print("                 LIBRARY VISIT PLANNER                         ")
day=input("What day is it today?(Monday to Sunday): ").strip().capitalize()
weather=input("How is the weather outside(sunny/cloudy/rainy/windy)").strip().lower()
book_due=input("Do you want to return the book? yes/no ").strip().lower()

if day=="Monday":
    print("Today is the start of the week ")
elif day=="Friday":
    print("Today is the last day of school")
elif day in ("Saturday""Sunday"):
    print("Weekends are the best time in the library. You have no fear of disturbance")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("It is a normal school day")
else:
    print("Undefined day, enter a valid day")

if weather=="sunny" and book_due=="yes":
    print("The weather looks awesome today.Return your due book and borrow a new book if you want.")

if weather=="rainy" or weather=="cloudy":
    print("Carry an umbrella just in case it rains")

if not book_due=="yes":
    print("There is no book to return, you may get a new book for your choice.")



if weather == "rainy" and book_due == "yes":
    print("Take your umbrella and that book better be on my today.")
elif weather == "sunny" and book_due == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan   : Stop by the library after school and return your book.")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Come to the libray for a relaxing")
else:
    print("Find the best time and make a visit to the library one day.")

print("THANK YOU FOR USING LIBRARY VISIT PLANNER ")





