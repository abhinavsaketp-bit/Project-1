import random 
import math

lucky_number=random.randint(1,10)
print("The lucky number is:", lucky_number)

Fun_choices=["Play a video game","Play outside with your friends","Do swimming","Cook your favourite food"]
random_activity=random.choice(Fun_choices)
print("The activity is:", random_activity)

secret_number=random.randint(1,5)
while True:
    choice=int(input("Enter your number: "))
    if choice==secret_number:
        print("Congrates you have guessed the secret number!!.")
        break

    print("Try again! You have gussed the wrong number!")

decimal_number=float(input("Enter a decimal value: "))
print("The ceiling value of the number is:", math.ceil(decimal_number))
print("The floor value of the number is:", math.floor(decimal_number))

x=29
y=-7
print(x)
print(y)
print("The copysign of these numbers is:", math.copysign(x,y))

negative_number=int(input("Enter a negative number: "))
print("The absolute value of the negative number is:", math.fabs(negative_number))

num1=int(input("Enter the first number to find the HCF/GCD of the two numbers given by you: "))
num2=int(input("Enter the second number to find the HCF.GCD of the two numbers given by you: "))
print("The GCD/HCF of the two numbers is:", math.gcd(num1,num2))

print("Lucky Number:", lucky_number)
print("Random Activity:", random_activity)
print("Secret Number..............",secret_number,"!!!!!!!!!!!!!!")







