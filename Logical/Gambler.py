import  random
stakes= int(input("Enter the number of stakes: " ))
goal= int(input("Enter the goal: " ))
trials= int(input("Enter the number of times : " ))
 
win=0
bet=0

for i in range(trials):

    cash=stakes
    while cash > 0 and cash < goal :
        bet+=1
        cash+=random.choice([-1,1])

    if cash==goal:
        win+=1

print("Wins:", win)
print("Win %:", (win/trials)*100)
print("Loss %:", 100 - (win/trials)*100)