#This file is to learn about tuples

'''
Tuple is one of the built in data-types in python - which is ordered and unchangable
Tuple doesn't have add/extend or remove method as the data is unchangable
'''

thistuple = ("banana", "orange", "orange")

#printing the tuple
print(thistuple) 

#Print the type of tuple
print(type(thistuple))

#print(length of the tuple)
print(len(thistuple))

'''
To recorgnise something as a tuple in python - if we want to have a single element as a tuple then we should have the , at the end or else it will be treated as a string
'''
names = ("sona",)
print(type(names))

multi_data_type_tuple = ("manoj", 5, [1,2,3,56], False)

print(multi_data_type_tuple)


'''
Accessing elements of the tuple
'''
#acessing element using index
print(multi_data_type_tuple[2])

#negative indexing
print(multi_data_type_tuple[-1])

#range indexing
print(multi_data_type_tuple[0:2])

#if item exists in the tuple
if "manoj" in multi_data_type_tuple:
    print("Hey, 'manoj' exists in the tuple")

'''
Updating tuple - Since tuples are immutable we can't add or delete elements from the tuple
instead we can do the below to do the same - convert the tuple to list and then add element to the list and then change back list to tuple
even have to do the same for the removing as well
'''
fruits = list(thistuple)
fruits[1] = "kiwi"
thistuple = tuple(fruits)

print(thistuple)


'''
Packaging and unpacking tuples
'''

#packing
names = ("manoj", "vamshi", "purna", "prasad")
#unpacking
(eleder_son, younger_son, wife, me) = names
print(eleder_son)

#if the number of values are greater then number of total values of the tuple then use * to get the rest of the values as list
states = ("maharastra", "kerala", "andhra pradesh", "telangana", "tamilnadu", "west bengal")
(mp, *southern_states, wb) = states

print(southern_states)
