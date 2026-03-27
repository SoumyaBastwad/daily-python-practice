
# count() it is used to count the objects in list
n=[1,2,3,5,5,5,1,2,4,4,6,6,6]
print(n.count(1))
print(n.count(2))
print(n.count(3))
print(n.count(4))
print(n.count(5))
print(n.count(6))

# index() function
val=[1,2,3,5,5,5,1,2,4,4,6,6,6]
print(val.index(1))
print(val.index(2))
print(val.index(3))
print(val.index(4))
print(val.index(5))
print(val.index(6))


#when we needed pre defined function we import the module in python
# for example we import datetime method for know current date time in our system
import datetime
date=datetime.datetime.now()
print("It's now:{:%d/%m/%y %H:%M:%S}".format(date)) 


#Break Statement:
#Break statements break the loop immediately and we can use break statement in any loop like for loop, while loop, nested for loop.
for i in range(1,5):
    if i==3:
        break
    print(i)


#Continue Statement:
# Continue statement skips the current iteration and moves to the next.
for i in range(1,5):
    if i==3:
        continue
    print(i)

#example for continue statement
mycart=[10,20,200,300,800,60,700]
for i in mycart:
    if i>400:
        print("this my purchased cart item")
        continue
    print(i)


#sum of first 10 list  numbers
list=[1,2,3,4,5,6,7,8,9,10]
sum=0
for x in list:
    sum=sum+x
print('the sum =',sum)


#logical or operatour and break statement
rollno=[3,5,7,1,11,4,5,2]
for x in rollno:
    if x==2 or x==4 or x==6 or x==8 or x==10:
        print("even no is found",x)
        break


#disply string using for loop it's dividing string
name="prashanth"
for i in name:
    print(i)



#program to remove duplicate character
name="pooja"
newname=" "
for i in name:
    if i not in newname:
        newname+=i
        print(newname)


#reverse sting using for loop
name="soumya"
for i in range(-1,-7):
    newname+=i
    print(newname)


#Find index of a specific character 
name="soumyabastwad"
i=0
for x in name:
    if x=='n':
        print("The character index is:",i,"value=",x)
        break
    i=i+1

# count the total number of vowels and consonents
name="soumya"
vow=0
con=0
vowels=['a','e','i','o','u']
for i in name:
    if i in vowels:
       vow+=1
    else:
        con+=1
print("no of vowels:",vow)
print("no of consonents:",con)


#print numbers in reverse order from 5 to 0
for i in  range(5,0,-1):
    print(i)


#program to calculate factorial
fact=1
for i in  range(1,6):
     fact=i*fact
print("factorial of 5:",fact)


#sample A=[1,2,3] B=[2,3,4] C=[3,4,5] output=3 / to check common element in all given list
A=[1,2,3]
B=[2,3,4]
C=[3,4,5]
for i in A:
    if i in B and i in C:
        print(i)

