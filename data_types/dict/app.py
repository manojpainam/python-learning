'''
Dict are used to store the values in key value pairs
'''

#dict can have any type of data
thisdict = {
    "name" : "manoj",
    "designation" : "package app development analyst",
    "expirence" : "3",
    "age" : 25,
    "graduated" : 1 
}

#dict is ordered and changable and doesn't allow duplicate keys
print(thisdict)

#accessing elements
print(thisdict["name"])

#get the type
print(type(thisdict))

#print the length of the dict
print(len(thisdict))

#dict constructor
new_dict = dict(name = "manoj", age = 25, college = "Aditya Engineering College")
print(new_dict)

#get only keys
print(new_dict.keys())

new_dict["age"] = 24
print(new_dict)

print(new_dict.values())

'''
items method will return the key:value as a tuple in a list -
    [(key, value), (key, value)]
'''
print(new_dict.items())

#check if key exists in dict
if "age" in new_dict:
    print("Hey, My age exists and it is ", new_dict["age"])


'''
Update dict elements
'''
thisdict["expirence"] = 2.10

#using update method
thisdict.update({"name":"Manoj P"})


'''
Add items to the dict
'''
thisdict["nationality"] = "Indian"

thisdict.update({"graduation_stream":"Mining Engineering"})



'''
Remove dict items
'''
#pop method removes the item specified at key
#del will also works the same
#del can also removes the complete dict
thisdict.pop("age")
del thisdict["expirence"]

#will remove the lastitem
thisdict.popitem()
print(thisdict)

del thisdict
#as we have deleted the dict above it will throw error
#print(thisdict)

#clear method empties the list
#new_dict.clear()

'''
Looping through dict
'''
#this will only prints the keys
for item in new_dict:
    print(item)

#this will print the values of the dict
for key in new_dict:
    print(new_dict[key])

#to get both keys and values
for key, value in new_dict.items():
    print(key, value)

'''
Copying dict
'''
#we can't copy the dict directly by dict2 = dict1 because changes made to dict1 will sync to dict2 instead it can be copied using copy method
copied_dict = new_dict.copy()
print(copied_dict)