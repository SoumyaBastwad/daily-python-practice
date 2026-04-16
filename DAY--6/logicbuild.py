# example for while loop to print 1 to 5
i=1
while i<=5:
    print(i)
    i=i+1


# count the how many even number and odd number in 1 to 10
i=1
even=0
odd=0
while i<=10:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
    i=i+1
print("total number of even numbers:",even)
print("total number of even numbers:",odd)


# sum of natural numbers using while loop
i=1
total=0
while i<=10:
    total=i+total
    i=i+1
print(total)


# factorial of 5 using while loop
fact=1
i=1
while i<=5:
    fact=fact*i
    i=i+1
print(fact)


# output is 1 5
#           2 4
#           4 2
#           5 1 using loop
for i,j in zip(range(1,6),range(5,0,-1)):
    if i==3 and j==3:
        continue
    print(i,"  ",j)


#nested for loop patern
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end="  ")
    print()


#ASCII upercase letters in matrix format
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end="  ")
    print()


# pattern example
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i,end="  ")
    print()

# pattern example
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,1+i):
        print(i,end="  ")
    print()

# wap to manu driven code
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
