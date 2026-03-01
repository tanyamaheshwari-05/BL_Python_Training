number = int(input("Enter  number : "))
while(number>=10):
    original=number
    sum=0
    while(original>0):
        digit= original % 10
        sum +=digit
        original //= 10
    number=number-sum
print("Final digit : ",number)