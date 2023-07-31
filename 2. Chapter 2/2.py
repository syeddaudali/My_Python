#arithmatic opertaprs

'''
a=5
b=10
c=55
d=12
print(a+b+c+d)'''

'''
a=50
b=25
print(a-b)'''

'''a=12
#b=12
print(a*b)'''

'''
a=25
b=5
print(a/b)'''

'''a=10
b=3
print(a%b)
'''

'''a=27
b=8

print(a%b)
'''






'''
a= (int(input("Enter 1st no.! ")))
b= int(input("enter 2nd no.! "))

BODMAS

print(a+b-c/d*e)
'''

#comparison operator  >, <, !=, >=, <=

'''
a=10
b=6
print(a>b)


a=5
b=8
print(a!=b)
'''
'''
a=(input('Enter an alphabet!'))
b=len(a)

if a==a.upper():
    print(f"You have entered {a}.Length of alphabet is {b} and it is a capital alphabet!")
elif a==a.lower():
    print(f"You have entered {a}.Length of alphabet is {b} and it is a smaller alphabet")    
elif (a==a.upper(),a==a.lower()):
    print(f"You have entered {a}.Length of alphabet {b} and it includes both captical and smaller alphabets!")
    
'''


'''from turtle import *
color('red')
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()
'''

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error

diabetes=datasets.load_diabetes()

'''print(diabetes.keys())
dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])'''

#print(diabetes.data)

#print(diabetes.DESCR)

diabetes_x=diabetes.data[:,np.newaxis,2]

#print(diabetes_x)

'''x axis label'''
diabetes_x_train=diabetes_x[:-30]
diabetes_x_test=diabetes_x[-30:]

'''print(diabetes_x_train)
print(diabetes_x_test)'''

'''y axis features'''

diabetes_y_train=diabetes.target[:-30]
diabetes_y_test=diabetes.target[-30:]


model=linear_model.LinearRegression()

model.fit(diabetes_x_train,diabetes_y_train)

diabetes_y_predicted=model.predict(diabetes_x_test)

print("Mean squared error is: ",mean_squared_error(diabetes_y_test,diabetes_y_predicted))

print("weights ",model.coef_)
print('intercept', model.intercept_)

plt.scatter(diabetes_x_test,diabetes_y_test)
plt.plot(diabetes_x_test,diabetes_y_predicted)
plt.show()