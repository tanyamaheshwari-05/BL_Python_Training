class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks # here marks are private(__) 

    def get_marks(self):
        return self.__marks

s= Student("Tanya",98)
print(s.name)
print(s.get_marks())
