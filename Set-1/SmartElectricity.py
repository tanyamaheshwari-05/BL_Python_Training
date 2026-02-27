units = int(input("Enter the units "))
totalSum = 0
if(units<=100):
    totalSum = 3*100
elif (units<=200):
    totalSum = 3*100 + (units-100)*5
else:
    totalSum = 3*100 + 100*5 + (units-200)*8

if(units > 300):
    totalSum += (totalSum*10)/100
print("Total bill : ", totalSum) 
    
