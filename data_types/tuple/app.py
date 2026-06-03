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