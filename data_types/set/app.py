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



