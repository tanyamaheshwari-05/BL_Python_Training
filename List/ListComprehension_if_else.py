# list of fruits.
fruits=["banana","apple","orange","apple"]
newlist=[]

for x in fruits:
    if(x!="banana"):
        newlist.append(x)
    else:
        newlist.append("orange")

print(newlist)

# by using list comprehension :

fruits=["banana","apple","orange","apple"]
newlist=[x if x!="banana" else "orange" for x in fruits]
print(newlist)
