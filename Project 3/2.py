print("*****Welcome to Python Love Calculator*****")
a = input("Enter your name! ")
b = input("Enter your crush name! ")
c = a+b
i = c.lower()
print(i)

t = i.count('t')
r = i.count('r')
u = i.count('u')
e = i.count('e')
true = t+r+u+e


l = i.count('l')
o = i.count('o')
v = i.count('v')
e = i.count('e')
love = l+o+v+e

w = int(str(true)+str(love))
print(w)
print(f"Your Love Percentage is: {w}%")


if w < 20:
    print("Beta Parhai Ker lo phir kerna ashqi mashoqi")

elif w >= 20 and w < 40:
    print("Ya bachii tumha barbad kara ge! apna kam ker")
elif w >= 40 and w < 60:
    print("Your relation is in good term,jati rakho bacho")
elif w >= 60 and w < 80:
    print("pure soul mates,best of luck for future")
elif w >= 80 and w < 100:
    print("Your marriage will be fixed soon")
else:
    print("YOur love is out of range,apna demag ka ilaj kerwao")
