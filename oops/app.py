'''
OOP - oop stands for object oriented programming languga 

Advantages of oop -
                create a clear structure to programs
                makes code easrie to maintain, reusable
                help you to write DRY (Don't repeat yourself)
'''

#creation of the class
class MyClass:
    number = 67

#creation of the object
my_obj = MyClass.number

print(my_obj)

#objects can be deleted using del keyword
del my_obj

#as the object is deleted it will raise an error so wrapped in try-except
try:
    print(my_obj)
except NameError as e:
    print(str(e))

#can be implemented later if nothing is required
class Person:
    pass

#All classes by default will have a __init__() method, which always executed when class is being intitiated
# __init__() method is sued to assign values to object properties
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
user = User("Manoj", 24)
print(user.name)
print(user.age)

#without the __init__() we have to assign/set values/properties to each object


#Default values for __init__() method
class Car:
    #class properties
    is_car_certified = True
    location = ""

    def __init__(self, name, model, person_name, color="Black"):
        #slef parameters also known as object properties
        self.name = name
        self.model = model
        self.person_name = person_name
        self.color = color
    
    #self paramter is a reference to the current object of the class
    def start(self):
        print("Starting the car : {}".format(self.name))
    
    #this is example of calling the same functionsins from the class
    def wish_user(self):
        self.start()
        print("Started the car")
    
car = Car("BMW M330i", 2025, "Manoj")

print("car : {}, model : {}, color : {}".format(car.name, car.model, car.color))
car.start()

car.wish_user()

#modifying properties
car.name = "BMW"
print(car.name)

#delete properties
del car.color

car.location = "hyderabad"

#class variables
print(Car.is_car_certified)
print(car.location)

#Add new properties which doesn't exists
car.brand = "BMW"

print(car.brand)


'''
class methods
'''
class Calculator:
    pi = 3.17 #class properties
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    #class methods
    def add(self, number1, number2):
        return number1 + number2
    
    def substract(self, number1, number2):
        return number1 - number2
    
    def multiply(self, number1, number2):
        return number1 * number2
    
    def divide(self, number1, number2):
        if number2 == 0:
            raise ZeroDivisionError
        
        return number1 / number2
    
    def __str__(self):
        return "Called calualtor nethod with params {} and {}".format(number1, number2)
    
    #for the nmethod of the class first param should be slef
    def goint_to_delete(self):
        return "This will be going to delete"

number1 = 5
number2 = 6
calculator = Calculator(number1, number2)
print(calculator.add(number1, number2))
print(calculator.substract(number1, number2))
print(calculator.multiply(number1, number2))
print(calculator.divide(number1, number2))
print(calculator)

print(calculator.goint_to_delete())
del calculator.goint_to_delete

try:
    print("From here")
    print((calculator.goint_to_delete()))
except AttributeError as e:
    print(str(e))

