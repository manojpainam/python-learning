#varibales

name = "manoj" #string
age = 25 #int
is_married = False #bool
salary = 53647.00 #float

#type casting
print("float conversion of int :", float(age))
print("int conversion of float is :", int(salary))
print("string conversion of int is:", str(age))

#get the type of the varibales
print("Type of the name varible is :", type(name))
print("Type of the age varible is :", type(age))
print("Type of the salary varible is :", type(salary))
print("Type of the is_married varible is :", type(is_married))

#assigning multiple values or varibles at once
x, y, z = 10, 20, 50
print(x, y, z)

#scope of varibles
def do_something():
    global occupation 
    occupation = "Packaged app development analyst"
    pass

#calling is necessary or else the value inself is not assigned without calling the function 
do_something()
print("occupation is declared inside the do_sonething but still we will be able to access it:", occupation)
