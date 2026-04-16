# types of errors
# syntax error
# runtime error

#syntax error comes when we do not follow proper syntactical rule means predefined grammatical rules
#runtime error 

# in exception there are 2 types predefined exception and user defined exception
a=int(input("enter any one number"))
b=int(input("enter second number"))
print(a/b)  #if 5/0 ZeroDivisionError: division by zero

# runtime error is also known as exception

#exception handling ZeroDivisionError: division by zero
a=int(input("enter any one number"))
b=int(input("enter second number"))
try:
     print(a/b) 
except:
     print("can't devide by 0")

# value error exception handling
a=int(input("enter any one number"))
b=int(input("enter second number"))  #ValueError: invalid literal for int() with base 10: '*'
print(a/b) 



# value error exception handling
try:
      a=int(input("enter any one number"))
      b=int(input("enter second number"))  
      print(a/b) 
except (ZeroDivisionError):
       print("can't devisible by 0")
except (ValueError):
       print('enter only integers')

# exception handling
a=int(input("enter any one number"))
b=int(input("enter second number"))  # if suppose input 5/0
try:
      print(a/b) 
except ZeroDivisionError as message:
       print("the description of exception :",message) # output:the description of exception : division by zero 


# Handling multiple different kinds of exception with singke except block
try:
    a=int(input("enter any one number"))
    b=int(input("enter second number"))  
    print(a/b) 
except (ValueError,ZeroDivisionError) as message:
      print(message)


# the concept of default except block ,
#generally we used for writing normal message or showing normal error     
try:
    a=int(input("enter any one number"))
    b=int(input("enter second number"))  
    print(a/b) 
except (ValueError,ZeroDivisionError) as message:
      print("enter correct number:",message)
except:
     print("this is default part of except block")
     

             
# we can use else block if no error will generate it is depend on our own need and necessity
try:
    a=int(input("enter any one number"))
    b=int(input("enter second number"))  
    print(a/b) 
except (ValueError,ZeroDivisionError) as message:
       print("enter correct number:",message)
else:                                       # if there is no exception then else excuits
      print("Everyting is ok")
    

# finally block will always execuited whether try block generate error or not 
try:
    a=int(input("enter any one number"))
    b=int(input("enter second number"))  
    print(a/b) 
except (ValueError,ZeroDivisionError) as message:
       print("enter correct number:",message)
finally:                                    
      print("i will always execute")


# nested try except block
try:
    a=int(input("enter any one number"))
    b=int(input("enter second number"))  
    try:
        print(a/b)
    except ZeroDivisionError as message:
        print(message)
except ValueError as message:
      print(message)


# exception ,else and finally block
try:
     a=int(input("enter any one number"))
     b=int(input("enter second number"))  
     print(a/b) 
except (ValueError,ZeroDivisionError) as message:
       print(message)
else:
     print("there are no error in try block")
finally:                                    
      print("i am finally block i will always execute")


# user defined exception by raise keyword
bank_bal=500
if bank_bal<2000:
    raise Exception("your account balance is below a acessing limit")
else:
    print("your amount has withdrawal")


# write program  to manu driven code
import sys
def addition():
    a=int(input("enter a value:"))
    b=int(input("enter b value:"))
    print("Addition=",a+b)
def substraction():
    a=int(input("enter a value:"))
    b=int(input("enter b value:"))
    print("Substraction=",a-b)
def multiplication():
    a=int(input("enter a value:"))
    b=int(input("enter b value:"))
    print("Multiplication=",a*b)
def Division():
    a=int(input("enter a value:"))
    b=int(input("enter b value:"))
    print("Division=",a/b)
while True:
    print("1.Addition:")
    print("2.Substraction:")
    print("3.Multiplication:")
    print("4.Division:")
    print("5.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        addition()
    elif choice==2:
        substraction()
    elif choice==3:
        multiplication()
    elif choice==4:
        Division()
    elif choice==5:
        sys.exit()
