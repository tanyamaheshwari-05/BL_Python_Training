class Car:
    car_manufacturer = "Toyota" 
    def __init__(self,brand,color): # self is reference of the object it refers to the currentt object, and __init__ is always invoked whenever we create an object.
        self.colour=color
        self.brand= brand
    
c1 = Car("BMW","Blue")
print(c1.colour,c1.brand,c1.car_manufacturer)

c2= Car("Mercedes" , "Black")
print(c2.colour,c2.brand,c2.car_manufacturer)


