total_homework = 4
original_count = total_homework

completed_count = 0
task_num = 1
 
while task_num <= total_homework:
    if task_num == 1:
        next_task = "It is time to study some social science"
    elif task_num == 2:
        next_task = "Time to read some english"
    elif task_num == 3:
        next_task = "Maths time"
    else:
        next_task = "It is obviously coding time!"
 
    answer = input(f"Have you finished {next_task} yes/no: ").strip().lower()
    if answer == "yes":
        completed_count += 1
        task_num += 1
        print("Good work. Keep it up.")
    else:
        print("Finish your howework before you do anything.")
   
    print("Homework tasks remaining: ", total_homework - completed_count)

print("Good job finishing your homework.")

test_value = 0
safety_counter = 0
 
while test_value <= 0:
    print("This is going to loop forever becasuse this equation is false.")
    safety_counter += 1
    
 
    if safety_counter == 3:
        print("The Equation is false but still lets break the code anyway. No one wants to waste thier storage.")
        break
 
print("Homework for today:" , original_count)
print("Homework completed:" , completed_count)
print("Homework that needs finishing:" , total_homework - completed_count)

