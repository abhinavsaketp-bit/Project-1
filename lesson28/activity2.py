class Computer:
    def __init__(self):
        self.__max_price=900
    def sell(self):
            print("Selling price {}", format(self.__max_price))
    def setMaxPrice(self,price):
         self.__max_price=price
virus=Computer()
virus.sell()

virus.__max_price=1000
virus.sell()

virus.setMaxPrice(1000)
virus.sell()
