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
                Examples - Kadane's algorithm, nth fabinocci series
'''
def max_subarray_sum(arr):
    res = arr[0]

    max_element = arr[0]

    for i in range(1, len(arr)):
        max_element = max(max_element + arr[i], arr[i])

        res = max(res, max_element)
    
    return res

print(max_subarray_sum([-2, -4]))

'''
O(n^2) or O(n^3) Time complexity - 
                            This is mostly used in the sorting techniques.
                            Bubble sort, insertion sort, selection sort are the examples of the sorting tevhniques
                            this will have the nested loops
'''

#bubble sorting functionality - it tries to sort the order of elementd in s array(list)
def bubble_sort(arr):
    length = len(arr)

    for i in range(length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [90, 8, 56, 4, 55, 543, 876, 1034, 78]
print(bubble_sort(arr))


'''
O(logn) Time Complexity - 
                    This is the second most optimized or high time efficient algorithm after O(1)
                    Examples : Binary search

                    logic : The array/list will become half every time we do the operation 
                    Example : n -> n/2 -> n/4 -> n/8 ...... 1 which will also become n/2^0  -> n/2^1 -> n/2^2 ...... n/2^x => n = 2^x => log2n = x 
'''


