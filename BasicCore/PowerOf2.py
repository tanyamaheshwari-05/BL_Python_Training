number = int(input("Enter a number : "))
if(number >=31 or number <0):
    print("Please enter with in the range of 0  to 30")
else:
    i=0
    while(i<=number):
        print("2 ^", i,"=",2**i )
        i+=1

