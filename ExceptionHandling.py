try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number : "))
    print(a/b)

except ZeroDivisionError:
    print("Cannot divide by Zero.")

except ValueError:
    print("Invalid input.")
else:
    print("Program runs successfully")

finally:
    print("Program finished")

