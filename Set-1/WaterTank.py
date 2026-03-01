N = int(input("Enter number of inflow"))
capacity=1000
minute=0
while(N>0):
    inflow = int(input("Enter inflows: "))
    if(capacity>0):
        capacity-=inflow
        minute+=1
    N-=1
print("OverFlow minutes : " , minute)


