def book():
    b='''
    ====Following Books are Present in Library!=====
    Python Book
    C# Book
    C++ Book
    SQL Book
    Data Analysis
    '''
    print(b)
    d=input("Enter a book name,you want to take!\n",)
    print(d)

    print("Your request has been forwarded to incharge")
def request():
     b='''
    ====Following Books are Present Library!=====
    python 
    c# 
    c++ 
    sql
    Data analysis
    '''
     input("pleased Enter your name\n")
     int(input("Enter your Student id\n"))
     input("Enter your degree\n")
     
     print("Thank you")

     d=input("Enter a book name,you want to take!\n")
     if d in b:
        print("Your request has been forwarded to incharge")
     else:
        print("please enter a valid choice")   
def Return():
    input("pleased Enter your name\n")
    int(input("Enter your Student id\n"))
    input("Enter your degree\n")
    input("enter the name of book you want to return\n")
    print("Thank you for returning this book")


def exit():
    print("Ja Ja tur ja")
a=('''
    ====Welcome To Python Library====   
    1.Show the List of Books1
    2.Request a Book
    3.Return a Book
    4.Exit from Library''')
print(a)
c=int(input("Please Choose an option: "))



if c==1:
     book()
elif c==2:
    request()    
elif c==3:
    Return()
elif c==4:
    exit()