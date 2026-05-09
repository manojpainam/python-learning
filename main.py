#impoerting the python modules
import random

#variable declaration
name = "manoj"

#printing variable
print("Hello " + name)

#Assign multiple varibles at a time
fname, lname, phone = "Manoj", "P", "+91-9999999999"
print(phone)

#Assign single values to multiple varibles
fruit = color = "orange"
print(fruit)

#Unpack multiple values in a list
fruits = ["banana", "apple"]
first_fruit, second_fruit = fruits
#can print mutliple varibales at once
print(second_fruit, first_fruit)

#global varibales
def intial_function():
    #defining a global variable
    global review
    review = "awesome"
    #as fruit is defined here it will fetch the fruit as mango
    fruit = "mango"
    print("My fruit is " + fruit)

#calling function
intial_function()

#as fruit is a global variable it will fetchb orange
print(fruit)

#As review is defined as global it will fetch value
print("Python is " + review)

'''
Data Types -
Text type     : str
Numeric type  : int, float, complex
sequence type : list, tuple, range
mapping type  : dist
set    type   : set, frozenset
boolean  type : bool
bytes   type  : bytes, bytesarray, memoryview
none    type  : none
'''
#get the type of varibales using type()
print(type(fruits))

#int - float - complex data types
#int     - suppperts the numbers with posivite or negative numbers
#float   - will have numberic types
#complex - complex numbers are written with j as a imaginary part
x, y, z = 1, 2.1, 1j
print(type(x), type(y), type(z), x, y, z)

#type conversion - also called as the type casting float(x) is a type casting here
print(type(float(x)))

random_number = random.randrange(1, 10)

def guess_number():
    count = 0
    while(count != 3):
        guessed = int(input("Enter the number : "))

        if random_number == guessed:
            print("You guessed in it correctly")
            break
        else:
            if count == 2:
                print("max appemts reached generated number is ", random_number)
                break
            else:
                print("Try again with different number")
                count += 1
            
guess_number()