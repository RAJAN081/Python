"""variables"""

# sher = "harsh bhaiya"

# SheryiansSchool = "students" #pascal case

# sheryiansSchool = "students" #camel case

# sheryians_school = "students" #snake case




"""data types"""

# a = -34

# b = 56.8
# c = 12/3

# v = 34j

# print(type(v))



# st = '1231243235 dsagaiogiaeb !@#$%^&*'

# print(type(st))

# b = True

# t = False

# print(type(b))


"""Strings and basic Python operations"""

# Example of a string and slicing
# a = "SHER CODER"
# print(a[::])  # prints the whole string. [::] means start to end with step 1

# Example of integer division
# a = 12 
# print(12/3)  # division, result is 4.0 (float)

# Using f-strings for formatted output
# name = "akarsh"
# age = "23"
# print(f"My name is {name} and my age is {age}")

# Taking input from user (input returns string by default)
# age = int(input("Hello, what is your age: "))
# print(age)

# Basic arithmetic operations
# a = 5
# b = 32
# print(a + b)   # addition
# print(b - a)   # subtraction
# print(a * b)   # multiplication
# print(b//a)    # integer division
# print(b/a)     # float division
# print(5**100)  # exponentiation
# print(32%5)    # modulus (remainder)

# Operator precedence example
# print(12+4/2)  # division happens first, then addition

# Assignment operators and compound assignment
# a = 20
# a += 20  # a = a + 20
# a += 40
# a += 60
# a -= 10  # a = a - 10
# a *= 2   # a = a * 2
# a /= 5   # a = a / 5
# a //= 3  # a = a // 3
# a **= 2  # a = a ** 2
# print(a)

# Comparison operators
# a = 12.1
# b = 12
# print(a == b)   # equality check
# print(a != b)   # inequality check
# print(a > b)    # greater than
# print(45 < 67)  # less than
# print(23 >= 23) # greater than or equal
# print(45 <= 45) # less than or equal

# ASCII values and string comparison
# print(ord("A"))  # prints ASCII value of A = 65
# print(ord("B"))  # prints ASCII value of B = 66
# print("ABC" > "ACD")  # string comparison (lexicographic)
# print("A" > 34)  # will give error: cannot compare str and int

# Logical operators
# print(12 > 20 and 123 > 100 and 34 == 34 and 45 < 90)  # AND operator
# print(12 != 12 or 23 == 45 or 67 == 56 or 10 > 5)       # OR operator
# print(not 12 == 12)  # NOT operator

# IF-ELSE examples
# a = 6
# if a > 10:
#     print("I will do task A")
# else:
#     print("I will do task B")

# Example using input and multiple conditions (if-elif-else)
# money = int(input("Please provide me the money: "))
# if money == 10:
#     print("I will have a choco bar icecream")
# elif money == 20:
#     print("I will have a mangodolly")
# elif money == 30:
#     print("I will have a frosty")
# else:
#     print("I will have a cone")

# Compare two numbers
# num1 = int(input("Please tell your first number: "))
# num2 = int(input("Please tell your second number: "))
# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")
# else:
#     print("Both numbers are same")

# Gender check example
# gen = input("Please tell your gender as character (M or F): ")
# if gen == 'M' or gen == 'm':
#     print("Good morning SIR")
# elif gen == 'F' or gen == 'f':
#     print("Good morning MAM")
# else:
#     print("Unidentified gender")

# Even or Odd check
# num = int(input("Please tell your number: "))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# Voting eligibility check
# name = input("Please tell your name: ")
# age = int(input("Now tell your age: "))
# if age >= 18:
#     print(f"Hello {name}, you are a valid voter")
# else:
#     print(f"Hello {name}, you are not a valid voter")

# Leap year check
# year = int(input("Tell your year: "))
# if year % 100 == 0 and year % 400 == 0:
#     print("It's a leap year")
# elif year % 100 != 0 and year % 4 == 0:
#     print("It's a leap year")
# else:
#     print("It's a normal year")

