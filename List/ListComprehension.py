# find square using list 
square=[]

for x in range(10):
    square.append(x**2)

print("sqaure of number upto 10 : " , square)


# By using list comprehension : 

square=[x**2 for x in range(10)] # [expression(what need to perform ) for item in iterable]
print("sqaure of number upto 10 : ",square)

