class Father:
    def __init__(self,eye_colour,age,height,hair_colour):
        self.eye_colour=eye_colour
        self.age=age
        self.height=height
        self.hair_colour=hair_colour

    def show_traits(self):
        print("Eye colour",self.eye_colour)
        print("Age",self.age)
        print("height",self.height)
        print("hair_colour",self.hair_colour)
class child(Father):
    def __init__(self,height,weight,hair_colour):
        
        self.weight=weight
        super().__init__(self.hair_colour,self.height)
    
