habit_info=("Chess",True,7,3.44)
print("The habit info is:", habit_info)  

weekly_habits=(0,1,1,0,1,1,1,0,0,1)
print("The weekly habit list is:", weekly_habits)

print("The total number of days tracked is:", len(weekly_habits))

indexing_number_for_weekly_habits=int(input("Enter a number so i can direct you to that positioning of the weekly_habits's list (Make sure the number you enter is less than 11): "))
print("The number you have desired is:", weekly_habits[indexing_number_for_weekly_habits-1] )

num1_for_slicing_weekly_habits=int(input("Enter the first number for slicing weekly habits list: "))
num2_for_slicing_weekly_habits=int(input("Enter the second number for slicing weekly habits list: "))
print("The slice you asked for is coming right up:", weekly_habits[num1_for_slicing_weekly_habits:num2_for_slicing_weekly_habits])

weekly_habits=weekly_habits+(0,)
print("Weekly habits list after adding one more day:", weekly_habits)

completed=weekly_habits.count(1)
missed=weekly_habits.count(0)
print("The number of completed days: ",completed)
print("The number of missed days:", missed)

finished=0
not_finished=0

for days in range(0,len(weekly_habits)):
    if weekly_habits[days]==1:
        finished=+1
    elif weekly_habits[days]==0:
        not_finished=+1
if finished>not_finished:
    print("Great progress!")
elif not_finished>finished:
    print("Try harder")

        







