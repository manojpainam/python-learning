'''
Set is one of the data types in the python - 
        set is unordered, unindexed and unchangable also it doesn't allow the duplicate elements
'''

#set is unordered which means that we are not sure which order the elements will appear
thisset = {"manoj", "vamshi", "prasad", "purna", "sravya", "manoj", True, False, 1}
#this doesn't garuntee that it will print the elements in the same order that we have kept the data
#set does allow duplicate elements - even though we kept the manoj twice it will print only once
#True and 1 refers to be same so it will print any one same for false and 0
print(thisset)

#length of the set
print(len(thisset))

#to make anything to be like set use set() function (also known as set constructor)
names = set(("manoj", "vamshi", "purna", "prasad"))
print(names)


print("\nName of the participants - ")
'''
Accessing elements
'''
for name in names:
    print(name)

#check if element exists in the set
message = "Exists" if "Johnny" in names else "Doesn't exists"
print(message)

#add element to the set
names.add("pavan")
print(names)

education_data = {"chaitanya central school"}
collegs = {"Govt polytechnic college Gudur", "Aditya engineering college"}

#to add the two sets
education_data.update(collegs)
print(education_data)

#Add any iterable
thislist = ["TalentSprint"]
education_data.update(thislist)

print(education_data)

#remove element from the set
education_data.remove("TalentSprint")
print(education_data)

'''
Remove - Will remove an element from the set if exists, if the element doesn't exists then it will raise an error
discard - will remove an element from the set if exists, if it doesn't exists it doesn't raise any exception
pop - will also remove the element but it doesn't grantuee which element will get removed as the elements is unordered
clear - this method will empties the set
del - this will deletes the set completely
'''
#this will raise the error as the key already removed
#education_data.remove("TalentSprint")

#this won't raise any error
education_data.discard("TalentSprint")

#pop
education_data.pop()
print(education_data)

#clear
education_data.clear()
print(education_data)
del education_data

#as we have deleted this varibale above this will produce an error
#print(education_data)

#looping sets
heros = {"Ram Charan", "Pawan Kalyan", "Jr NTR", "Allu Arjun"}
for hero in heros:
    print(hero)

'''
Joining sets
'''
#As we know that set doesn't allow duplicates it will ignore if dupliactes exists
mid_heros = {"Ram Charan", "Varun Sandeesh", "Sai Dharam Tej"}

#union method is used to combine the 2 sets
#union will create a new set
combined_heros = heros.union(mid_heros)
print(combined_heros)

alphabets = {"a", "b", "c", "d"}
numbers = {1, 2, 3, 4}

#Also we can use | operator to work same as union
combined_data = alphabets | numbers
print(combined_data)

#can join multiple sets using union method also we can also use | to join the same
whole_data = combined_heros.union(combined_data, thisset)
print(whole_data)

#update method | it will not create a new set instead it can update the existing set
#heros.update(mid_heros)
#print(heros)

#intersection will keep the only duplicate elements | will return a new set
new_set = heros.intersection(mid_heros)
print(new_set)

#also we can use & to perform the same intersection method
common_elements = heros & mid_heros
print(common_elements)

#just like the intersection method it will show only the common element but instead of new set it will show in the existing elememt
# heros.intersection_update(mid_heros)
# print(heros)

#Difference method will return the elements from the first elements which doesn't exists in the second set
new_heros_set = heros.difference(mid_heros)
print(new_heros_set)

# - operator will give the same result as difference
new_heros_set_using_hyphen = heros - mid_heros
print(new_heros_set_using_hyphen)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

new_set_of_heros = heros.symmetric_difference(mid_heros)
print(new_set_of_heros)

#we can also use ^ to perform the same symmetric_difference
new_set_of_heros_using_cap = heros ^ mid_heros
print(new_set_of_heros_using_cap)

set3 = {"apple", "banana", "cherry"}
set4 = {"google", "microsoft", "apple"}

#to keep the items that are not present in both sets
set3.symmetric_difference_update(set4)

print(set3)

'''
frozen set - unlike sets fronset doesn't allow to create or delete the elements
'''
x = frozenset({"pondicherry", "tiruvanmalai", "banglore", "Hyderabad"})
print(x)
print(type(x))