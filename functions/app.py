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


#By default function has to be called with certail params in specific cases we may not know how many params are being passed.
'''
arbitrary arguments - when we don't know the how many number of args can be passed to a method
        - if we keep * then it will become a arbitrary args the functions will receive a tuple elements
'''
def arbitrary_args(*args):
    return "I have received this parmas : " + args[0] + " " + args[1]

print(arbitrary_args("Passport", "Name"))


##arg with regular aruguments
def greet_people(greeting, *names):
    for name in names:
        print(greeting, name)

greet_people("Hello", "Manoj", "Vamshi", "Prasad")


#practical example : sum of all the numbers
def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    
    return total

print(sum(10, 20, 30, 40))
print(sum(10, 20, 30, 40, 50))
print(sum(10))


#practical example : max of all the numbers
def find_max(*numbers):
    if len(numbers) == 0:
        return None
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    
    return max

print("The maximum number is : ", max(89, 67, 100, 105, 45, 68))


''''
Arbitrary keyword arguments -
        sometimes we don't know how many parameters can be passed to a function in such cases we need to use this
        can be defined by **
'''
def arbitrary_args(**names):
    return "Hello" + names["fname"] + " " + names["lname"]

print(arbitrary_args(fname = "Manoj", lname = "P"))

'''
Decarators - it add extra behaviour to the function without changing the function code
A decorator is a function that takes another functions as a input and returns a new function
'''

def changecase(func):
    def myinnerfunc():
        return func().upper()
    return myinnerfunc


@changecase
def greet_with_decorator():
    return "hello manoj painam"

print(greet_with_decorator())

print(greet_with_decorator.__name__)

'''
Lambda
'''
# lambda arguments : expressions

product = lambda a, b : a * b
print(product(45, 34))

#lambda functions
def myfunc(n):
    return lambda a : a * n

my_doubles = myfunc(2)
print(my_doubles(11))

'''
Recursion is a function calling it self
'''

def do_job(n):
    if n <= 0:
        print("Job is Done")
    else:
        print(n)
        do_job(n-1)

do_job(5)


#for a recursion there will be two set of statements - a base condition (when it should stop) - Recursive case (calling itself with modified data)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(10))