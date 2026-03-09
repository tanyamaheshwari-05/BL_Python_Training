a= int(input("Enter value of a : "))
b= int(input("Enter value of b : "))
c= int(input("Enter value of c : "))

delta= b*b - 4*a*c

if(delta > 0):
    root1 = (-b + sqrt(delta))/(2*a)
    root2 = (-b - sqrt(delta))/(2*a)

    print("Root 1 of quardatic eq. " ,root1)
    print("Root 2 of quardatic eq. ",root2)
else:
    print("Complex root ")

