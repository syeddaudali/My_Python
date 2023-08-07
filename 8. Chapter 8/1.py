'''def max(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
        else:
            return n3

    else:
        if n2>n3:
            return n2
        else:
            return n3


a=max(12,56,98)                
print("the maz value is ", str(a))




def percent(marks):
    a=(marks[0]+marks[1]+marks[2]+marks[3])
    return a

c=[23,43,5,34]
b=percent([45,76,0,7])    
print(b)'''


a=int(input("Enter a no.: "))
for i in range(a+1):
    print((" ")*(a-i),"*"*i)