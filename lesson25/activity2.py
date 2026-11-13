class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
        self.name=name
car1=Vehicle("Honda",300,50)
car2=Vehicle("Toyota",200,13)

print("Car 1 details: ", car1.name,car1.max_speed,car1.mileage)
print("Car 2 details: ", car2.name,car2.max_speed,car2.mileage)

