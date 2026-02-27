time = int(input("Enter Time : " ))
signal = time % 90
if(signal <=30):
    print(" Red ")
elif(signal >=31 and signal <=45 ):
    print("Yellow")
else:
    print("Green")
