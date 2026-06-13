# a=90
# b=95
# c=99
# total=a+b+c
# average=total/3
# percentage=total/300*100
# print("total=",total)
# print("average=",average)
# print("percentage=",percentage)

# a=45
# b=34
# print(a,b)
# x=input("enter a number")
# print(x)
# print(type(x))

# x=5
# print(type(x))
# x=5.4
# print(type(x))
# x="hello"
# print(type(x))
# x=True
# print(type(x))
# x=None
# print(type(x))

# x=input()
# print(type(x))

# x=int(input("enter a number"))
# print(type(x))
# x=float(input(5))
# print(type(x))

# name=input("enter the name")
# x=float(input("enter the mark in physics"))
# y=float(input("enter the mark in maths"))
# z=float(input("enter the mark in science"))
# total=x+y+z
# average=total/3
# percentage=total/300*100
# print("total=",total)
# print("average=",average)
# print("percentage=",percentage)

# age=int(input("enter your age"))
# if(age>=18):
#   print("eligible")
# else:
#  print("not eligible")



# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# c=int(input("enter a number:"))
# print(a,b,c)
# if a>b and a>c:
#     print("a is the largest")
# elif b>a and b>c:
#     print("b is the largest")
# elif c>a and c>b:
#     print("c is the largest")
# else:
#     print("all are equal")

# x=float(input("enter a number"))
# print(x)
# if x>0 and x<=8:
#  print("kids")
# elif x>8 and x<=18:
#   print("junior")
# elif x>13 and x<=19:
#   print("teenager")
# elif x>20 and x<=50:
#   print("adult")
# else:
#   print("senior citizen")

# for i in range(1,11):
#     print(i)  

# for i in range(1,101):
#     if i % 2==0:
#         print(i)

# i=1
# while i <= 10:
#  print(i)
#  i += 1

# i=1
# while i<=10:
#      if i % 2==0:
#         print(i)
#      i += 1

# def add (a,b):
#     return a + b
# result = add(6,5)
# print("the sum is:", result)

# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit
# celsius_val = 25
# fahrenheit_val = celsius_to_fahrenheit(celsius_val)
# print(f"{celsius_val} degreecelsius is equal to {fahrenheit_val} degreefahrenheit")

# def sum_of_prime(limit):
#     prime_sum = 0
#     for num in range(2, limit + 1):
#         if all(num % i !=0 for i in range(2, int(num**0.5) + 1)):
#             prime_sum += num
#     return prime_sum
# print(f"the sum is:{sum_of_prime(100)}")


# x=lambda a,b: a+b
# print(x(2,3))

# x=lambda a: a**0.5
# print(x(4))

# x=lambda a: " even " if a%2==0 else "odd"
# print(x(4))

# class Student:
#  def __init__(self, name,age,marks):
#        self.name=name
#        self.age=age
#        self.marks=marks
# s1= Student("john",21,84)
# s2= Student("james",22,94)
# print(s1.name,s1.age,s1.marks)
# print(s2.name,s2.age,s2.marks)


# class Student:
#  def __init__(self, name,age,marks):
#        self.name=name
#        self.age=age
#        self.marks=marks
#  def info(self):
#     return f"my name is {self.name} and my mark is {self.marks} "
# s1= Student("john",21,84)
# s2= Student("james",22,94)
# print(s1.name,s1.age,s1.marks)
# print(s2.name,s2.age,s2.marks)
# print(s1.info())
# print(s2.info())
