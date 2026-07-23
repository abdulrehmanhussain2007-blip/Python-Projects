class Computer:
    def __init__(self):
        self.maxprice=10000
    def sell(self):
        print(f'Selling price: {self.maxprice}')
    def setMaxprice(self,price):
        self.maxprice=price
comp=Computer()
comp.sell()
comp.setMaxprice(1500)
comp.sell()