import numpy as np
# np1 = np.array([0,1,2,3,4,5])
# print(np1)
# print(np1[1:5])
a = input("enter your 1st number ")
b= input( "enter your 2nd number ")
sum1= float(a)+ float(b)
minus= float(a) - float(b)
multiply= float(a) * float(b)
input1= input("type sum for + " \
"type minus for -"
"type multiply for *")

if input1 == "sum":
    print(sum1)
elif input1== "minus" :
    print(minus)
elif input1== "multiply":
    print(multiply)
else: 
    print ("invalid")
