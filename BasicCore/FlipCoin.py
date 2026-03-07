import random
no_of_times= int(input("Enter numbers of time to flip coins: "))
head=0
tail=0
while(no_of_times>0):
    flip = random.randint(0, 1)
    print("You get : ",flip)
    if(flip==0):
        head+=1
    else:
        tail+=1
    no_of_times-=1
head_percentage = head *100 / (head+tail)
tail_percentage = tail *100 / (head+tail)
print("Getting head percentage : ",head_percentage ," %")
print("Getting tail percentage : ",tail_percentage ," %")
