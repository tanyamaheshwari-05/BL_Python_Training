password = input("Enter password : " )
Upper=False
Digit=False
for char in password:
    if(char.isdigit()):
        Digit=True
    elif(char.isupper()):
        Upper=True
if(len(password)>=8 and Digit and Upper):
    print("Strong ")
else:
    print("Weak")