base=int(input("Please enter the base value: "))
exponent = int(input("Enter the exponent: "))
result=1

for i in range(exponent):
    result=result*base
print(f"The Calculation of {base}^{exponent} is :  ")
print(result)

