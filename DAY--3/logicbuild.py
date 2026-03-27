#wap to accept three numbers like a,b,c and find maxmum number
# using nested if else:
a=int(input("Enter the value 1:"))
b=int(input("Enter the value 2:"))
c=int(input("Enter the value 3:"))
if a>b:
    if a>c:
        print("A is greater")
    else:
        print("c is greater")
else:
    if b>c:
        print("b is greater")
    else:
        print("c is greater")



#wap to accept three numbers like a,b,c and find minmum number
# using nested if else:
a=int(input("Enter the value 1:"))
b=int(input("Enter the value 2:"))
c=int(input("Enter the value 3:"))
if a<b:
    if a<c:
        print("A is smaller")
    else:
        print("c is smaller")
else:
    if b<c:
        print("b is smaller")
    else:
        print("c is smaller")

#displayind all elements in list
mylist=[3,4,5,6,7]
for i in mylist:
    print(i)



# in c language for loop for(intialization;cond;inc/decr)
#in python range() function is used
#display starting number 0 to 4 using for loop
for i in range(5): #start from 0 to 4
    print(i)

#display starting number 1 to 4 using for loop
for i in range(1,5): #start from 1 to 4
     print(i)


#displaying numbers from 1 to 10 and difference 2
for i in range(1,11,2): 
    print(i)

#display tables from 2 to 18 side by side
for i in range(1,11): 
    print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ")
print("--------------------------------------------------------------------------")
for i in range(1,11): 
    print(i*11," ",i*12," ",i*13," ",i*14," ",i*15," ",i*16," ",i*17," ",i*18," ")


#comparision operator to verify password 
username=input("Enter user password:")
password=input("Enter password:")
if username==password:
    print("login successfull")
else:
    print("invalid login")



# example for elif ladder
brand=input("enter your colddrink name either in upper case or in lower case but not combine:")

if brand=="pepsi" or brand=="PEPSI":
    print("swag")
elif brand=="dew" or brand=="DEW":
    print("dar age jeet hai")
elif brand=="thumsup" or brand=="THUMSUP":
    print("taste the thunder")
else:
    print("go with your brand")


# exaple for logical and operator
n1=int(input("enter first number"))
n2=int(input("enter second number"))
n3=int(input("enter third number"))
if n1>n2 and n1>n3:
    print("n1 is biggest number:",n1)
elif n2>n3:
    print("n2 is greater number:",n2)
else:
    print("n3 is greater number:",n3)

# counting even numbers range from 1 to 9
count=0
for i in range(9):
    if i%2==0:
        print(i)
    else:
        print(i)
        count+=1
print("count=",count)