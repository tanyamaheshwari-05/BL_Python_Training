dict={}
for i in range(10):
    if(i % 2 == 0):
        dict[i]=i**2
print(dict)

# By using dictionary comprehension :
# {expression for item in iterable if condition }

dict = {i:i**2 for i in range(10) if i % 2 == 0}
print(dict)