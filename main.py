#impoerting the python modules
import random

#variable declaration
name = "manoj"

#printing variable
print("Hello " + name)

#Assign multiple varibles at a time
fname, lname, phone = "Manoj", "P", "+91-9999999999"
print(phone)

#Assign single values to multiple varibles
fruit = color = "orange"
print(fruit)

#Unpack multiple values in a list
fruits = ["banana", "apple"]
first_fruit, second_fruit = fruits
#can print mutliple varibales at once
print(second_fruit, first_fruit)

#global varibales
def intial_function():
    #defining a global variable
    global review
    review = "awesome"
    #as fruit is defined here it will fetch the fruit as mango
    fruit = "mango"
    print("My fruit is " + fruit)

#calling function
intial_function()

#as fruit is a global variable it will fetchb orange
print(fruit)

#As review is defined as global it will fetch value
print("Python is " + review)

'''
Data Types -
Text type     : str
Numeric type  : int, float, complex
sequence type : list, tuple, range
mapping type  : dist
set    type   : set, frozenset
boolean  type : bool
bytes   type  : bytes, bytesarray, memoryview
none    type  : none
'''
#get the type of varibales using type()
print(type(fruits))

#int - float - complex data types
#int     - suppperts the numbers with posivite or negative numbers
#float   - will have numberic types
#complex - complex numbers are written with j as a imaginary part
x, y, z = 1, 2.1, 1j
print(type(x), type(y), type(z), x, y, z)

#type conversion - also called as the type casting float(x) is a type casting here
print(type(float(x)))

random_number = random.randrange(1, 10)

def guess_number():
    count = 0
    while(count != 3):
        guessed = int(input("Enter the number : "))

        if random_number == guessed:
            print("You guessed in it correctly")
            break
        else:
            if count == 2:
                print("max appemts reached generated number is ", random_number)
                break
            else:
                print("Try again with different number")
                count += 1
            
#guess_number()


def longestCommonPrefix(strs):
    # Edge case: no strings given, so there's no prefix to find
    if not strs:
        return ""

    # Start by assuming the entire first string is the common prefix.
    # We'll shrink this guess as we compare against the other strings.
    prefix = strs[0]

    # Compare our current guess against every other string in the list
    for s in strs[1:]:
        # Keep chopping the last character off prefix until
        # the current string actually starts with it
        while not s.startswith(prefix):
            prefix = prefix[:-1]

            # If we've trimmed all the way down to nothing,
            # there's no common prefix at all — exit early
            if not prefix:
                return ""

    # After checking against every string, whatever remains
    # in prefix is the longest common prefix
    return prefix

strs = ["mango", "manoj", "manchuria", "mangrooves"]
print("Longest prefix is : ", longestCommonPrefix(strs))


#leet code easy problem
def is_valid(s):
    stack = []
    pairs = {
        '{' : '}',
        '[' : ']',
        '(' : ')'
    }

    for char in s:
        #check if the char exists in the pairs
        if char in pairs:
            #if exists then appened to the stack
            stack.append(pairs[char])
        
        #if the stack is empty or if the last opened bracke is not correct then return False 
        elif not stack or stack.pop() != char:
            return False
    
    return not stack

print(is_valid("()[]{(})"))


def two_sum(nums, target):
    required_num = {}

    for i in range(len(nums)):
        required = target - nums[i]

        if required in required_num:
            return [required_num.get(required), i]
        
        required_num.update({nums[i] : i})
    
    return []

nums = [3, 2, 4]
target = 6
print("two sum :", two_sum(nums, target))


def plusOne(digits):

        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):

            # If digit is less than 9
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If digit is 9, make it 0
            digits[i] = 0

        # If all digits were 9
        return [1] + digits

digits = [1,2,3]
print("plus one :", plusOne(digits))