# Temperature conditions
# t = int(input("Please tell the temperature: "))
# if t < 0:
#     print("Freezing cold")
# elif t >= 0 and t < 10:
#     print("Very cold")
# elif t >= 10 and t < 20:
#     print("Cold")
# elif t >= 20 and t < 30:
#     print("Pleasant")
# elif t >= 30 and t < 40:
#     print("Hot")
# else:
#     print("Temperature is very hot")

# Basic print
# print("Hello world")



# -----------------------------
# FOR LOOP EXAMPLES
# -----------------------------

# Print multiplication table of a number
# n = int(input("Which table you want? "))
# for i in range(n, (n*10)+1, n):
#     print(i)

# Working with strings
# a = "SHERYIANS TEACHES INDUSTRY THINGS"
# print(len(a))  # prints the length of the string

# Iterate through each character using index
# for i in range(len(a)):
#     print(a[i])

# Iterate through each character directly
# a = "SHERYIANS IS COOL"
# for i in a:
#     print(i)

# For loop with break
# for i in range(1, 21):
#     if i == 56:
#         print("Break statement is executed")
#         break  # exit the loop immediately
#     print(i)
# else:
#     print("Break statement is not executed")  # executes only if loop wasn't broken

# Print "hello world" n times
# n = int(input("Please tell your number: "))
# for i in range(n):
#     print("hello world")

# Print numbers from 1 to n
# n = int(input("Please tell your number: "))
# for i in range(1, n+1):
#     print(i)

# Print numbers from n down to 1
# n = int(input("Please tell your number: "))
# for i in range(n, 0, -1):
#     print(i)

# Print multiplication table in formatted way
# n = int(input("Which table you want: "))
# for i in range(1, 11):
#     print(f"{n} * {i} = {n*i}")

# Sum of first n numbers
# n = int(input("Please tell your number: "))
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i
# print(f"Your sum is {sum}")

# Factorial of a number
# n = int(input("Please tell your number: "))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(f"Your factorial is {fact}")

# Sum of even and odd numbers up to n
# n = int(input("Tell your number: "))
# even = 0
# odd = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
# print(f"Your even and odd sum are {even}, {odd}")

# Print all factors of a number
# n = int(input("Which number's factors you want: "))
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)

# Check if a number is perfect
# n = int(input("Check if your number is perfect: "))
# sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum += i
# if sum == n:
#     print("Your number is perfect")
# else:
#     print("Not a perfect number")

# Check if a number is prime
# n = int(input("Check if your number is prime: "))
# count = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1
# if count == 2:
#     print("Your number is prime")
# else:
#     print("Your number is not prime")

# Reverse a string
# a = "SHERYIANS"
# b = ""
# for i in range(len(a)-1, -1, -1):
#     b += a[i]
# print(b)

# Check if a string is palindrome
# a = "NAMAN"
# b = ""
# for i in range(len(a)-1, -1, -1):
#     b += a[i]
# if b == a:
#     print("Your string is palindrome")
# else:
#     print("It's not a palindrome")

# Count characters, digits, and special characters in a string
# a = "sdfsogn12413@#$%^&U"
# char = 0
# dig = 0
# spchr = 0
# for i in a:
#     if i.isdigit():
#         dig += 1
#     elif i.isalpha():
#         char += 1
#     else:
#         spchr += 1
# print(f"Your digits are {dig}\nYour alphabets are {char}\nYour special characters are {spchr}")

# View all string methods
# print(dir(str))

# -----------------------------
# WHILE LOOP EXAMPLES
# -----------------------------

# Print numbers from 1 to 30 using while loop
# a = 1
# while a <= 30:
#     print(a)
#     a += 1

# Reverse a number
# a = int(input("Tell your number: "))
# rev = 0
# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10
# print(rev)

# Check if a number is palindrome
# a = int(input("Tell your number: "))
# copy = a
# rev = 0
# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10
# if copy == rev:
#     print("Palindromic number")
# else:
#     print("Not a palindromic number")


