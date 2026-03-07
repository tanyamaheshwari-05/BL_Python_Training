N= int(input("Enter the range : " ))
if(N==0):
    print("Number should not be 0 ")
else:
    harmonic = 0.0
    for i in range(1,N+1):
        harmonic+=1/i
    print("Harmonic number :  ",harmonic)
