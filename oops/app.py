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
    def __init__(self, name, model, person_name, color="Black"):
        #slef parameters
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