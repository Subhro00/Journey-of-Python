for i in range(6):
    print(i)
    if i==4:
        break   #in case of break the else block is not executed 
else:
    print("Sorry no i")
#the else block will be executed after all the iteration are completed

for i in []:
    print(i)
else:
    print("Sorry no i")
#in case of empty list it directly prints else block

for x in range(5):
    print("Iteration no. {} in for loop".format(x+1))
else:
    print("else nlock in loop")
print("Out of the loop")

