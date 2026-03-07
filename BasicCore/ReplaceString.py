name = input("Enter username: ")
if(len(name)>=3):
    template= "Hello <<UserName>> ,How are you?"
    result= template.replace("<<UserName>>", name)
    print(result)
else:
    print("Name should not be less than 3")

