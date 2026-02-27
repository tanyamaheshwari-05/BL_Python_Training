initialBalance = int(input("Enter the balance: "))
number = int(input("Enter number of accounts :"))
balance=initialBalance
for i in range(number):
    request = int(input("Enter each request :"))
    if(request % 100 == 0 and request<balance):
        balance-= request
        print("Success")
    else:
        print("Fail")
        number-=1
print("Final balance : " ,balance)


        
