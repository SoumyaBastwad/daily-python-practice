#Collection Datatype 
# There are four types of collection data types they are given below: 
# List
# Tuple
# Set
# Dictionary


#Perform List Slicing which basics but very important:
mylist=["soumya","sinchana","srushti","komal","poornima",3,4,"shreya",68.9,"prashanta"]
print(mylist)         #["soumya","sinchana","srushti","komal","poornima",3,4,"shreya",68.9,"prashanta"]
print(type(mylist))   #<class 'list'>
print(mylist[0])       #soumya
print(mylist[1])         #sinchana
print(mylist[-1])         #prashanta
print(mylist[2:5])        #["srushti","komal","poornima",3]
print(mylist[:6])       #["soumya","sinchana","srushti","komal","poornima",3,4]
print(mylist[1:])        #["sinchana","srushti","komal","poornima",3,4,"shreya",68.9,"prashanta"]
print(mylist[1:8:2])      #["sinchana","komal",3,"shreya"]
print(mylist[:])          #["soumya","sinchana","srushti","komal","poornima",3,4,"shreya",68.9,"prashanta"]
print(mylist[::-1])     #['prashanta', 68.9, 'shreya', 4, 3, 'poornima', 'komal', 'srushti', 'sinchana', 'soumya']


#to check list is mutable means change the value
mylist=["soumya","sinchana","srushti","komal","poornima",3,4,"shreya",68.9,"prashanta"]
mylist[2]="tania"
print(mylist)     #['soumya', 'sinchana', 'tania', 'komal', 'poornima', 3, 4, 'shreya', 68.9, 'prashanta']


# in is a membership operator we used to check value is present or not
if "komal" in mylist:
    print("yes komal is avilable")
else:
    print('not available')


# append() method id used to add new object at the end
mylist=['soumya', 'sinchana', 'tania', 'komal', 'poornima', 3, 4, 'shreya', 68.9, 'prashanta']
mylist.append('harsh')
mylist.append('laxmi')
print(mylist)

#  using a insert method to add object a specified position
mylist=['soumya', 'sinchana', 'tania', 'komal', 'poornima', 3, 4, 'shreya', 68.9, 'prashanta']
mylist.insert(1,"pooja")
print(mylist)

#remove() method is used to remove object from the list
mylist=['soumya', 'sinchana', 'tania', 'komal', 'poornima', 3, 4, 'shreya', 68.9, 'prashanta']
mylist.remove('komal')
print(mylist)

#copy() method is used to copy the list objects to one list another
mylist=['soumya', 'sinchana', 'tania', 'komal', 'poornima', 3, 4, 'shreya', 68.9, 'prashanta']
newlist=mylist.copy()
print(newlist)


#multidimentional list
mlist=[['prashanth','jha'],['85.67'],[440022,"yyy"]]
print("example of multidimentional list:")
print(mlist)      #print(mlist[row][col])
print(mlist[0][0])   # prashanth
print(mlist[0][1])   # jha
print(mlist[1][0])   #85.67
print(mlist[2][0])   #440022
print(mlist[2][1])   #yyy


#multiplication in list
list1=["soumya","bastwad"]
print(list1*2)

#adding two list
list1=["soumya","bastwad"]
list2=[50,25.25]
print(list1+list2)

#we can delete particular index value
list2=[50,45.32,"soumya"]
del list2[2]
print(list2)


# print items in list one by one using for loop
v=[1,2,3,4,5]
for i in v:
    print(i)


# we want empty list
list2=[50,45.32,"soumya"]
list2.clear()
print(list2)   #[]


# List typecasting using 'list()' function  
name = "prashant"  
print(name)  # Output: prashant  
myname = list(name)  
print(myname)  # Output: ['p', 'r', 'a', 's', 'h', 'a', 'n', 't']  
  
# Reversing a list using 'reverse()' function  
mylist = [40, 30, 20, 10]  
mylist.reverse()  
print(mylist)  # Output: [10, 20, 30, 40]  
  
