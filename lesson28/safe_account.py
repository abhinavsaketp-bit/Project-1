class Account:
 
    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = pin   
 
    def show_pin_status(self):
        print("Account :", self.owner)
        print("PIN is stored .")

    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN updated successfully.")
        else:
            print("Invalid PIN. PIN must be exactly 4 digits.")
 
    def check_pin(self, entered_pin):
        if entered_pin == self.__pin:
            print("Access granted.")
        else:
            print("Access denied.")
 
    def __str__(self):
        return "Account holder: " + self.owner
 
 
my_account = Account("Abhinav", "2468")

print(my_account)

my_account.show_pin_status()

my_account.__pin = "1234"
print("Changing PIN from outside.")

my_account.check_pin("1234")
my_account.check_pin("2468")

my_account.set_pin("1234")

my_account.check_pin("1234")
