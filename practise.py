names = ["manoj", "vamshi", "purna"]

for name in names:
    print(name)

names.append("prasad")

print(names)
names.pop()
names.pop()

for i in range(len(names)):
    print(names[i])

additional_names = ["purna", "prasad", "sravya"]

names.extend(additional_names)

print(names)

print(names[1:])
print(names[1:3])
print(names[::-1])
print(names[2:])

names.remove("manoj")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

[print(number) for number in numbers if number % 3 == 0]

[print(name) for name in names if "a" in name]

random_numbers = [90, 86, 45, 56, 1, 23, 45, 20, 99]
random_numbers.sort(reverse=True)
print(random_numbers)


################################################################
#tuple

movies = ("epic", "bangaram", "kushi", "svsc")

print(movies)
print(movies[1])
l_movies = list(movies)
l_movies.append("f1")
movies = tuple(l_movies)
print(movies)

for movie in movies:
    print(movie)

#gadgets
gadgets  = ("macbook",)
print(type(gadgets))

info = ([90, 91, 93], "manoj", 26, ["maths", "physics", "chemistry"])

#unpacking elements
marks, user, age, subjects = info

print(subjects)


#######################################################################
#set
cricket_temas = {"rcb", "csk", "mi", "gt"}
extra_teams = {"rcb", "lsg", "srh", "dc"}
for team in cricket_temas:
    print(team)


cricket_temas.update(extra_teams)

print(cricket_temas)

#set cab be created using set constructor
my_set = set((10, 20, 30, 40))

#my_set.remove(50)
my_set.discard(50)


######################################################################
my_info = {
    "name" : "manoj",
    "age" : 26,
    "skills" : ["java", "python", "react"],
    "education" : {
        "school" : "CCS - ongole",
        "diploma" : "GPT - Gudur",
        "bachelors" : "AEC - Surampalem"
    },
    "experience" : {
        "talentsprint" : {
            "yoe" : "2.5",
            "doj" : "01-07-2023",
            "acquired_skills" : ["spring boot", "java", "python"]
        },
        "accenture" : {
            "yoe" : "0.9",
            "doj" : "01-12-2025",
            "acquired_skills" : ["php", "java8", "react"]
        }
    }
}

for obj in my_info:
    print(my_info[obj])

for key, value in my_info.items():
    print(key,":",value)

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # Create a dictionary to store each number and its index
    required_nums = {}

    # Iterate through the list using the index
    for i in range(len(nums)):
        # Calculate the number needed to reach the target
        required = target - nums[i]

        # Check if the required number has already been seen
        if required in required_nums:
            # Return the index of the required number and the current index
            return [required_nums.get(required), i]
        
        # Store the current number and its index in the dictionary
        required_nums.update({nums[i]: i})

    # Return an empty list if no valid pair is found
    return []

print(twoSum([2, 7, 5, 8], 7))


#a number is said to be majority element if the number is appeared in the list more than len(list) / 2 times
def majority_element(nums: List[int]) -> int:
    #create to varibles to track count and majority
    majority = None
    count = 0

    #looping thorugh numbers
    for num in nums:
        #if count is 0 then update the majority
        if count == 0:
            majority = num

        #if current number and majority is equal then update the count (increase)
        if num == majority:
            count += 1
        else:
            #else update the count (decrease)
            count -= 1
    return majority

print("Majority element of the list is :", majority_element([1, 2, 3, 3, 3, 4, 4, 4, 4, 5]))

def contains_duplicates(nums: List[int]) -> bool:
    #check the length of the list is equals to the len of the set conversion of the list
    return len(nums) != len(set(nums))

print("containes duplicates in the list:", contains_duplicates([1, 2, 3, 4, 5, 6, 7]))


#mutable vs immutable

#immutable once the value is created it can't be chnaged in python tuple and strings are immutable
try:
    my_tuple = ("1", "2", "5")
    my_tuple[1] = "56"
except Exception as e:
    print(str(e))

try:
    my_string = "manoj"
    my_string[2] = "t"
except Exception as e:
    print(str(e))

#mutable objets where its values can be changed once they have been create - In python list, dict, sets are mutable
bikes = ["glamour", "unicorn", "shine"]

bikes[1] = "Honda Unicorn"

print(bikes)

my_info["name"] = "Manoj Painam"

print("\n", my_info)



#### indexing #######
marks = [100, 99, 78, 89, 90]

print(marks[0])
print(marks[-5])

#indexing can also be used to modify the vakues of a list
marks[0] = 69
print(marks)

print("with step:", marks[0:5:2])

#since strings are immutabke we can't change the values it once it was created we have seen the same above

#indexing and slicing
fruits = ["apple", "banana", "kiwi", "water melon", "dragon fruit"]

print(fruits[0:3])
print(fruits[:3])
print("Reverse of a list is :", fruits[::-1])

for index, value in enumerate(fruits):
    print("index:", index, "value:", value)

it = iter(fruits)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#membership if an object it is used to check the membership of a object in sequence.
#this includes the operators like in/not in

l = [1, 2, 3, 4, 5]
statment = "Hello world"

if 2 in l:
    print("2 exists in the list")

if 'o' in statment:
    print("'o' exists in the statement")

if 'z' not in  statment:
    print("z is not in the statement")

import operator

print(operator.contains(l, 5))


data = [1, 2, 2, 3, 4, 4, 5]

print(list(set(data)))


s = "programming"

frequency = {}

for i in s:
    frequency[i] = frequency.get(i, 0) + 1
print(frequency)


#creating a function
def my_function():
    print("This is a function and it will be executed if and only if it is called")

#calling a function
my_function()

def greet_people(name = "User"):
    print("Hello,", name)

greet_people("Manoj")
greet_people()

def name_people(*people):
    print(people[0], people[1], people[2])

name_people("manoj", "vamshi", "purna")

lambda a, b : a + b
    