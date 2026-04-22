#predefined modules
import math
print(math.sqrt(4))
print(math.pi)

#alias name for module
import math as m
print(m.sqrt(4))
print(m.pi)


#random module:
# this module defines several function to generaate 
#random number
#we can use these function while developing developing games
from random import *
for i in range(5):
    print(random())


# To generate random integer between two given numbers(inclusive)
from random import *
for i in range(5):
    print(randint(1,1000))


#choice() function:
# it wont return random number
#it will return a raandom object from the given list or tuple
from random import *
list=["prashanth","rahul","ashish","sandip","sumil","nikkil"]
for i in range(10):
    print(choice(list))

# valueerror
a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60
print(a)

#output  for this code [4,3,2]
a=[1,2,3,4,5]
print(a[3:0:-1])

# output for this code is 3 44
def func(value,values):
    var=1
    values[0]=44
t=3
v=[1,2,3]
func(t,v)
print(t,v[0])

# output for this code is 4 7 11 15
arr=[[1,2,3,4],
     [4,5,6,7],
     [8,9,10,11],
     [12,13,14,15]]
for i in range(0,4):
    print(arr[i].pop())


# output for this code is [1] [1,2] [1,2,3]
def f(i,values=[]):
    values.append(i)
    print(values)
f(1)
f(2)
f(3)

# output of this code is 22
fruit_list1=['apple','berry','cherry','pappya']
fruit_list2=fruit_list1
fruit_list3=fruit_list1[:]
fruit_list2[0]='guava'
fruit_list3[1]='kiwi'

sum=0
for ls in (fruit_list1,fruit_list2,fruit_list3):
    if ls[0]=='guava':
        sum+=1
    if ls[1]=='kiwi':
          sum+=20
print(sum)

