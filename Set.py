variable =  {"Tanya","Hello" , 1 ,3 ,5,"world"}
print(variable)
print(type(variable))

empty_set = set()  # create empty sets
# print(type(empty_set)) 
empty_set.add(2)
empty_set.add(3)
empty_set.add(1)
empty_set.add(7)
empty_set.add("Tanya")
print(empty_set)

empty_set.remove(3)
print(empty_set)

empty_set.clear()
print(empty_set)

print(empty_set.pop())


# set union and intersection
set1= {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))
print(set1.intersection(set2))


