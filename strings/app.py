#strings can be defined with using single or double quotes - below data will have the same effect
print('hello')
print("hello")

#Assing values to a variable
greeting = 'Good evening '

print(greeting)

#
quote = '''
This is a multiline
quote
'''

print(quote)

#strings as arrays
learning = 'java python'
print(learning[1])

print()

#get length of the string  using len
print("Length of the word is : ", len(learning))


'''
Looping
'''
#looping through strings
for x in learning:
    print(x)


#check a string exists in a word
if "python" in learning:
    print("Yes word exists in ", learning)

if "php" not in learning:
    print("Hey php not exists in ", learning)

#slicing in strings - can return a range of characters by using slice syntax
#In slicing the start in inclusive where as end is exclusive(not included)
print(learning[2:7])

#slice from start
print(learning[:7])

#slice till end
print(learning[2:])

#negative slicing
print(learning[-6:])

'''
Modify strings
'''
print(greeting.upper(), greeting.lower(), greeting.strip(), greeting.replace("evening", "night"), greeting.split(" "))

'''
Concatination
'''
fname = 'John'
lname = 'Doe'
age = 56
print(fname+" " + lname)

#concatination can only be done str to str not str to int or vice versa if we try to do so will produce an error
#print(fname + age)
#print(age + fname)

#instead of above we can use f-strings like this - using place holders {var_name}
print(f'Full Name is {fname} {lname} with age {age}')


