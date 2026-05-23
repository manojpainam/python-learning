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
thistuple = ('thailand', 'nepal', 'fiji')
contries.extend(thistuple)
print("countries after the tuple extension", contries)

'''
Remove items
'''
#remove specific item from the list
names.remove("surya kumary yadav")
print(names)

#remove 0th element from the list
names.pop(0)
print(names)

#if not specifoed the index in the pop then it will automatically remove the last item
names.pop()
print(names)

#rdel keyword is used to delete the list completely
del names[0]
print(names)

#to clear the ietms in the list retaining the list
# names.clear()

# print(names)

'''
Looping list
'''
print("\nPrinting items through the normal looping of the list - ")
for country in contries:
    print(country)

print("\nPrinting items through the normal looping of the list using range and len- ")
for i in range(len(contries)):
    print(contries[i])

print("\nusing while loop")
count = 0
while(count < len(contries)):
    print(contries[count])
    count += + 1

print("\nUsing short for loop")
[print(x) for x in contries]

#List conprehension
new_contries = [x for x in contries if "a" in x]
print("\nnew contries : ", new_contries)

#list comprehensation using the ramge
nums_greater_10 = [x for x in range(11) if x > 5]
print(nums_greater_10)

'''
Sorting lists
'''
names.append("Gawtham")
print("\nnames before sorting : ", names)
names.sort()
print("\nnames after sorting : ", names)

numbers = [3, 5, 33, 21, 46, 9, 56, 89, 10]
print("\nNumber before sorting : ", numbers)
numbers.sort()
print("\nNumbers after sorting : ", numbers)
numbers.sort(reverse=True)
print("\nNumbers in descending order : ", numbers)



# Returns how far a number is from 50
# Smaller value means closer to 50
def myfunc(n):
    return abs(n - 50)

# List of numbers
thislist = [100, 50, 65, 82, 23]

# sort() uses the returned value from myfunc()
# Numbers closest to 50 come first
thislist.sort(key=myfunc)

print(thislist)

print("\nsort in reverse")
#thislist.sort(reverse=True)
#print(thislist)
thislist.reverse()
print(thislist)


fruitslist = ["Orange", "cherry", "Kiwi", "Apple"]
#this is will sort the data based on the alphabatical order
fruitslist.sort(key=str.lower)
print(fruitslist)

#this will sort the data based on the data we have provide
#example list is [1, 2, 4, 3] then rever will become [3, 4, 2, 1]
the_numbers = [1, 2, 4, 3]
the_numbers.reverse()
print(the_numbers)


'''
Copying the list
'''
our_family_names = ["manoj", "vamshi", "purna", "prasad"]
copied_names = our_family_names.copy()
print(copied_names)
using_list_method = list(our_family_names)
print(using_list_method)
using_slice_operator = our_family_names[:]
print(using_slice_operator)


'''
join lists
'''
#using concatination operator
group1 = ["RCB", "MI", "CSK", "PBKS", "GT"]
group2 = ["RR", "SRH", "LSG", "KKR", "DC"]

print(group1 + group2)

#looping and appending to group1
for team in group2:
    group1.append(team)

print(group1)

#using extend
old_teams = ["RPS", "DCH"]
group1.extend(old_teams)
print(group1)

