# name=2025 
# print(type(name)) 
# name = 20.56 
# print(type(name))
# name = True
# print(type(name))

# x = None
# x = 3.5678

# print("Hello world") # print statement 
# var = 10 # variable declaration and initialization assignment statement 

# print(5+2)
# print (5 * 2)
# print (5 -2)

# arithmetic operators () * / % + -
#comparison operator == != > < >= <=

#Type casting

# a = bool(1)
# a = int(100)
# a = float(100)
# a = str(100)

# string
#firstName = "Vibhuti" #string variable 
#lastName = 'Dhimar'

# # string cancatenation
# print(firstName.upper() +" "+ lastName) 

#print(firstName[-5:-1])

#Logical AND(all the conditions must be TRUE to procced) OR (Only one condition needs to be TRUE to proceed) NOT (REVERSE)
#comparison == ! = > <= TRUE / FALSE

# num1 = 5
# num2 = 7

# #print(not(num1 <= num2))

# #Login
# email = "vibhutidhimar@live.com"
# password = "12345"

# if email == "vibhutidhimar@live.com" and password == "12345"
#     print("welcome") 
# # elif password == 123456:
# #     print("password is correct")
# else:
#     print("Sorry your password and or email are not correct")

#number = 5

# if number % 2 == 0:
#     print("number is an even number.")
# else:
#     print("number is an odd number.")

list

# fruits = ["apple" , "bananas" , "Cherry"] #list of strings ordered, changable, duplicates, indexed

# print("before addition", fruits)
# fruits.append("bananas")
# # print("before removal", fruits)
# # fruits.remove("bananas")
# # print("after removal", fruits)
# # fruits.pop(len(fruits)-1)


# print(fruits[2])
# print(len(fruits))

# example = "vibh vibh vibh vibh vibh vibh"
# print(len(example))
# print (type(example))


# tuples
#fruits = ("apple" , "bananas" , "Cherry") # tuple of strings ordered, unchangable, duplicate, indexed
#fruit.

# print(fruits)
# print(type(fruits))
# print(list(fruits))
# print(tuple(fruits))

# fruits[0] = "orange" #typeError: 'tuple' object does not support item assignmnet 
# tuple(fruits)

#Is there any way to change value in Tuple?

# sets

# fruits = {"apple" , "bananas" , "Cherry"} #no duplicates , unordered, unchangable, unindexed 
# fruits.add("kivi") #adding a value 
# print(fruits)

# dictionaries - phone dictionary - key value pair - changable, ordered, no duplicate 

# phoneDictionary = {
    
#     "John": 67676687,
# }
# print(phoneDictionary["John"])

# users = {
#     {
#         "firstName": "Jane",
#         "lastName": "Doe",
#         "phoneNumber": "1234567890",
#         "email": "lorem@gmail.com",
#         "address": "123, Lorem Ipsum"
#     },
#     {
#         "firstName": "John",
#         "lastName": "Doe",
#         "phoneNumber": "1234567890",
#         "email": "abc@mail.com",
#         "address": "123, Lorem Ipsum"
#     }
# }

# print(users[0])


# player_score = 0
# correct_answer = 0

# x = int(input("Enter player score:"))
# print(player_score + 5, x)

# y = input("Enter correct answer:")
# print(correct_answer + 3, y)

# if player_score == correct_answer:
# #     # player_score + 10
# #     # correct_answer + 1
#     print("correct")
# else:
#    print("incorrect")


# Loops 

# For loops

# for i in range(1, 50):
#     print(i)

#While loops

i = 1
# while i < 50:
#     print(i)
#     i = i + 1 # increamenting the value of i by 1
#    # i +=1
  #   i = i - 1 #decrementing the value of i by 1 


# i = 1
# for x in range(1,5):
#     i = i * x
# print(i)

# number = 1
# for i in range(1,6):
#     number*=i
# print(number)

#factorial of 5 = 5 * 4 * 3 * 2 * 1 = 120

# 1. sequence
# 2. conditional statement
# 3. loops / iterations

# myFirstName = "Muhammed"
# for character in myFirstName:
#     print(character)

# myList = [1,2,3,4,5,6,7,8,9,10]
# for number in myList:
#     print(number)

# mySet = {1,2,3,4,5,6,7,8,9,10}
# for number in mySet:
#     print(number)

# myTuple = (1,2,3,4,5,6,7,8,9,10)
# for number in myTuple:
#     print(number)

# for i in range(1, 10):
#     if i == 5:
#         continue
#     print (i)

# myCountryList = ["United Kingdom","India","Spain","USA"]

# for country in myCountryList:
#       print(country)

# if myCountryList[3] == "Spain":
#       print("Yaay!")
# else:
#       print("Boo")

myFirstName = "Vibhuti"
reversed = myFirstName[::-1]
print(reversed)

#for char in reversed:
 #   print(char)

import random

targetNumber = 6
guess = random.randint(0, 6)

# ! = not equal to 
while guess != targetNumber:
    print("sorry, that's not it.")
    guess = random.randint(0, 6)
    print("Guess again as your guess was", guess)

print("you got it")

create a repository named Python-Experience 

https://github.com/Vibh7589/Python-Experience
git clone https://github.com/Vibh7589/Python-Experience

   









