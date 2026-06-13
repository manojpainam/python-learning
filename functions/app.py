'''
In python functions are defined by def keyword
'''

#Function : function is a piece of code which runs only when it is called

#this is a function
def my_function():
    print("This is a function")

#above function is being called from here now
my_function()

#why functions : make a code to write once and then access as many times as needed. It will remove the code duplication

#without function
temperature1 = 45
celcius1 = (temperature1 - 32) * 5 / 9

print(celcius1)

temperature2 = 56
celcius2 = (temperature2 - 32) * 5 / 9
print(celcius2)

#if we observe that the code has become duplciated instead if we use functions then it won't get dupliacted
def fahrenheit_to_celsius(temperatue):
    #instead of just printing values we can just return the values whomever it is calling
    return (temperatue - 32) * 5 / 9

#Now we can call the function multiple times with different parameters (temperatues) but the main logic of conversion remains only once
print(fahrenheit_to_celsius(45))
print(fahrenheit_to_celsius(56))

def empty_function():
    pass

#As we called the function which doesn't do anything it will print None
print(empty_function())

#Params to a function : num1 and num2 are (params or aruguments)
def addition(num1, num2):
    return num1 + num2

print(addition(56, 99))

#this function has only one argument
def greetings(name):
    return "Helllo " + name

print(greetings("Manoj"))

#This function has the 2 aruguements
def get_fullname(fname, lname):
    return fname + " " + lname

print(get_fullname("Manoj", "P"))

#In Python we can also have the default args as well if value provided then it will show that value else it will take the default assigned value
def greet_user(name = "User"):
    return "Hello " + name

print(greet_user())

#KeyWord arguments : when we are calling the key word arguments then the order doesn't matter
fullname = get_fullname(lname = "P", fname = "Vamshi")
print(fullname)

#postional only args method we can specify uding / if we try to use the keyword then it will throw error
def postional_arg(number1, /):
    print("Received the number ", number1)

postional_arg(56)

def only_keyword_arg(*, number):
    print("Revied number for keyword arg ", number)

only_keyword_arg(number=1)

def comibned(a, b, /, *, c, d):
    print("Received ", a, " ", b, " ", c, " ", d)

comibned(56, 65, c = 91, d = 100)