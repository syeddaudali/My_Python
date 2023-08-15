es=0
os=0
a=int(input("Enter a no.: "))
while a<=0:
    if a%2==0:
        es= es+a
        
    else:
        os= os+a
        
    print("The sum of even no. is: ",es)
    print("The sum of odd no. is: ",os)