# -----------------------------
# RANDOM NUMBER GUESSING GAME
# -----------------------------
# import random
# num = random.randint(1,10)  # Generate random number between 1 and 10
# tries = 0

# while True:
#     guess = int(input("Please guess a number between 1 and 10: "))
#     tries += 1
#     if num == guess:
#         print(f"You are right! You guessed the number in {tries} tries")
#         break
#     elif num < guess:
#         print("Go a little lower")
#     elif num > guess:
#         print("Go a little higher")
# print(12)  # Just a print statement outside loop

# -----------------------------
# FUNCTIONS
# -----------------------------
# Simple function without arguments
# def hello():
#     print("This is a hello function")

# hello()  # Call the function

# Function with parameters
# def hello(name, age):
#     print(f"Your name is {name} and your age is {age}")

# hello(age=22, name="akarsh")  # Calling with named arguments

# Function to check palindrome
# def palindrome(st):
#     rev = ""
#     for i in range(len(st)-1, -1, -1):
#         rev += st[i]
#     if rev == st:
#         print(f"{st} is a palindrome")
#     else:
#         print(f"{st} is not a palindrome")

# palindrome("NAMAN")
# palindrome("CURSOR")

# Function with return value
# def hello():
#     return "Hello, how are you"

# print(hello())

# -----------------------------
# LISTS
# -----------------------------
# a = [12,13,14,15,16,34.5]

# # Iterating using index
# for i in range(len(a)):
#     print(a[i])

# # Iterating directly over elements
# for i in a:
#     print(i)

# Separate positive and negative elements
# l = [-45,67,12,-68,-69,34]
# print("Positive elements are:")
# for i in l:
#     if i >= 0:
#         print(i)
# print("Negative elements are:")
# for i in l:
#     if i < 0:
#         print(i)

# Average of list
# l = [12,435,67,89,23,25,69]
# sum = 0
# for i in l:
#     sum += i
# print(sum / len(l))  # average

# Find largest element and its index
# l = [12,567,43,235,347,568,45,7]
# largest = l[0]
# index = 0
# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i
# print(f"Largest number is {largest} at index {index}")

# Find largest and second largest
# l = [12,16,13,19,17]
# largest = l[0]
# sec_largest = l[0]
# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i
# print(f"Second largest: {sec_largest}, Largest: {largest}")

# Check if list is sorted
# a = [12,13,18,15,16]
# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("Your list is not sorted")
#         break
# else:
#     print("Your list is sorted")

# -----------------------------
# TUPLES
# -----------------------------
# a = (1,2,3,4,5,5,5.5,print(),"hello")  # tuples can store multiple types
# count = a.count(5)  # count occurrences of 5
# print(count)

# a = (1,)  # single-element tuple
# print(type(a))  # <class 'tuple'>

# -----------------------------
# SETS
# -----------------------------
# a = {1,8,9,"hello",2,3,4,5}  # unordered, unique elements
# for i in a:
#     print(i)  # iteration order may vary

# a = {8,1,2,3,4}
# a.clear()  # remove all elements
# print(a)   # prints set()

# Set difference
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# b -= a  # remove elements of a from b
# print(b)

# -----------------------------
# DICTIONARIES
# -----------------------------
# d = {10:100, 20:200, 30:300, 40:400}
# d[10] = 100  # update
# d[50] = 500  # create
# del d[30]    # delete
# print(d)

# Access dictionary items
# d = {10:100,20:200,30:300,40:400}
# print(d.items())  # returns list of key-value tuples

# Merge two dictionaries
# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}
# for i in d2:
#     d1[i] = d2[i]  # add/update keys
# print(d1)

# Sum of dictionary values
# d1 = {10:100,20:200,40:300}
# sum = 0
# for i in d1:
#     sum += d1[i]
# print(sum)

# Count occurrences of elements in a list using dictionary
# a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]
# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

# Merge dictionaries and sum values for common keys
# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}
# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]  # sum values if key exists
#     else:
#         d1[i] = d2[i]   # create new key
# print(d1)



