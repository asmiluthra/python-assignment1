#Ques1:
# print("""Twinkle, twinkle, little star,
#     How I wonder what you are!
#         Up above the world so high,
#         Like a diamond in the sky.
# Twinkle, twinkle, little star,
#     How I wonder what you are""")

#Ques2:
# first = input("Enter your first name: ")
# last = input("Enter your last name: ")
# print(last + " " + first)

#Ques3:
# import math
# r = float(input("Enter radius of circle: "))
# area = math.pi * r * r
# print("Area of Circle:", area)

#Ques4:
# color_list = ["Red","Green","White","Black"]
# print("First color:", color_list[0])
# print("Last color:", color_list[-1])

#Ques5:
# n = int(input("Enter a number: "))
# result = n + int(str(n)*2) + int(str(n)*3)
# print("Result:", result)

#Ques6:
# data = input("Enter comma-separated numbers: ")
# lst = data.split(",")
# tpl = tuple(lst)
# print("List:", lst)
# print("Tuple:", tpl)

#Ques7:
# c = float(input("Enter temperature in Celsius: "))
# f = (c * 9/5) + 32
# print("Temperature in Fahrenheit:", f)

#Ques8:
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# a, b = b+1, a   # swapping + increment a variable
# print("After swapping: a =", a, ", b =", b)

#Ques9:
# n = int(input("Enter a number: "))
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

#Ques10:
# year = int(input("Enter year: "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

#Ques11:
# import math
# x1, y1 = map(float, input("Enter first point (x1 y1): ").split())
# x2, y2 = map(float, input("Enter second point (x2 y2): ").split())
# dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
# print("Euclidean Distance:", dist)

#Ques12:
# a, b, c = map(int, input("Enter three angles: ").split())
# if a + b + c == 180 and a>0 and b>0 and c>0:
#     print("Valid Triangle")
# else:
#     print("Not a Triangle")

#Ques13:
# p = float(input("Enter principal: "))
# r = float(input("Enter rate (%): "))
# t = float(input("Enter time (years): "))
# ci = p * (pow((1 + r/100), t)) - p
# print("Compound Interest:", ci)

#Ques14:
# n = int(input("Enter a number: "))
# if n > 1:
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not Prime")

#Ques15:
# n = int(input("Enter N: "))
# sum_sq = sum(i*i for i in range(1, n+1))
# print("Sum of squares:", sum_sq)
