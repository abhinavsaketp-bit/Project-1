class Employee:
    def __init__(self):
        print("Constructor called")
    def __del__(self):
        print("Destrutor called")
def Create_object():
    obj=Employee()
    return obj

obj=Create_object()
del obj 