# Sorting a list using 'sort()' function  
mylist = [44, 22, 77, 0, 9, 88]  
mylist.sort()  
print(mylist)  # Output: [0, 9, 22, 44, 77, 88]  
  
# Sorting a list in descending order  
mylist.sort(reverse=True)  
print(mylist)  # Output: [88, 77, 44, 22, 9, 0]  
  
# Implementing aliasing concept  
mylist = [44, 22, 77, 0, 9, 88]  
newlist = mylist  
print(id(mylist))  # Output: same id  
print(id(newlist))  # Output: same id  
  
# Implementing 'count()' function  
n = [1, 2, 3, 5, 5, 5, 1, 2, 4, 4, 6, 6, 6]  
print(n.count(1))  # Output: 2  
print(n.count(2))  # Output: 2  
print(n.count(3))  # Output: 1  
print(n.count(4))  # Output: 2  
print(n.count(5))  # Output: 3  
print(n.count(6))  # Output: 3  
print(n.count(7))  # Output: 0  
  
# Returning the last element using 'pop()' function  
list1 = [3, 4, 5, 6, 7]  
print(list1.pop())  # Output: 7  



#A String is a sequence of characters enclosed within single quotes or double quotes.
name="soumya"  #str
print(name)
myname=list(name) # typecasting=converting str into list
print(myname)


# WE have used list constructor
#for reverse list:
mylist=[40,30,20,10]
mylist.reverse()
print(mylist)

# sorting elements in ascending order
mylist=[44,22,77,0,9,88]
mylist.sort()
print(mylist)

# sorting elements in decending order
mylist=[44,22,77,0,9,88]
mylist.sort(reverse=True)
print(mylist)


# default sorting order for number is ascending order
# default sorting order for string is string is alphabetical order
# we should know that list should contain homogenious
#data otherwise we will get type error

# both the list having same address
mylist=[44,22,77,0,9,88]
newlist=[56,78,43,67,3]
newlist=mylist
print(id(mylist))
print(id(newlist))


#Tuple== tuple is exactly as similar as list data type only the difference is that list is mutable but tuple is immutable
#tuple is represented in () it is optional
#Duplicate data are also allowed
#tuple by nature is growable means if you add the value consciously tuple variable size will grow and similarly when you remove the objects from list it’s size automatically decreases.
#It is Immutable means we cannot change the value

#Tuple used to store multiple items in a single variable
mytuple=("prashant","alish","sandeep","komal","ankush","rajesh",23,3.15,77,"sandip")
print(mytuple)
print(type(mytuple))
print(mytuple[5])

# #tuple is immutable
mytuple[2]="sunil"
print(mytuple)

#membership operator : in and not in
print("z" in "soumya")
print("z" not in "soumya")
print("a" in "soumya")
print("a" not in "soumya")
mylist=[3,5,2,8,9]
print(3 in mylist)

#identity operators used for compare the address
#when we want do address comparison 
a=10
b=10
print(id(a))
print(id(b))
print(a is b)            #true
print(a is not b)         #false

# Set Data Type:
# If we don’t want duplicate values and we want to represent random data that means, there is unordered collection of unique elements then we should go for set datatype.
# No Order wise data (unordered and unique element)
# Heterogeneous data are possible in set like (integer, float, string)
# set represented by { } curly braces
# Duplicate data are not allowed
# set by nature it is growable 

#set datatype==if we dont want duplicate value and we want to represent random data
myset={1,2,"soumya",5.66,"rahul","ravi","ankita","rashika"}
print(myset)
print(type(myset))
print(myset[0])    #'set' object is not subscriptable
myset.add(60)
print(myset)
myset.remove(3)
print(myset)

#union
myset={10,20,30,40}
yourset={"prashant","jha"}
newset=myset.union(yourset)
print(newset)

#intersection
myset={10,20,30,40}
yourset={10,50,69,30}
print(myset.intersection(yourset))

#difference() method this will return the element 
#present in first set but not in second set
myset={10,20,30,40}
yourset={10,50,60,30}
print(myset.difference(yourset))

# clear() we can use to clear data
# pop() method is used to remove object
myset={10,20,30,40}
print(myset.clear()) #None





