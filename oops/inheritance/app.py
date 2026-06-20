'''
Inheritance -
            it allows us to define a class inherits all methods and properties
            parent class is the class that is being inherited from, also called the base class
            child class is the class that inherits from, also called the base class
'''

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def print_name(self):
        return "Hi this is {} {}".format(self.fname, self.lname)

person = Person("Manoj", "P")
print(person.print_name())

#syntax for inheritng the class into another class
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year
    
    def welcome(self):
        return "Hi {} {}, welocme to the year : {}".format(self.fname, self.lname, self.year)

student = Student("Manoj", "P", 2026)
print(student.welcome())