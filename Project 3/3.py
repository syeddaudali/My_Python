b=0
w=0
print("*****Welcome to Quiz*****")
a=int(input("Press 1 for Tea or Press for Coffee for 0!"))

if a==1:
    print("You choose the slect option")
    b += 1
elif(a==0):
    print("You choose the wrong option")
    b -= 1

c=int(input("Press 1 for Cricket or Press Football for 0!"))

if c==1:
    print("You choose the slect option")
    b += 1
elif(c==0):
    print("You choose the wrong option")    
    b -= 1

print(f"You select the {b} correct options and {w} wrong options")    