#class=======================================================
# naming convention rule =classname start with capital letter
class Student:
    a=10    #data member
    b=20
    def add(self):           #self is default argument
        print(self.a+self.b)

#object creation====================================================
obj=Student()
obj.add()              # we call method using . 
print(obj.a)
by default everything in class like variable,functions are public


#constructor call automatically whenever we create object or we can say that at the time of creation of object
#internally also we have constructors
#for one object it call one constructor
class NewClass:
    def __init__(self):  # constructor declaration (called automatically)
        print("constructor allways execute first")
    def show(self):
        print('welcome to class level progrsmming')
obj=NewClass()
# print(obj)
obj.show()
obj1=NewClass()

# example for constructer
class Hod:
    def __init__(self):   #constructor
        self.name="soumya"
        self.age=20
        self.empid=102
    def info(self):      #instance method
        print("My name is:",self.name)
        print("My age is:",self.age)
        print("My id is",self.empid)
obj=Hod()             # object creation
obj.info()          

#parameterized constructor
class Hod:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
    def show(self):
        print("My name is:",self.name)
        print("My age is:",self.age)
        print("My id is",self.rollno)

obj=Hod("soumya",20,102)
obj.show()
        

# how many types of variables we declare inside class
# instance variable: we can declare instance variable using self keyword inside constructor
# static variable
# local variable

#insrance variable
class Student:
    def __init__(self):
        self.name="soumya"  #instance variable
        self.age=20
        self.id=102
    def getdata(self):
        self.mb=9182930423   #instance variable
obj=Student()
obj.getdata()
obj.s_branch="cs"            # outside class instance variable by using object
print(obj.__dict__)
print(obj.mb)


#for every object create separate memory
class New():
    def __init__(self):
        self.a=10

obj1=New()      # it's creating separate memory for every objects
obj2=New()
obj3=New()
obj1.a=20          # it is only effect obj1 not obj2 and obj3
print(obj1.a)
print(obj2.a)
print(obj3.a)


# static variable
# static variable creates only one memory for total class and this will assiable for all objects
# by using class name we can access static variable
# we can read or access static variable but can't delete or change
# static variable doesnot depend on object
class New:
    a=10            #static variable
    def __init__(self):
        self.name="soumya"            #instance variable
obj1=New()
obj2=New()
obj3=New()
print(obj1.a)
print(obj2.a)
print(obj3.a)
New.a=20  # we can changing the value of static var using classname
print(obj1.a)
print(obj2.a)
print(obj3.a)


# there are three types of metohds can use in class
# static metod
# instance method :if any variable we are implementing inside of any method then that method is called instance metod  
# class method

#instance method 
class Student:
    def __init__(self,name,rollno,mob):
        self.name=name       # instance variable
        self.rollno=rollno
        self.mob=mob
    def display(self):            # instance method
        print(self.name," ",self.rollno," ",self.mob)
stud=Student("soumya",35,9348028244)
stud.display()


#static method==========================================
class Student:
     # by using class name we can access static method
    @staticmethod         # decorator
    def get_personal_detail(firstname,lastname):
        print("your personal detail:",firstname,lastname)
    @staticmethod
    def contact_detail(mobile,rollno):
        print("your contact detail:",mobile,rollno)

Student.get_personal_detail("soumya","bastwad")
Student.contact_detail(823619401,35)


#class method our work

#inheritance====extending properties from one class to another class
#Base class:A class which inherits it's property to another is called baseclass or parent class
#derived class:A class in which properties are inherited called as derived class or child class
# types of inheritamnce
#1.single    #2.multilevel    #3.multiple


#single inheritance sytax
#class derived-class(base-class):

class College:
    def college_name(self):
        print("hsit")

class Student(College):
    def student_info(self):
        print("Name:soumya")
        print("brach:cse")
obj=Student()
obj.college_name()
obj.student_info()
                     

# multilevel inheritance syntax
# class Grandfather:
#        _______________
# class Father:
    # _____________________
# class Child:
#         ________________

class College:        #first class first level
    def college_name(self):
        print("hsit")
#======================================================
class Student(College):     #secong class 2nd level
    def student_info(self):
        print("Name:soumya")
        print("brach:cse")
#======================================================
class Exam(Student):      #third class 3rd level
    def subject(self):
        print("subject1:math")
        print("subject2:os")
#======================================================
obj=Exam()
obj.college_name()
obj.student_info()
obj.subject()


#multiple inheriance syntax
# class A:
# class B:
#class C:
# class derived(A,B,C,_______)

class SubjMarks:
    math=int(input("enter a marks of maths"))
    de=int(input("enter a marks of de"))
    english=int(input("enter a marks of english"))

class PractMarks:
    react=int(input("enter marks of react"))

