marks=[90.6,45,90,78.6]
print(marks)
print(type(marks))
print(marks[3])
print(len(marks))

marks[2]=60
print(marks)

marks[4]= 40
print(marks)

# Slicing

marks=[90, 45, 90, 78, 60]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[:-1])

# List methods (append , sort, reverse, insert, remove, pop, )
list= [3,2,8,1]
list.append(4)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list.insert(2,10)
print(list)

list.remove(2) # remove first occurence of element givent in the paranthesis.
print(list)

list.pop(0) #remove the particular element by its index.
print(list)
