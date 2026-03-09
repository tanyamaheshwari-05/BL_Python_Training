import math

t = int(input("Enter Temperature in (Fahrenhite): "))
v = int(input("Enter wind speed : "))

if abs(t) > 50 or v>120 or v<3:
    print("Invalid range")

else:
    w = 35.74 + 0.6125 * t +(0.4275 * t - 35.75 ) * math.pow(v,0.16)
    print("Wind chill : ",w)