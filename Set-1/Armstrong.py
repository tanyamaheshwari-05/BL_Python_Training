number = int(input("Enter the number : "))
original  = number
total=0
while(number>0):
    digit =  number % 10
    total += digit **3
    number = number // 10
if(total == original):
    print("Yes")
else:
    print("No")
