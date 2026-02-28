correct_pin = input("Enter correct pin : ")
access = False
for i in range(3):
    attempt= input("Enter attempted password : ")
    if(attempt == correct_pin):
        access=True
        break
if access:
    print("Access Granted")
else:
    print("Access Locked")
