# ques1:
# def difference(n):
#     if n>17:
#         return 2* abs(n-17)
#     else:
#         return abs(n-17)
    
# number = int(input("Enter A Number:"))
# result = difference(number)
# print("Result:",result)

# ques2:
# def testnumber(n):
#     return (100<= n <= 1000) or (n == 2000)
# num = int(input("Enter a Number:"))
# if testnumber(num):
#     print("The Number Is Between 100 And 1000 or equals to 2000")
# else:
#     print("The Number Is Not Within The Range")

# ques3:
# def reversestring(s):
#     return s[::-1]
# text = input("Enter a String:")
# reversetext = reversestring(text)
# print("Reversed String:",reversetext)

# ques4:
# def countcase(s):
#     uppercount = 0
#     lowercount = 0

#     for char in s:
#         if char.isupper():
#             uppercount +=1
#         elif char.islower():
#             lowercount +=1

#     print("Number of uppercase letters:", uppercount)  
#     print("Number of lowercase letters:", lowercount)   

# text= input("Enter a String:")
# countcase(text)

# ques5:
# def uniquelist(lst):
#     return list(set(lst))

# numbers = input("Enter numbers separated by space:").split()
# numbers = [int(num)for num in numbers]

# result = uniquelist(numbers)
# print("List With Distinct Elements:",result)

# ques6:
# def evennumbers(lst):
#     return[num for num in lst if num%2 ==0]

# numbers = [1,2,3,4,5,6,7,8,9]
# result = evennumbers(numbers)

# print("Even Numbers:",result)

# ques7:
# def robot():
#     def move():
#         print("The robot is moving")
#     move()

# robot()

# ques8:
# def student(name, age, course):
#     return f"Name: {name}, Age: {age}, Course: {course}"

# # Display argument names using function attributes
# print("Argument names:", student.__code__.co_varnames[:student.__code__.co_argcount])

# # Example call
# print(student("Yuvraj", 19, "RAI"))

#ques9:
# def move_robot(x, y, direction):
#     if direction == "up":
#         return (x, y+1)
#     elif direction == "down":
#         return (x, y-1)
#     elif direction == "left":
#         return (x-1, y)
#     elif direction == "right":
#         return (x+1, y)
#     else:
#         return (x, y)  # no change if invalid

# # Example
# print(move_robot(0, 0, "up"))   # → (0,1)
# print(move_robot(2, 3, "left")) # → (1,3)

#ques10:
# def classify_temperature(temp):
#     if temp < 15:
#         return "Cold"
#     elif 15 <= temp <= 30:
#         return "Moderate"
#     else:
#         return "Hot"

# # Example
# print(classify_temperature(10))
# print(classify_temperature(25))
# print(classify_temperature(35))

#ques11:
# def is_goal_reached(path):
#     x, y = 0, 0
#     for move in path:
#         if move == "up":
#             y += 1
#         elif move == "down":
#             y -= 1
#         elif move == "left":
#             x -= 1
#         elif move == "right":
#             x += 1
#     return (x, y) == (2, 0)

# print(is_goal_reached(["up", "right", "right", "down"]))


