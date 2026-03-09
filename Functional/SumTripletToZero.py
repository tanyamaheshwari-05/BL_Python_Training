N = int(input("Enter number of elements : "))

count=0

arr=[]
for i in range(N):
    arr.append(int(input()))

for i in range(0,N):
    for j in range(i+1,N):
        for k in range (j+1,N):
            if(arr[i]+arr[j]+arr[k]==0):
                print(arr[i],arr[j],arr[k])
                count+=1
print("Total triplets whose sum is 0: ",count)