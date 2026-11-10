profil={"Abhinav":94,"Felix":95,"Adi":89,"Rodrigo":71,"Bob":56}
avarage=0
total=0
for name,marks in profil.items():
    total=marks+total
avarage=total/5
highest=max(profil.values())
lowest=min(profil.values())
print("HIghest is :", highest)
print("Lowest is:", lowest)
print("Average is:", avarage)
print(profil.get("Adi"))
name1=input("Enter a student name: ")
print("This is the student marks requested:", profil.get(name1))





    