name=input("what is your name? ")
print(f"Welcome {name}") 
username=input(f"what is your username {name} : ")
marks=int(input("How many marks did you get in your examination?: "))

if marks>90:
    print(f"You are a A+ student {name}. OH WOW. Keep up the hard work.")
elif marks>80:
    print(f"You are a A student {name}. Aim for A+ next time.")
elif marks>70:
    print(f"You are a B+ student {name}. Aim for A+ next time.")
elif marks>60:
    print(f"You are a B student {name}. Come on never give up. Aim for the big.")
elif marks>50:
    print(f"You are a C student {name}. Success come in some consistent steps of hard work.")
else:
    print(f"You need to work really really hard {name}.")





