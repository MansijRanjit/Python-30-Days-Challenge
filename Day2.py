"""Question no2 : Write a program to display on range of 10 the following:
Current no is: 1 and previous number is: 0.The sum of Number is:1
Current no is: 2 and previous number is: 1.The sum of Number is:3
Current no is: 3 and previous number is: 2.The sum of Number is:5
Current no is: 4 and previous number is: 3.The sum of Number is:7
Current no is: 5 and previous number is: 4.The sum of Number is:9
Current no is: 6 and previous number is: 5.The sum of Number is:11
Current no is: 7 and previous number is: 6.The sum of Number is:13
Current no is: 8 and previous number is: 7.The sum of Number is:15
Current no is: 9 and previous number is: 8.The sum of Number is:17
Current no is: 10 and previous number is: 9.The sum of Number is:19
"""
# for i in range(1,11):
#    first=i
#    second=i-1
#    sum= first+second
#    print("Current no is: ", first, " and previous number is: ",second,".The sum of Number is:" ,sum)


"""Function"""

# def function1(a,b):
#   d=a+b
#   print(d)
#   return
# function1(5,6)

# def CalcSquare(a):
#   square=a*a
#   print("\nSquare:",square)
# CalcSquare(5)

# def get_Square(num):
#   return num*num
# for i in [1,3,4]:
#   print("Square of",i, "is",get_Square(i))

"""Arbitrary Arguments (*args)"""

# def sum(*numbers):
#   result=0
#   for num in numbers:
#     result=result+num
#   print("\n",result)

# sum(1,2,3)
# sum(4,9)
# sum(9,9,9,9)

# def func(*fruits):
#   print("The Selected Fruit is:",fruits[1])

# func("Mango","Örange","Banana")

"""Arbitrary Keyword Arguments (**kwargs)"""

# def intro(**data):
#   print("\nData type of argument:",type(data))
#   for key,value in data.items():
#     print("{} is {}".format(key,value))

# intro(Name="Supermansij",Address="Kalanki",Phone=9840253456,Email="mansijranjit@gmail.com")


"""Python Recursion"""
# def factorial(x):
#   if x==1:
#     return 1
#   else:
#     return(x*factorial(x-1))

# print(factorial(4))


