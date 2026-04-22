# write a program to find maximum and minimum elements in array
# sample input:[5,3,9,2,8]
arr=[5,3,9,2,8]
max=arr[0]
min=arr[0]
for i in arr:
    if i>max:
        max=i
    if i<min:
        min=i
print("Maximum",max)
print("Minimum",min)

# write a program to reverse the order of element in array
# sample input:[1,2,3,4,5]
arr=[1,2,3,4,5]
print(arr[::-1])
#or
arr=[1,2,3,4,5]
rev=[]
for i in arr:
    rev=[i]+rev
print(rev)
#or
arr=[1,2,3,4,5]
rev=[]
for i in range(len(arr)-1,-1,-1):
      rev.append(arr[i])
print(rev)

# write a program to check if a list is palindrome or not
arr=[1,2,3,2,1]
rev=[]
for i in range(len(arr)-1,-1,-1):
      rev.append(arr[i])
if rev==arr:
     print("given list is palindrome")
else:
     print("given list is not a palindrome")

# write a program to check if a key exists in a dictionary 
dict={"name":"soumya","age":20,"usn":"2hn23cs102"}
key="age"
if key in dict:
     print("key exists in dict")
else:
     print("key not exists in dict")

# write program to iterate over the keys and values of a dictionary
dict={"name":"soumya","age":20,"usn":"2hn23cs102"}
for key in dict:
     print(key,":",dict[key])

# reverse a string
str="soumya"
rev=""
for i in str:
     rev=i+rev
print(rev)

# write a program to check if a list is palindrome or not
str="racecar"
rev=""
for i in str:
     rev=i+rev
if rev==str:
     print("palindrome")
else:
     print("not palindrome")
