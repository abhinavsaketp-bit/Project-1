rows=int(input("rows: "))
iter=int(rows/2)+1
loop=1
for i in range(iter):
    for j in range(iter-1):
        print(" ", end="")
    for k in range(loop):
        print("*",end="")
        #print(f"loop{loop}")
    if (int(loop)==rows):
        print()
        break   
    loop=loop+2
    print()
    iter=iter-1
    
    
    






  