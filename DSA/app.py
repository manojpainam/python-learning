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
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return - 1

arr = [1, 5, 6, 7, 99, 100, 456, 789, 990]
print("Element found at index :", binary_search(arr, 789))


'''
O(nlogn) Time Complexity -
                    This is also Divide and conqure techiniques
                    Examples : Merge sort, Heap sort, Quick sort,

                    This is better than the O(n^2) time complexity
'''

'''
O(2^n) Time complexity -
                This is also called as the exponential time complexity
                Examples - Recursion (Brute force)
                This a not a good time complexity
'''

'''
O(n!) Time Complexity -
                This is used to solve the problems via brute-force approach
                Examples : n queens, Knights tours, strig -> all possibile permutations
                This is even worse time complexity even then the O(2"n)
                it will go on like this n * (n - 1) * (n-2) * ...... * 3 * 2 * 1
'''

'''
Bubble sort algorithm
'''

# Sorts the list using the Bubble Sort algorithm
def bubble_sorting(nums):
    # Each pass moves the largest unsorted element to the end.
    for i in range(len(nums) - 1):
        swapped = False

        # Compare adjacent elements in the unsorted portion.
        for j in range(len(nums) - i - 1): #exclude the last element '-i' as they were already sorted
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        # Stop early if no swaps were made.
        if not swapped:
            break

    return nums


nums = [895, 789, 534, 93, 90, 89, 67, 56, 56, 4, 1]
#print("Sorted list is:", bubble_sorting(nums))


'''
Selection sort algorithm
'''
def selection_sort(nums):  # Time Complexity: O(n²)
    # Move the boundary of the sorted and unsorted portions.
    for i in range(len(nums) - 1):

        # Assume the first element in the unsorted portion is the smallest.
        min_index = i

        # Find the index of the smallest element in the remaining unsorted portion.
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        # Place the smallest element at the beginning of the unsorted portion.
        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums

#print("Selection sort:", selection_sort(nums))


'''
Insertion sort
'''
def insertion_sort(nums):
    # Start from the second element since the first element
    # is considered to be already sorted.
    for i in range(1, len(nums)):

        # Store the current element to be inserted into
        # the correct position in the sorted portion.
        current = nums[i]

        # Start comparing with the previous element.
        previous = i - 1

        # Shift all elements greater than 'current'
        # one position to the right.
        while previous >= 0 and nums[previous] > current:
            nums[previous + 1] = nums[previous]
            previous -= 1

        # Insert the current element into its correct position.
        nums[previous + 1] = current

    return nums

print("Insertion Sort:", insertion_sort(nums))


'''
Linear serach : it will compare the each element with the other
'''
def liner_search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            return i
    return -1

list = [1, 89, 10, 45, 77, 65]
n = 65

result = liner_search(list, n)
if result != -1:
    print("Element found at index :", result)
else:
    print("Element not found")

def binarySearch(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = low + high // 2

        if list[mid] == target:
            return mid
        
        #narrow down search area
        if list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


'''
List and arrays - this is good for the lower data sets and also it has the lesser time complexity
'''
def get_lowest_from_list(arr):
    lowest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < lowest:
            lowest = arr[i]
    
    return lowest

print("Lowest number", get_lowest_from_list(nums))

'''
Stacks -
    Stack is a linear data structue in python that follows - Last In First Out (LIFO)
    The element which got added at the last will get removed first
    Operations - 
            push - add a new element on the stack
            pop - remove and return top element from the stack
            peek - returns the top element of the stack
            isEmpty - check if the stack is empty
            size - finds the size of the stack
'''
#push
nums.append(809)

print(nums)

#pop
nums.pop()

#peek
nums[-1]

print(nums)

#isempty
print(not bool(nums))

#size
print(len(nums))

