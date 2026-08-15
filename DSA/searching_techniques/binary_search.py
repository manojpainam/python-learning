from typing import List
'''
Binary search : Binary search seraches through a sorted array and returns the index of the value it searches for.
                Binary search is faster than the linear search but it requires a sorted array.

                it works by checking the value in center of the array. if target value is lower the next value to check is in the center of the left half of the array.
                this way of searching is always half of the previous search area and it is why binary search is fast.

                How it works:
                    # check value in center of array
                    # if target value is lower search left half. if target value is higher search right half.
                    # continue step 1 and step 2 for the new reduced part of the array until the target value is found or until the search area is empty
                    # if value found return its index if not return -1

                Implementing binary search alogorithm we need:
                    * an array with values to search thorugh
                    * a target value to search for
                    * a loop that runs as long as left index is less than or equal to the right index
                    * an if statement that compares the middle value with the target value and return its index if found
                    * an if statement that check if the target is less than the miidle value and updates the left or right varibales to narrow down search area
                    * after loop return -1. cause we know the value is not found
'''
def binary_search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return - 1

print("value found at index:", binary_search([3, 4, 5, 7, 8, 10, 19, 45], 19))


'''
leetcode : 367: Valid Perfect Square
'''
def is_valid_perfect_square(num: int) -> bool:
    low = 1
    high = num

    while low <= high:
        mid = (low + high) // 2

        if mid * mid == num:
            return True

        if mid * mid < num:
            low = mid + 1
        else:
            high = mid - 1

    return False

print("Number is a perfect square :", is_valid_perfect_square(26))


'''
Search through rotated array
'''
def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
print("search found at index : ", search([4,5,6,7,0,1,2], 0))
         