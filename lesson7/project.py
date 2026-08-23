camara= 2 
microphone= 4 
storage= 6
location= 8

approved=["Chess","Teams","Codingal"]
restricted=["Shopping","Games","Bank"]

name=input("What is your name? ")
apps_asked=input("What app do you want to access? ").lower()

if type(name) is str:
    print("User name is a string")
if type(apps_asked) is not int:
    print("No app is not stored as a number")

if apps_asked in approved:
    print("Access granted, you may you the app")
else:
    print("Access denied, this app is restricted ")

if apps_asked not in restricted:
    print("You might use this app")
else:
    print("This app is restricted")

student_permission= camara| microphone| storage
print("Student permission as binary ", bin(student_permission))

if student_permission & camara:
    print(" Permission: granted")
 
if student_permission & microphone:
    print(" Permission: granted")
 
if student_permission & storage:
    print("Permission: granted")
 
if student_permission & location:
    print("Permission: granted ")
else:
    print("Permission: restricted")


next_permission = camara << 1
 
print("Camera in binary:", bin(camara))
print("After left shift:", bin(next_permission))
 

previous_permission = storage >> 1
 
print("Storage bit:", bin(storage))
print("After right shift:", bin(previous_permission))

if apps_asked in approved and apps_asked not in restricted:
    print("Access granted to", apps_asked)
else:
    print("Access declined to", apps_asked)
 