from typing import List
'''
Linear search : It searches the elemnent one by one.
        How it works :
            * It goes through the element one by one from the start
            * compare each value to check if it is equal to value we are looking for
            * if the value found return the index of that value
            * if it is not found then return -1

        To implement liner search we need:
            * an array with values to search through
            * a target value to search for
            * a loop that goes through array from start to end
            * if statement that compares the values target value if it is equal then return the index
            * if not then return -1
'''
def search_element(nums: List[int], target: int) -> int:
    for i in range(0, len(nums)):
        if nums[i] == target:
            return i
    return -1

print("Searching the element using Linear search:", search_element([4, 6, 7, 8, 9, 45, 2], 2))