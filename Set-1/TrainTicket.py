distance = int(input("Enter the distance : "))
age = int(input("Enter the age : "))
fare = distance*2
if(age<12):
    fare-=(fare*50)/100
elif(age>60):
    fare-=(fare*30)/100
print("Total Fare : ", fare)
