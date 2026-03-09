rows= int(input("enter number of rows: "))
column = int(input("Enter number of columns: "))

arr=[]

print("Enter elements: ")
for i in range(rows):

    row=[]
    for j in range(column):
        val=int(input())
        row.append(val)
    arr.append(row)

print("Array: ")

for row in arr:
    print(row)

