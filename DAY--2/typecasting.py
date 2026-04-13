#type casting:
#The conversion of value from one data type to another data type is called typecasting.
#There are various predefined functions available for typecasting.


#int() used to convert an integer  
print(int(3.14))    #3
#print(int(10+5j))    # we cannot convert complex value to int
print(int(True))     #1
print(int(False))     #0
# print(int("4.22"))    #we cannot convert floating point value string to int
print(int("4"))      #4


#float() used to convert in float
print(float(3))         #3.o
#print(float(50+2j))     #the complex number is not possible
print(float(True))    #1.0
print(float(False))    #0.0
print(float(4.22))     #4.22
print(float("4"))       #4.o


#bool() is used to convert in boolean value 
print(bool(0))  #False
print(bool(15))    #True
print(bool(3.14))    #True
print(bool(0.0))      #False
print(bool(1+2j))    #True
print(bool(0+0j))       #False
print(bool(-1))         #True
print(bool(False))      #False
print(bool(True))    #True
print(bool(""))      #False


#WAP to check if three variables have the same value so all the three variable addresses are the same.
#( Using id() function we can check the address) 
math=50
che=50
phy=60
print(id(math))
print(id(che))
print(id(phy))


#WAP to check if values are different so memory addresses are different.
math = 100    
chemistry = 50    
physics = 70    
print(id(math))    
print(id(chemistry))    
print(id(physics)) 


# input function it takes by default string value
print(2+2)
print("2"+"2")
val1=input("Enter value 1:\t")
val2=input("Enter value 2:\t")
print(val1+val2)


# WAP it accept five numbers in 5 different variables and check maximum number and print it
n1=int(input("Enter a number1:"))
n2=int(input("Enter a number2:"))
n3=int(input("Enter a number3:"))
n4=int(input("Enter a number4:"))
n5=int(input("Enter a number5:"))
if n1>n2 and n1>n3 and n1>n4 and n1>n5:
    print("number1 is max",n1)
if n2>n1 and n2>n3 and n2>n4 and n2>n5:
    print("number2 is max",n2)
if n3>n1 and n3>n2 and n3>n4 and n3>n5:
    print("number3 is max",n3)
if n4>n1 and n4>n2 and n4>n3 and n4>n5:
    print("number4 is max",n4)
if n5>n1 and n5>n2 and n5>n3 and n5>n4:
    print("number5 is max",n5)


#WAP to accept three subject marks and calculate total percentage is greater than or equal 60 so he\she is eligibal for placement drive
math=int(input("Enter marks for maths:"))
che=int(input("Enter marks for chemistry:"))
phy=int(input("Enter marks for physics:"))
per=math+che+phy/3.0
if per>=60:
    print("he/she eligibal for placement drive")
else:
    print("he/she not eligibal for placement drive")
print(per)


# WAP to accept only digits in that positive,negative,nutral it display
n=int(input("Enter a integer:\t"))
if n>0:
    print("positive number")
if n<0:
    print("Negative number")
if n==0:
    print("it is zero")
     

# input function it takes by default string value
print(2+2)
print("2"+"2")
val1=input("Enter value 1")
val2=input("Enter value 2")
print(val1+val2)
