temp=int(input("What is the tempture today? "))

if temp<20:
    activity="indoor reading"
    play=print("Let's do Indoor reading. Come on!")
else:
    activity="outdoor play"
    play=print("let's play outside together! ")

rain=input("Is it raining outside ? yes or no: ")
if rain=="yes":
    print("You better stay inside and don't think about going outside.")

homework=int(input("How long is your homework? "))
if homework>45:
    Break="yes"
    print("Why don't you take a 15 minutes")
else:
    Break="no"
    print("Homeworktime is too short for you to take a break." )
free_time=input("Do you have free time today? yes or no: ")
if free_time=="yes":
    final_task="hobby time"
    print("It's time for hobby time")
else:
    final_task="planning time"
    print("It is planning time then")

print("Temprature: ", temp)
print("Activity chosen: ", activity)
print("Raining status: ", rain)
print("Break status: ", Break)
print("Final task:", final_task)

