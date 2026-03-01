N = int(input("Enter number of seats : " ))
seats = 40
for i in range(N):
    request= int(input("Enter number of ticket : "))
    if(request<=seats):
        print("Confirmed")
        seats-=request
    else:
        print("WaitListed")