# Dictionary Data Type:
# In dictionary we store the data as key and value pair 
# dict represented by {key:value } parenthesis 
# Duplicate keys are not allowed 
# Duplicate values are allowed 
# dict by nature it is growable 
#  It is mutable dictionary is Unordered 
#  Dictionary is a mapping types If you try to access the value which does not exist then you will get error 
# Values are accessed using keys, not by indexing.


mydict={"name":"soumya","professional":"student","rollno":35}
newmydict={"name":"pooja","professional":"stu","rollno":45}
print(mydict)
print(type(mydict))
print(id(mydict))
print(id(newmydict))

mydict={101:"prashanta",102:"ashish","103":"mohini","104":"trisha",101:"ashish",104:"ashish"}
print(mydict)

# with the help of key we can print value
a=mydict[102]
print(a)

# # we will replace old value by new value
mydict[102]="soumya"
print(mydict)

#Print only keys using a loop
for x in mydict:
    print(x)


#just value we get by using values() function
for x in mydict.values():
    print(x)


# Print keys and values using items() function  
for x,y in mydict.items():
    print(x,y)


# if i have to add new key and value pair in my dictionarty
mydict["mobile no"]=9740270004
print(mydict)

# using pop() to remove key and value
mydict={"name":"soumya","professional":"student","rollno":35}
mydict.pop("name")
print(mydict)


#copying dictionary by using copy() function
mydict={"name":"soumya","professional":"student","rollno":35}
newdict=mydict.copy()
print(mydict)
print(newdict)


