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


"""strings"""

# a = "SHER CODER"


# print(a[::])

# a = 12 

# print(12/3)

# name = "akarsh"
# age = "23"

# print(f"my name is {name} and my age is {age}")

# age = int(input("hello what is your age"))

# print(age)

# a = 5
# b = 32


# print(a + b)
# print(b - a)
# print(a * b)
# print(b//a)
# print(b/a)
# print(5**100)
# print(32%5)


# print(12+4/2)


#assignment operators 

# a = 23

#compound assignmet operations

# a = 20

# a += 20
# a += 40
# a += 60
# a-=
# a*=
# a/=
# a//=
# a**=

# print(a)

# a = 12.1
# b = 12 

# print(a == b)

# print(a != b)

# print(a > b)
# print(45 < 67)
# print(23 >= 23)
# print(45 <= 45)


# print(ord("A"))
# print(ord("B"))

# print("ABC" > "ACD")

# print("A" > 34)

# print(12 >20 and 123 > 100 and 34 == 34 and 45 < 90)

# print(12 !=12 or 23 ==45 or 67 == 56 or 10 > 5)

# print(not 12 == 12)

#IF else 

# a = 6

# if a > 10:
#     print("I will do task A")

# else:
#     print("I will do task B")

# money = int(input("please provide me the money :- "))

# if money == 10:
#     print("I will have a choco bar icecream")

# elif money == 20:
#     print("I will have a mangodolly")

# elif money == 30:
#     print("I will have a frosty")
    
# else:
#     print("I will have a cone")

# num1 = int(input("pleae tell your first number "))
# num2 = int(input("pleae tell your second number "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")

# else:
#     print("Both the numbers are same")


# gen = input("please tell your gender as character (M or F):-")

# if gen == 'M' or gen == 'm':
#     print("Good morning SIR")
# elif gen == "F" or gen == 'f':
#     print("Good morning MAM")

# else:
#     print("Unidentified gender")


# num = int(input("please tell your number :- "))

# if num%2 == 0:
#     print("even number")

# else:
#     print("Odd number")

# name = input("please tell your name : - ")
# age = int(input("now tell your age :- "))

# if age >=18 :
#     print(f"hello {name} you are a valid vote")

# else:
#     print(f"hello {name} you are not a valid vote")

# year = int(input("tell your year :- "))

# if year %100 == 0 and year %400 == 0:
#     print("Its a leap year")

# elif  year %100 != 0 and year %4 ==0:
#     print("Its a leap year")

# else:
#     print("its a normal year")

# t = int(input("please tell the temprature :- "))

# if t < 0:
#     print("Freezing cold")

# elif t >= 0 and t <10:
#     print("very cold")

# elif t >= 10 and t <20:
#     print("cold")

# elif t >= 20 and t <30:
#     print("plesant")

# elif t >= 30 and t <40:
#     print("hot")

# else:
#     print("temprature is very hot ")


# print("hello world ")


#For loop

#lets print a table of 5
# n = int(input("Which table you want ? "))

# for i in range(n,(n*10)+1,n):
#     print(i)

# a = "SHERYIANS TEACHES INDUSTRY THINGS"
# print(len(a))

# for i in range(len(a)):
#     print(a[i])


# a = "SHERYIANS IS COOL"

# for i in a:
#     print(i)


# for i in range(1,21):
#     if i == 56:
#         print("break statement is executed")
#         break
#     print(i)

# else:
#     print("Break statement is not executed")


# n = int(input("please tell your number"))

# for i in range(n):
#     print("hello world ")

# n = int(input("please tell your number "))

# for i in range(1,n+1):
#     print(i)

# n = int(input("please tell your number "))

# for i in range(n,0,-1):
#     print(i)


# n = int(input("which table you want : - "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")


# n = int(input("please tell your number:- "))

# sum = 0 

# for i in range(1,n+1):
#     sum = sum + i


# print(f"your sum is {sum}")

# n = int(input("please tell your number:- "))

# fact = 1 

# for i in range(1,n+1):
#     fact = fact * i


# print(f"your factorial is {fact}")


# n = int(input("tell your number :- "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i

# print(f"your even and odd sum are {even} , {odd}")


# n =int(input("which number factors you want :- "))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)


# n = int(input("check your number is perfect or not :-"))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i

# if sum == n:
#     print("your number is perfect")
# else:
#     print("not a perfect number")




# n = int(input("check your number is prime or not  :-"))

# count = 0

# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1

# if count == 2:
#     print("your number is prime")
# else:
#     print("your number is not prime")


# a = "SHERYIANS"

# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# print(b)

# a = "NAMAN"

# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]


# if b == a:
#     print("your string is pallindrome")

# else:
#     print("its not a pallindrome")

# a = "sdfsogn12413@#$%^&U"

# char = 0
# dig = 0
# spchr = 0

# for i in a:
#     if i.isdigit():
#         dig +=1 
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr +=1 

# print(f"your digits are {dig}\nyour alphabets are {char}\nyour special characters are {spchr}")

# print(dir(str))

