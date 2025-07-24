"""genrality to specificity"""
from functools import reduce
from xmlrpc.client import boolean

'''class is a blueprint
class name
object must belong any class'''
# a=2
# print(type(a))
'''a is a object belongs to class integer
class will have data (attributes) and functions or behaviour'''

'''object is a instance of class or real world entity
car---->alto , alto is a object of class Car'''
#alto=Car()

'''function is a normal function which is not in a class
method is a function which is inside of class'''
l=[1,2,3]
# print(len(l))
'''here we are passing list inside a function its an inbuilt function
'''
l.append(2)

'''here append is a method inside a list class we are calling it as object.method()
constructor is a special method which executes automatically when object of that class created'''
# class Atm:
#     def __init__(self):
#         print("hello")
#
# obj=Atm()
'''here hello is printed,constructor gets executed when object of that class is created
'''
class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0

        self.menu()

    def menu(self):
        user_input=int(input('''
        1.Enter 1 to create pin
        2.Enter 2 to deposit
        3.Enter 3 to withdraw
        4.Enter 4 to check balance
        5,Enter 5 to exit
        '''))

        if user_input==1:
            self.create_pin()
        elif user_input==2:
            print("withdraw")
        elif user_input==3:
            print("deposit")
        elif user_input==4:
            print("balance")
        else:print("bye")

    def create_pin(self):
        self.pin=input("Enter your pin")
        print("pin set successfully")


# print(Atm.create_pin())

# class Employee:
#     def __init__(self):
#         self.__password = "secret"  # Private
#
# emp = Employee()
# print(emp._password)        #  AttributeError
# print(emp._Employee__password)#  Works (but not recommended)
# emp._Employee__password="ed"
# print(emp._Employee__password)
# print(emp.get_password)


# class Xyz :
#     # def __init__(self,name=None):
#     #     self.name=name
#
#     def greet(self,a):
#         print("welcome",a)
#
#     def greet1(self):
#         print(f"welcome {self.name}",)
#
# obj=Xyz()
# obj.greet("abhi")

# class Employee:
#     company = "OpenAI"
#
#
#     def get_company(self):
#         print(Employee.company)
#
# Employee().get_company() # Output: OpenAI
# obj=Employee()
# obj.get_company()
class Cal:
    counter = 0

    # def __init__(cls):
    #     cls.counter=0

    @classmethod
    def increase(cls,n):
        cls.counter+=n


    def increase1(cls, n):
        cls.counter += n

    def display(a):
        return a.counter

# obj1=Cal()
# obj2=Cal()
# print(obj1.increase1(2))
# print(obj2.increase1(5))
# print(obj2.display())

# class Parent:
#
#     def __init__(self,num):
#         self.num=num
#
#     def get_num(self):
#         return self.num
#
# class Child(Parent):
#
#
#
#     def get_val(self):
#         return self.num
#
# son=Child(10)
# print(son.get_val())

class Parent:
    def __init__(self, num1):
        self.num1 = 20

class Child(Parent):
    def __init__(self,name):
        self.num1=3
        self.name = name       # Extend it with new logic
#
# c = Child( "Alice")
# print(c.num1)   # From Parent
# print(c.name)  # From Child

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # ✅ still call parent greet
        print("Hello from Child")

# c = Child()
# c.greet()

class Parent:
    nam="abhi"
    def __init__(self,name):
        self.name =name

class Child(Parent):
    def __init__(self,name ,age):
        super().__init__(name)
        self.age = age


# c = Child("xyz",12)
# print(c.name)  # Output: Alice
# print(c.age)   # Output: 12

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        pass

    def area1(self):
        return 3.14*self.radius*self.radius

class Square(Shape):

    def __init__(self,length):
        self.length=length

    def area2(self):
        return self.length*self.length

# obj1=Square(10)
# print(obj1.area2())

# obj1=Circle(5)
# print(obj1.are())

# '''Duck typing'''
#
# class Human:
#     def speak(self):
#         print("hello")
#
# class Dog:
#     def speak(self):
#         print("Bark")
#
# def call_speak(entity):
#     return entity().speak()
#
# call_speak(Human)
# call_speak(Dog)