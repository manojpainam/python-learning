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

'''
O(n) Time complexity -
                The time complexity of this problem is O(n) as we are doing the only one loop and rest we are changing the values of the variables/constants
                O(n) - is the better time complexity algorithm also known as the linear time complexity
Kadane's algorith
'''
def max_subarray_sum(arr):
    res = arr[0]

    max_element = arr[0]

    for i in range(1, len(arr)):
        max_element = max(max_element + arr[i], arr[i])

        res = max(res, max_element)
    
    return res

print(max_subarray_sum([-2, -4]))

