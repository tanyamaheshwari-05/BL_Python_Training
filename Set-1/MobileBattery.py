drain = int(input("Enter drain per minute: "))
count=0
battery =100
while (battery>0):
    battery-=drain
    count+=1
print("Minutes : ",count)