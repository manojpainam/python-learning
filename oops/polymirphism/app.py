'''
Polymorphism - 
            The word polymorphism refer to the many forms
            In Programming methods/operators/functions with same name that can be executed on many objects or classes
'''

#len() is a example of polymorphism beacuse it can check he numbers of characters in sting, numbers of items in an tuple
my_list = ["manoj", "vamsi", "purna", "prasad"]
#here it can print the len of the list
print(len(my_list))

my_str = "Hello world!"
#here it can print the len of the string
print(len(my_str))

class Car:
    def __init__(self, name, company):
        self.name = name
        self.company = company
    
    def move(self):
        print("Move!")

class Boat:
    def __init__(self, name, company):
        self.name = name
        self.company = company
    
    def move(self):
        print("Sail!")
    
class Aeroplane:
    def __init__(self, name, company):
        self.name = name
        self.company = company
    
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Aeroplane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  #we can see that move method is there in all objects
  x.move()