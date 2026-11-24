class myClass:

    __private_var= 27;

    def __private_meth(self):
        print("I am located inside the class.")
    def Hello(self):
        print("Hi, i am visable to everyone.",myClass.__private_var)

object= myClass()
object.Hello()
object.__private_var
object.__private_meth
    
