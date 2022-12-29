"""3"""
# num_list=[12,20,33,46,55]
# print("The element in the list are:",num_list)
# print("Divisible by 5")
# l=[]
# for num in num_list:
#   if num%5==0:
#     l.append(num)
# print(l)

"""(4) Print the following pattern
        1 
        2 2 
        3 3 3
        4 4 4 4
        5 5 5 5 5"""
# for i in range(6):
#   for j in range(i):
#     print(i,end=" ")
#   print()


"""(5) Write a program to check if the given number is a palindrome or not"""

num=input("Enter a number to check palindrome:")
len=len(num)
n=[]
l=[]
for i in range(len):#5
  if i<=len/2:#2
    l.append(num[i-1])
  elif len%2!=0 and i>((len/2)+1):#4
    n.append(num[i-1])
  elif len%2==0 and i>=((len/2)+1):#3
    n.append(num[i-1])

for i in n:
  if(i!=l.pop()):
    print("Not palindrome")
    break
  else:
    print("Palindrome")

  
"""Class"""

# class Person:
#   def __init__(self,name,age):
#     self.name = name
#     self.age= age
#   #Adding str function
#   def __str__(self):
#     # return f"{self.name}({self.age})"
#     return "newobj"
#   #Adding another function
#   def myfunction(self):
#     print("The given name is",self.name)

# p1=Person("Mansij",21)
# print(p1.name)
# print(p1.age)
# print(p1)
# p1.myfunction()


"""Calculate Area using Class"""

# #Create a class Room
# class Room:
#   length=0.0
#   breadth=0.0
#   #method to calculate area
#   def calculate_area(self):
#     print("Area of Room=",self.length*self.breadth)

# #Create object of Room Class
# study_room=Room()

# #Assign Value to all the properties
# study_room.length=3
# study_room.breadth=9

# #access method inside class
# study_room.calculate_area()


"""Inheritance"""

# class Animal:
#   name=""
#   def eat(self):
#     print("Tiger eat Sheep")

# #inherit from Animal
# class Dog(Animal):
#   #new method in subclass
#   def display(self):
#     #access name attribute of superclass using self
#     print("My name is",self.name)

#   #override eat() method
#   def eat(self):
#     #call the eat() method of the superclass using super()
#     super().eat()

#     print("I like to eat bones")

# #create object of subclass
# labrador=Dog()

# #access superclass attribute and method
# labrador.name="Rocky"
# labrador.eat()

# #call subclass method
# labrador.display()