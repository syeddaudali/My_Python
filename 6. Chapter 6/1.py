'''n1=int(input("Enter 1st no.: "))
n2=int(input("Enter 1st no.: "))
n3=int(input("Enter 1st no.: "))

if n1>n2:
    if n1>n3:
        print(f"{n1} is graetest")
    else:
        a=n3 
else:
    if n2>n3:
        print(f"{n2} is greatest")   
    else: 
        a=n3    
if a==n3:
    print(f"{n3} is greatest")             '''
a=input("Enter a String: ")    
if len(a)>10:
    print("You entered greater than 10 char str")
else:
    print("you entered less than 10 char str")    