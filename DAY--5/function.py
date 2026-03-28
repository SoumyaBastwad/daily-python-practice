#user defined function
def msg():        #called function
    print("hello")

msg()    #calling function
msg()


#login by using user defined program
def login():
    username=input("enter user nsme:")
    password=input("enter password:")
    if username==password:
        print("login successful")
    else:
        print("Invalid credential")
login()


# how many types of arguments we can pass in function
# positional argument
# keyword argument
# defautl argument
#variable length argument/variable number of argument

#positional argument
def add(x,y):  #called function
    print("Add=",x+y)

add(2,3) #calling function

#example for positionl argument we can pass in function
def add(x,y):
    print("add=",x+y)

a=int(input("enter the value a:"))
b=int(input("enter the value of b:"))
add(a,b)

#example 2
def add(x,y):
    return x+y
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
print(add(a,b))


#example  3
def add(x,y):
    return x+y
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
print(add(a,b))
result=add(a,b)
print("add=",result)

#in python it is possible to return multiple values
def add(x,y):
    add= x+y
    sub=x-y
    mul=x*y
    div=x/y
    return add,sub,mul,div  #return in tuple
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
print(add(a,b))
result=add(a,b)
print("add=",result)


# keyword argument in parameter name and keyword name is must match
def personalinfo(fname,lname):
    print("First name:",fname)
    print("Last name:",lname)

personalinfo(fname="soumya",lname="bastwad")


#default argument
def cityname(city):
    print("City name:",city)

cityname("pune")
cityname("kholapur")
cityname()  # error  cityname() missing 1 required positional argument: 'city'

#example  2
def cityname(city="delhi"):
    print("City name:",city)

cityname("pune")
cityname("kholapur")
cityname()         # here it's taking default argument delhi


#example
def cityname(city="delhi"):
    print("City name:",city)

cityname("pune")


#variable length argument\variable number of arguments
def cityname(*city):
    print("City name:",city)

cityname("pune","belgaum","goa","mumbai")


#nested function
def outerfunction():
    print('outer function')
    def innerfunction():
        print("inner function")
    innerfunction()
outerfunction()


