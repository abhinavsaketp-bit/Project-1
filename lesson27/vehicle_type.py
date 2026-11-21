class Vehicle:
    def __init__(self,brand,max_speed):
        self.brand=brand
        self.max_speed=max_speed
    def show_details(self):
        print("The brand of the car is: ",self.brand)
        print("The max speed of the car is: ",self.max_speed)
class Car(Vehicle):
    def __init__(self,brand,model,wheels,max_speed):
        self.model=model
        self.wheels=wheels
        super().__init__(brand,max_speed)
    def show_details(self):
        print("The model of the car is:", self.model)
        print("The number of wheels is:", self.wheels)
        super().show_details()

    def fuel_type(self,fuel):
        print(self.model,"uses",fuel) 

my_car=Car("Range Rover","Sport",4,290)

my_car.show_details
my_car.fuel_type("petrol")

print("Is Car a sub class of Vehicle:", issubclass(Car,Vehicle))



