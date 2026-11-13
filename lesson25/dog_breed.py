class Pet:
    print("\nPet class\n")
pet_object= Pet()

class Pet_Profile:
    category="pet"
    def __init__(self,name,animal_type,age,favourite_food):
        self.name=name
        self.animal=animal_type
        self.age=age
        self.favourite_food=favourite_food

pet1=Pet_Profile("Surya","Dog",5,"Biscuits")
pet2=Pet_Profile("Mars","Cat",3,"Fresh Fish")

print("Surya is a {}".format(pet1.category))
print("Mars is a {}\n".format(pet2.category))

print("{} is a {} and is {} year old.".format(pet1.name,pet1.animal,pet1.age))
print("{} favourite food is {}.\n".format(pet1.name,pet1.favourite_food))

print("{} is a {} and is {} year old.".format(pet2.name,pet2.animal,pet2.age))
print("{} favourite food is {}.\n".format(pet2.name,pet2.favourite_food))