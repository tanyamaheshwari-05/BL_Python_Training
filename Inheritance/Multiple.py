class A:
    varA="Welcome to class A"

class B:
    varB ="Welcome to class B"

class C(A,B):
    varC = "Welcome to class C"

obj1= C()
print(obj1.varC)
print(obj1.varB)
print(obj1.varA)