'''x = "abcdef"
for i in x:
    print(i, end=" ")'''


'''x = "cdefa"
i = "e"
for i in x:
    if i==x:
        break
    
    print(i, end = " ")    '''


'''x = "abcdef"
i = "a"
while i in x[1:]:
    print(i, end = " ")    '''


'''

x = ['ab', 'cd']
for i in x:
    print(i.upper())'''


def book():
    b = '''
    ====Following Books are Present Library!=====
    python 
    c# 
    c++ 
    sql
    Data analysis
    '''
    print(b)


input("pleased Enter your name\n")
int(input("Enter your Student id\n"))
input("Enter your degree\n")

print("Thank you")

d = input("Enter a book name,you want to take!\n")
if d in b:
    print("Your request has been forwarded to incharge")
else:
    print("please enter a valid choice")
a = ('''
    ====Welcome To Python Library====   
    1.Show the List of Books1
    2.Request a Book
    3.Return a Book
    4.Exit from Library''')
print(a)
c = int(input("Please Choose an option: "))


if c == 1:
    book()
