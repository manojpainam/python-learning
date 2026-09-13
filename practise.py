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