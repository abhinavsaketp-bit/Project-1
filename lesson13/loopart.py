rows=int(input("Enter the number of rows: "))

for i in range(rows):
    for j in range(i-1):
        print("*", end=" ")

rows=int(input("Enter the number of rows for the Floyd's triangle: "))
number=1

for i in range(1,1+rows):
    for j in range(1,i+1):
        print(number, end=" ")
        number=+1
    print()

rows=int(input("Enter the number of rows for the diamond number pattern: "))

if rows==2:
    half_rows=rows//2
else:
    half_rows=rows//2+1

space=half_rows-1

for i in range(1, half_rows + 1):
    for j in range(1, space + 1):
        print(" ", end="")
 
    space -= 1
    number = 1
 
    for j in range(2 * i - 1):
        print(number, end="")
        number += 1
 
    print()
 
space = 1
 
for i in range(1, half_rows):
    for j in range(1, space + 1):
        print(" ", end="")
 
    space += 1
    number = 1
 
    for j in range(1, 2 * (half_rows - i)):
        print(number, end="")
        number += 1
 
    print()
 