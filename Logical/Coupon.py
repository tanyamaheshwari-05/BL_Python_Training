import random
no_of_coupon =  int(input("Enter number of coupons: "))

coupon=set()
count=0

while len(coupon)< no_of_coupon:

    num = random.randint(1, no_of_coupon)
    count+=1
    coupon.add(num)
    
print("Total count for distinct coupons: ", count)
