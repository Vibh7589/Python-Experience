# #define a function = default value
# def greet(FirstName = "default", LastName = "None"):
#     print("Welcome", FirstName, LastName)

# #call a function 
# greet("Vibh")

#Arithmetic Function

def sum(a,b):
    return a + b
print(sum(2,3)) 

def sub(a,b):
    return a - b
print(sub(2,3)) 

def mul(a,b):
    return a * b
print(mul(2,3)) 

def div(a,b):
    return a / b
print(div(2,3)) 

#print(sum(2,3)) 
# print(sub(2,3)) 
# print(mul(2,3)) 
# print(div(2,3)) 

# What is difference between function and a procedure.

# function returns a value
# procedure does not return a value.

# build in function. print len range type --> with parameter, without parameters
 
name = "Vibhuti" # global variable 

def my_function():
   #surname: "Dhimar"
   print("Hello", name)

my_function()