rice_cost=2 
milk_cost=3
fruit=1
baskets=3
family_members=4

baskets_cost_per_person=(rice_cost+milk_cost+fruit)*baskets/family_members
print("The baskets_cost_per_person: ", baskets_cost_per_person)

total_number_of_grocery=int(input("Enter the total number of groceries: "))
number_of_family_members=int(input("Number of member in your family: "))

if total_number_of_grocery% number_of_family_members ==0:
    print("Items can be divided equally")
else:
    print("Items cannot be divided equally.")

recorded_average=58
wrong_week_cost=30
correct_week_cost=100
total_weeks=3

recorded_total=recorded_average*total_weeks
print("The total groceries recorded", recorded_total)

corrected_total=recorded_total-wrong_week_cost+correct_week_cost
print("The correct total is: ", corrected_total)

corrected_average= corrected_total/total_weeks
print("The corrected average is: ", corrected_average)

store_a_average = 70
store_b_average = 75
store_c_average = 80
 
print("Store A average:", store_a_average)
print("Store B average:", store_b_average)
print("Store C average:", store_c_average)
 
if (corrected_average < store_a_average and corrected_average < store_b_average and corrected_average < store_c_average):
    print("Corrected grocery average is less than all three store averages.")
 
elif (corrected_average > store_a_average and corrected_average > store_b_average and corrected_average > store_c_average ):
    print("Corrected grocery average is higher than all three store averages.")
 
else:
    print("Corrected grocery average is in between the three store averages.")