class Reasult(SubjMarks,PractMarks):


# metod overloading: method is same overloding is diff
# python support only operator ovedrloading
#method overloading is not possiable in python 
# if we are trying to declare multiple method with same name and different number of arguments then python will always aonsider only last method 
class Arithmatic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
obj=Arithmatic()                #error
obj.add(10)
obj.add(10,20)
obj.add(1,2,3)

# solution
# to handle overloading method in python
# if method with vriable number of arguments required then we can handle with default arguments x
class Arithmatic:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None:
            print(a+b)
        elif a!=None and b!=None and c!=None:
            print(a+b+c)
        else:
            print("enter atleast two argument")
obj=Arithmatic()
obj.add(10)
obj.add(10,20)
obj.add(1,2,3)


#constructor overloading constructor name are same but diff arguments
#constructor overloading is not possible in python 
# if we define multiple constructors then last constructor will be considered
class Arthmatic:
    def __init__(self):
        print("there is no argument")
    def __init__(self,a):
        print("passing one argument")
    def __init__(self,a,b):
        print("passing two argumenta")
obj=Arthmatic()
obj=Arthmatic(10)
obj=Arthmatic(2,2)


#operator overloading
#operator overloading
class Deposit:
    def __init__(self,cash):
        self.cash=cash
d1=Deposit(1000)
d2=Deposit(2000)
print(d1+d2)                        #error
# solution for this is by using magic method
# magic method avilable for every operator to overloading any operator we 
#have to override that method in our class
#the __add_ method is a magic method which gets called when we add two numbers
# using + operator
class Deposit:
    def __init__(self,cash):
        self.cash=cash
    def __add__(self,other):
        return self.cash+other.cash
    
d1=Deposit(1000)
d2=Deposit(2000)
print("total cash deposit amount",d1+d2)

#overriding
#in overriding method appling when parent amd child relationship
# when child class not happy with parent class property child class can override parent class method
class Rbi:
    def homeLoan_ROI(self):
        print("home loan rate of interest=7.5%")
    def carLoan(self):
        print("car loan rate of interest=8%")
class Sbi(Rbi):
    def homeLoan_ROI(self):
        print("home loan rate of interest=8.5")
obj=Sbi()
obj.homeLoan_ROI()
obj.carLoan()


# using super method we can accesss parent class method in child
class Rbi:
    def homeLoan_ROI(self):
        print("home loan rate of interest=7.5%")
    def carLoan(self):
        print("car loan rate of interest=8%")
class Sbi(Rbi):
    def homeLoan_ROI(self):
        print("home loan rate of interest=8.5")
        super().homeLoan_ROI()

obj=Sbi()
obj.homeLoan_ROI()
obj.carLoan()

#python supports method overriding and constructor overriding

# constructor overriding
class Father:
    def __init__(self):
        print("Father :=i am already at breakfast table")
class Child(Father):
    def __init__(self):
        print("Child:=i will be late for breakfast")
obj=Child()

#abstract
# a class which can contain one or more abstract method is called abstract class
from abc import ABC,abstractmethod
class Help4code(ABC):
    @abstractmethod
    def training(self):
        pass
    @abstractmethod
    def placement(self):
        pass
class Ashish(Help4code):
    def training(self):
        print("c,c++,java")
    def placement(self):
        print("java placement")

class Ankush(Help4code):
    def training(self):
        print("python|Django")
    def placement(self):
        print("python placement student")

class Prashanth(Help4code):
    def training(self):
        print("machine learning")
    def placement(self):
        print("Data science placement")

obj1=Ashish()
obj1.training()
obj1.placement()

obj2=Ankush()
obj2.training()
obj2.placement()

obj3=Prashanth()
obj3.training()
obj3.placement()


# example for abstract
from abc import ABC,abstractmethod
class Irctc(ABC):

    @abstractmethod
    def bookTicket(self):
        pass
    
class MakeMyTrip(Irctc):
      def bookTicket(self):
          print("==================================================================")
          print("      welcome to makemytrip.com        ")
          source    =input("enter a source station name")
          destination=input("enter a destination name")
          date =input("enter date")
          print("==================================================================")
class GoIbibo(Irctc):
      def bookTicket(self):
          
          print("      welcome to GOIBIBO        ")
          source    =input("enter a source station name")
          destination=input("enter a destination name")
          date =input("enter date")
class Yatra(Irctc):
      def bookTicket(self):
          
          print("      welcome to Yatra.com        ")
          source    =input("enter a source station name")
          destination=input("enter a destination name")
          date =input("enter date")         

m=MakeMyTrip()
m.bookTicket()
g=GoIbibo()
g.bookTicket()
y=Yatra()
y.bookTicket()