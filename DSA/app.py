'''
In python list is one of the data sturuces and it will server as a dynamic arrays
'''

#defining a list
numbers = [1089, 58, 60, 109, 789, 456, 54, 987, 435, 5, 9879]
smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print(smallest)


'''
Time complexities -
    O(1)  -- Best time complexity (As the even the number of input size changes it won't change the number of operations) 
    Examples - printing the first element in the list, print the last element of the list
'''
print(numbers[0]) #this will take exactly one operation to find out the element
print(numbers[len(numbers) - 1]) #Even this will take exactly one opeation to get the last element of the list

sum_of_n_numbers = 100
sum = sum_of_n_numbers * (sum_of_n_numbers + 1) / 2  #Even if the sum_of_n_numbers changes to higer number it will be judt one operation
print(sum)

'''
Time complexity of hashmaps will be O(1) - it is not actual but it is amatized (average) calculated values
'''

'''
Time Complexity -
    O(n) - also known as linear time complexity
'''
def factorial(number):
    factorial = 1

    for i in range(1, number): # this is running n times and trying to change a constant factorial value which is K O(n * K) since K is constant then it will become O(n)
        factorial *= i #This is constant

    return factorial

print(factorial(10))