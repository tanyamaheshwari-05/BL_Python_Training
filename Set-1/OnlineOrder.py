amount = int(input("Enter amount : "))
payable_amount=0
if(amount >= 5000):
    payable_amount= amount - amount *(20/100)
elif(amount>=3000):
    payable_amount= amount- amount*(10/100)
elif(amount>=1000):
    payable_amount=amount-amount-(5/100)
else:
    payable_amount=amount
print("Payable amount : ",payable_amount)
