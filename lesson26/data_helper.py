class DailyMessage:
    def __init__(self):
        self.message=""
    def get_message(self):
        self.message=input("Enter a sentance to fully capitalize: ")
    def print_message(self):
        print("This is the upper case of your input: ", self.message.upper())
daily_task=DailyMessage()
daily_task.get_message
daily_task.print_message

class HelperSession:
    def __init__(self):
        print("Session created")
    def __del__(self):
        print("Destructor called")

def create_session():
    session=HelperSession()
    return session

session_obj=create_session()

class PairFinder:
    def find_pair(self, numbers, target):
        lookup = {}
 
        
        for index, number in enumerate(numbers):
            needed_number = target - number
 
            if needed_number in lookup:
                return (lookup[needed_number], index)
 
            lookup[number] = index
 
        return None
 
 
numbers = (10, 20, 30, 40, 50, 60, 70)
 
target_value = int(input("Enter target sum to search: "))
 
result = PairFinder().find_pair(numbers, target_value)
 
if result is not None:
    print("index1=%d, index2=%d" % result)
else:
    print("No matching pair found.")

 
del session_obj
print("Program End")