# -----------------------------
# RANDOM NUMBER GUESSING GAME
# -----------------------------
# import random
# num = random.randint(1,10)  # Generate random number between 1 and 10
# tries = 0

# while True:
#     guess = int(input("Please guess a number between 1 and 10: "))
#     tries += 1
#     if num == guess:
#         print(f"You are right! You guessed the number in {tries} tries")
#         break
#     elif num < guess:
#         print("Go a little lower")
#     elif num > guess:
#         print("Go a little higher")
# print(12)  # Just a print statement outside loop

# -----------------------------
# FUNCTIONS
# -----------------------------
# Simple function without arguments
# def hello():
#     print("This is a hello function")

# hello()  # Call the function

# Function with parameters
# def hello(name, age):
#     print(f"Your name is {name} and your age is {age}")

# hello(age=22, name="akarsh")  # Calling with named arguments

# Function to check palindrome
# def palindrome(st):
#     rev = ""
#     for i in range(len(st)-1, -1, -1):
#         rev += st[i]
#     if rev == st:
#         print(f"{st} is a palindrome")
#     else:
#         print(f"{st} is not a palindrome")

# palindrome("NAMAN")
# palindrome("CURSOR")

# Function with return value
# def hello():
#     return "Hello, how are you"

# print(hello())

# -----------------------------
# LISTS
# -----------------------------
# a = [12,13,14,15,16,34.5]

# # Iterating using index
# for i in range(len(a)):
#     print(a[i])

# # Iterating directly over elements
# for i in a:
#     print(i)

# Separate positive and negative elements
# l = [-45,67,12,-68,-69,34]
# print("Positive elements are:")
# for i in l:
#     if i >= 0:
#         print(i)
# print("Negative elements are:")
# for i in l:
#     if i < 0:
#         print(i)

# Average of list
# l = [12,435,67,89,23,25,69]
# sum = 0
# for i in l:
#     sum += i
# print(sum / len(l))  # average

# Find largest element and its index
# l = [12,567,43,235,347,568,45,7]
# largest = l[0]
# index = 0
# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i
# print(f"Largest number is {largest} at index {index}")

# Find largest and second largest
# l = [12,16,13,19,17]
# largest = l[0]
# sec_largest = l[0]
# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i
# print(f"Second largest: {sec_largest}, Largest: {largest}")

# Check if list is sorted
# a = [12,13,18,15,16]
# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("Your list is not sorted")
#         break
# else:
#     print("Your list is sorted")

# -----------------------------
# TUPLES
# -----------------------------
# a = (1,2,3,4,5,5,5.5,print(),"hello")  # tuples can store multiple types
# count = a.count(5)  # count occurrences of 5
# print(count)

# a = (1,)  # single-element tuple
# print(type(a))  # <class 'tuple'>

# -----------------------------
# SETS
# -----------------------------
# a = {1,8,9,"hello",2,3,4,5}  # unordered, unique elements
# for i in a:
#     print(i)  # iteration order may vary

# a = {8,1,2,3,4}
# a.clear()  # remove all elements
# print(a)   # prints set()

# Set difference
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# b -= a  # remove elements of a from b
# print(b)

# -----------------------------
# DICTIONARIES
# -----------------------------
# d = {10:100, 20:200, 30:300, 40:400}
# d[10] = 100  # update
# d[50] = 500  # create
# del d[30]    # delete
# print(d)

# Access dictionary items
# d = {10:100,20:200,30:300,40:400}
# print(d.items())  # returns list of key-value tuples

# Merge two dictionaries
# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}
# for i in d2:
#     d1[i] = d2[i]  # add/update keys
# print(d1)

# Sum of dictionary values
# d1 = {10:100,20:200,40:300}
# sum = 0
# for i in d1:
#     sum += d1[i]
# print(sum)

# Count occurrences of elements in a list using dictionary
# a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]
# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

# Merge dictionaries and sum values for common keys
# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}
# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]  # sum values if key exists
#     else:
#         d1[i] = d2[i]   # create new key
# print(d1)



