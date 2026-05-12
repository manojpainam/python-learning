#List is used to store the simialr kind of data in a single varible
fruits = ["banana", "apple", "mango", "kiwi"]

#List is one out of four built in data types in python
'''
List Items are - Ordered ## When we say ordered means that the items have different order and it won't chnage
               - changable ## we can add or remove elements from the list
               - Allows dupliacates ## since lists are indexed can have multiple dupilicate values
'''

#print(fruits[1]) ##accessing the elements of the list
print(fruits)

print(len(fruits)) #length of the list

#to create a new list we have to use contructor by using list()
names = list(('manoj','purna', 'vanshi', 'prasad'))
print(type(names)) #print type of the list

'''
Accessing list items
'''
print(names[1]) #indexing
print(names[-1]) #print last element negative indexing
print(names[1:3]) #range of indexing

if 'manoj' in names:
    print("Name exists in the list")

'''
chnage list items
'''
names[2] = "vamshi" #chnage the 3rd element of the list
print("List after updation", names)
names[2:4] = ["vamshi P", "Prasad P"] #update the values of the third and fourth element 
print(names)

names.insert(0, "Sravya")
print(names) #to insert new element without changing the existing values we have to use insert



'''
Add ietms to the list
'''
names.append("surya kumary yadav") #Add elment at the end of the list using Append
print(names)

contries = ["India", "Russia", "USA"]
nearby_contrues = ["china", "bangladesh"]

contries.extend(nearby_contrues) #to extend element from another list
print(contries)

#extend method doesn't necessarly need to be a list it can be any iterable as well - tuple, set, dict as well
thistuple = ('thailand', 'nepal')
contries.extend(thistuple)
print("countries after the tuple extension", contries)