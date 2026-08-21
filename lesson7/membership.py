print("Enter the marks you got in 5 subjects: ")

subject1 = int(input("Subject1: "))
subject2 = int(input("Subject2: "))
subject3 = int(input("Subject3: "))
subject4 = int(input("Subject4: "))
subject5 = int(input("Subject5: "))

total_marks= subject1 + subject2 + subject3 + subject4 + subject5
average= int(total_marks/ 5)

validRange= range(0, 100)

if average not in validRange:
    print("Invalid Input!")

elif average in range(90, 100):
    print("Your Grade is A1")

elif average in range(80, 90):
    print("Your Grade is A2")

elif average in range(70, 80):
    print("Your Grade is B1")

elif average in range(60, 70):
    print("Your Grade is B2")

elif average in range(50, 60):
    print("Your Grade is C1")

elif average in range(40, 50):
    print("Your Grade is C2")

elif average in range(30, 40):
    print("Your Grade is D")

elif average in range(20, 30):
    print("Your Grade is E1")

elif average in range(0, 20):
    print("Your Grade is E2")