# -----------------------------
# ABSTRACT CLASSES
# -----------------------------
# from abc import ABC, abstractmethod

# Abstract base class
# class Abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass  # must be implemented in child class
    
#     @abstractmethod
#     def area(self):
#         pass  # must be implemented in child class

# class Square(Abstract):
#     def __init__(self, side):
#         self.side = side
#     def perimeter(self):
#         print("I have created perimeter for square")
#     def area(self):
#         print("I have created area for square")

# class Circle(Abstract):
#     def __init__(self, radius):
#         self.radius = radius
#     def perimeter(self):
#         print("I have created perimeter for circle")
#     def area(self):
#         print("I have created area for circle")

# obj = Circle(7)
# obj2 = Square(12)

# -----------------------------
# OPERATOR OVERLOADING
# -----------------------------
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"Hello, your name is {self.name}"
#     def __add__(self, other):
#         total_age = self.age + sum(o.age for o in other)
#         return f"Sum of ages: {total_age}"

# obj = Animal("lion", 12)
# obj2 = Animal("dolphin", 14)
# obj3 = Animal("tiger", 34)
# print(obj + (obj2, obj3))

# -----------------------------
# PROPERTY DECORATOR
# -----------------------------
# class Animal:
#     @property
#     def show(self):
#         print("Hello, how are you")

# obj = Animal()
# obj.show  # accessed like attribute, not function

# -----------------------------
# DECORATORS
# -----------------------------
# def decorate(func):
#     def wrapper(*args, **kwargs):
#         print("Addition to your numbers is: ")
#         func(*args, **kwargs)
#         print("Thank you! I hope you liked it")
#     return wrapper

# @decorate
# def addition(a, b):
#     print(f"Your total is {a + b}")

# addition(12, 67)

# -----------------------------
# VARIABLE KEYWORD ARGUMENTS
# -----------------------------
# def information(**kwargs):
#     print("Your information is:\n")
#     for key in kwargs:
#         print(f"{key} : {kwargs[key]}")

# information(name="Akarsh", age=23, designation="AI/ML")

# -----------------------------
# DICTIONARY COMPREHENSIONS
# -----------------------------
# l = {i: i**2 for i in range(1, 10)}
# print(l)

# -----------------------------
# MAP FUNCTION
# -----------------------------
# a = [1,2,3,4,5]
# def double(x):
#     return x * 2
# result = map(double, a)
# print(list(result))

# -----------------------------
# PRINT PATTERNS
# -----------------------------
# n = int(input("How many rows you want: "))
# for i in range(1, n+1):
#     for j in range(i):
#         print("* ", end="")
#     print()

# n = int(input("Tell how many rows you want: "))
# for i in range(1, n+1):
#     for j in range(n-i):
#         print("  ", end="")  # spaces
#     for k in range(i):
#         print("* ", end="")
#     print()

# -----------------------------
# STRONG NUMBER CHECK
# -----------------------------
# a = 1234
# copy = a
# total = 0
# while a > 0:
#     digit = a % 10
#     fact = 1
#     for i in range(1, digit+1):
#         fact *= i
#     total += fact
#     a //= 10
# if total == copy:
#     print("This is a strong number")
# else:
#     print("Not a strong number")

# -----------------------------
# PRIME NUMBERS
# -----------------------------
# for j in range(2, 21):
#     a = j
#     for i in range(2, (a//2)+1):
#         if a % i == 0:
#             break
#     else:
#         print(a)

# -----------------------------
# MOST FREQUENT ELEMENT
# -----------------------------
# a = [1,1,1,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,5,5,5]
# count_dict = {}
# for i in a:
#     if i in count_dict:
#         count_dict[i] += 1
#     else:
#         count_dict[i] = 1
# max_count = max(count_dict.values())
# for key in count_dict:
#     if count_dict[key] == max_count:
#         print(f"{key} occurred {max_count} times (largest occurrence)")
#         break
