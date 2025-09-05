#Ques1:
L = [11,12,13,14]
L.append(50)
L.append(60)
print("List after adding 50 and 60:",L)

L.remove(11)
L.remove(13)
print("List after removing 11 and 13:",L)

L.sort()
print("List after sort in ascending:",L)

L.sort(reverse=True)
print("List after sorting in descending:",L)

if 13 in L:
    print("13 Is Present")
else:
    print("13 Is Not Present")

print("Number of elements in L:",len(L))

print("sum of elements in L:",sum(L))

odd_sum = sum(x for x in L if x % 2 != 0)
print(" Sum of odd numbers:", odd_sum)

even_sum = sum(x for x in L if x % 2 == 0)
print(" Sum of even numbers:", even_sum)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
prime_sum = sum(x for x in L if is_prime(x))
print(" Sum of prime numbers:", prime_sum)

L.clear()
print("After clearing:", L)

del L
print("L is deleted.")


#ques2:
list1 = [10, 20, 30, 40]

sum = 0
for i in list1:
    sum = sum + i
print(sum)

# Ques3:
multiply=1
for i in list1:
    multiply = multiply * i

print(multiply)

#Ques4:

 array_3d = [[['*' for k in range(6)] for j in range(4)] for i in range(3)]
 print(array_3d)


#Ques5:
D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
D[8] = 8.8
print("Dict after adding:",D)

D.pop(2)
print("Dict after removing:",D)

if 6 in D:
    print("It Is Present")
else:
    print("It Is Not Present")

print("Number of Elements in D:",len(D))

total = 0
for value in D.values():
    total += value
print("Sum of all values:", total)

D[3] = 7
print("D after changing value:",D)

D.clear()
print("After clearing the D:",D)


#Ques6:
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

S1.add(55)
S1.add(66)
print("After adding 55 and 66 in S1:", S1)

S1.remove(10)
S1.remove(30)
print("After Removing10 and 30:",S1)

if 40 in S1:
    print("40 is Present")
else:
    print("40 Is Not There")

print("Union of S1 and S2:", S1.union(S2))

print("intersection of S1 and S2:", S1.intersection(S2))

print("difference of S1 and S2:", S1.difference(S2))


# Ques7:
import random
import string

for i in range(100):
    n = random.randint(6, 8)
    s = ""
    for j in range(n):
        s += random.choice(string.ascii_letters)
    print(s)


for num in range(600, 801):
    c = 0
    for i in range(1, num + 1):
        if num % i == 0:
            c += 1
    if c == 2:
        print(num)

for i in range(100, 1001):
    if i % 7 == 0 and i % 9 == 0:
        print(i)


# Ques8:
exam_st_date = (11, 12, 2014)
print("The examination will start from: %i / %i / %i" % exam_st_date)


# Ques9:
numbers = [10, 23, 45, 67, 50, 82, 95]

 for n in numbers:
     if n % 5 == 0:
         print(n)


# Ques10:
num = int(input("Enter a number: "))

is_even = (num % 2 == 0)  # Boolean variable

if is_even:
    print(num, "is Even")
else:
    print(num, "is Odd")


# Ques11:
text = "Emma is a good girl. Emma likes coding. Emma is smart."

count = 0
for i in range(len(text) - 3):  # 3 = len("Emma") - 1
    if text[i:i+4] == "Emma":
        count += 1

print("The substring 'Emma' appears", count, "times.")


# Ques12:
list1 = [10, 21, 4, 45, 66, 93]
list2 = [11, 20, 32, 97, 40, 55]

new_list = []

# Odd numbers from list1
for num in list1:
    if num % 2 != 0:
        new_list.append(num)

# Even numbers from list2
for num in list2:
    if num % 2 == 0:
        new_list.append(num)

print("New list:", new_list)

Ques13:
positions = [(2,3), (4,5), (6,7), (7,8)]
even_positions = [pos for pos in positions if pos[0] % 2 == 0]
print("Positions with even x-coordinate:", even_positions)

# Ques14:
sensor_data = {1: 2.3, 2: 4.5, 3: 1.8, 4: 3.6}
high_sensors = [sid for sid, reading in sensor_data.items() if reading > 3.0]
print("Sensor IDs with reading > 3.0:", high_sensors)

Ques15:
commands_received = {"MOVE", "TURN_LEFT", "TURN_RIGHT", "STOP"}
commands_executed = {"MOVE", "TURN_LEFT", "STOP"}

not_executed = commands_received - commands_executed
print("Commands not executed:", not_executed)

