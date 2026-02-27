salary= int(input("enter salary: " ))
late_days = int(input("Enter number of late days: "))
absent_days = int(input("Enter absent days: "))
if(late_days > 5):
    salary-=(salary*5)/100
elif(late_days>10):
    salary-=(salary*10)/100
elif(absent_days>2):
    salary-=(salary*5)/100
print("final_salary : " , salary)

