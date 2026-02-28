number = int(input("Enter a number : "))
count =0
while(number %2 ==0):
    count+=1
    number/=2
print(count)