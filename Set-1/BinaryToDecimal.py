binary_number = input("Enter the binary number : ")
sum=0
power = len(binary_number)-1
for i in binary_number:
    sum+= int(i) * (2** power)
    power-=1
print("Decimal number : " , sum)