class Car:
    @staticmethod
    def start():
        print("car started.")
    
    @staticmethod
    def stop():
        print("car stopped.")
    
    
class ToyotaCar(Car):
    def __init__(self , brand):
        self.brand=brand

class Fortuner (ToyotaCar):
    def __init__(self,type):
        self.type=type

c1 = Fortuner("Diesel")
print(c1.name)
print(c1.stop())
print(c1.start())
