from typing import List


# ------------------------------------------------------------
# Problem 1: Majority Element
#
# Given an integer array nums of size n, return the majority
# element.
#
# The majority element is the element that appears more than
# ⌊n / 2⌋ times. You may assume that the majority element
# always exists in the array.
#
# Example:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
# ------------------------------------------------------------

# Boyer-Moore Voting Algorithm
def majorityElement(nums: List[int]) -> int:
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

print("Majority element:", majorityElement([3, 4, 3, 4]))


# ------------------------------------------------------------
# Problem 2: Ugly Number
#
# An ugly number is a positive integer whose prime factors
# are limited to 2, 3, and 5.
#
# Given an integer n, return True if n is an ugly number.
# Otherwise, return False.
#
# Example:
# Input: n = 8
# Output: True
# ------------------------------------------------------------

def is_ugly(n):
    if n <= 0:
        return False

    for i in [2, 3, 5]:
        while n % i == 0:
            n //= i

    return n == 1

print("Ugly number:", is_ugly(8))


# ------------------------------------------------------------
# Problem 3: Maximum 69 Number
#
# You are given a positive integer consisting only of digits
# 6 and 9.
#
# Return the maximum number you can get by changing at most
# one digit (6 to 9 or 9 to 6).
#
# Example:
# Input: 9669
# Output: 9969
# ------------------------------------------------------------

def maximum69Number(num: int) -> int:
    max = num
    modified_num = str(num)

    for i in range(len(str(modified_num))):
        if modified_num[i] == str(6):
            modified_num = modified_num[:i] + str(9) + modified_num[i + 1:]
        elif modified_num[i] == str(9):
            modified_num = modified_num[:i] + str(6) + modified_num[i + 1:]

        if int(modified_num) > int(max):
            max = modified_num

        modified_num = str(num)

    return int(max)

print("Maximum number:", maximum69Number(9669))


# ------------------------------------------------------------
# Problem 4: Add Strings
#
# Given two non-negative integers represented as strings,
# return their sum as a string.
#
# You must not convert the inputs directly into integers or
# use any built-in BigInteger library.
#
# Example:
# Input: num1 = "89", num2 = "67"
# Output: "156"
# ------------------------------------------------------------

def addStrings(num1: str, num2: str) -> str:
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
        digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0

        total = digit1 + digit2 + carry

        result.append(str(total % 10))
        carry = total // 10

        i -= 1
        j -= 1

    return "".join(result[::-1])

print("Adding strings:", addStrings("89", "67"))


# ------------------------------------------------------------
# Problem 5: Find Lucky Integer in an Array
#
# A lucky integer is an integer whose value is equal to its
# frequency in the array.
#
# Return the largest lucky integer. If no lucky integer
# exists, return -1.
#
# Example:
# Input: [2,2,3,4]
# Output: 2
# ------------------------------------------------------------

def findLucky(arr: List[int]) -> int:
    freq = {}

    # Count frequencies
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    lucky = -1

    # Find the largest lucky number
    for num, count in freq.items():
        if num == count:
            lucky = max(lucky, num)

    return lucky

print("Lucky number:", findLucky([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))

def removeElement(nums: List[int], val: int) -> int:
    """
    Removes all occurrences of val from the array in-place.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    write = 0

    for num in nums:
        if num != val:
            nums[write] = num
            write += 1

    return write


# Example Usage
nums = [0, 1, 2, 2, 3, 0, 4, 2]
print("Remove element :", removeElement(nums, 2))


"""
LeetCode 389. Find the Difference

Given two strings `s` and `t`, where `t` is formed by shuffling `s` and adding one extra character, return the extra character.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def findTheDifference(s: str, t: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            if ch not in freq or freq[ch] == 0:
                return ch
            freq[ch] -= 1

print("Extra digit in charas : ", findTheDifference("litmn", "litmjn"))


"""
LeetCode 136. Single Number

Problem Statement:
Given a non-empty array of integers `nums`, every element appears exactly
twice except for one element, which appears only once. Find and return
that single element.

You must implement a solution with:
- O(n) time complexity
- O(1) extra space

Examples:
Input: nums = [2, 2, 1]
Output: 1

Input: nums = [4, 1, 2, 1, 2]
Output: 4

Input: nums = [1]
Output: 1

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Every element appears exactly twice except for one.

Approach:
- Initialize a variable `result` to 0.
- Traverse the array and XOR each element with `result`.
- Since:
    a ^ a = 0
    a ^ 0 = a
  all duplicate numbers cancel each other out, leaving only the
  number that appears once.

Time Complexity: O(n)
Space Complexity: O(1)
"""
def singleNumber(nums: List[int]) -> int:
    result = 0

    for num in nums:
        result ^= num

    return result

print("single number : ", singleNumber([4, 1, 2, 1, 2]))


"""
LeetCode 290. Word Pattern

Problem Statement:
Given a pattern and a string s, determine if s follows the same pattern.

Here, "follow" means there is a one-to-one mapping (bijection) between a
character in pattern and a non-empty word in s.

Rules:
1. Each character must map to exactly one word.
2. No two different characters can map to the same word.
3. The number of characters in pattern must equal the number of words in s.

Example 1:
Input:  pattern = "abba", s = "dog cat cat dog"
Output: True

Example 2:
Input:  pattern = "abba", s = "dog cat cat fish"
Output: False

Example 3:
Input:  pattern = "aaaa", s = "dog cat cat dog"
Output: False

Time Complexity: O(n²)
- Checking `word in mapping.values()` takes O(n) in the worst case.

Space Complexity: O(n)
- Stores at most one mapping for each unique character.
"""

def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()

    # Number of pattern characters and words must match.
    if len(pattern) != len(words):
        return False

    mapping = {}

    for i in range(len(pattern)):
        char = pattern[i]
        word = words[i]

        # Existing character must map to the same word.
        if char in mapping:
            if mapping[char] != word:
                return False
        else:
            # Prevent two different characters from mapping to the same word.
            if word in mapping.values():
                return False

            mapping[char] = word

    return True

print("word pattern:", wordPattern("abba", "dog cat cat dog"))

"""
LeetCode 278. First Bad Version

Problem Statement:
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.

Since each version is developed based on the previous version, all versions after
a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find the first bad one,
which causes all the following versions to be bad.

You are given an API:

    isBadVersion(version)

which returns:
- True if the version is bad.
- False otherwise.

Your task is to find the first bad version while minimizing the number of calls
to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4

Explanation:
Version 1 -> Good
Version 2 -> Good
Version 3 -> Good
Version 4 -> Bad
Version 5 -> Bad

The first bad version is 4.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:
- 1 <= bad <= n <= 2^31 - 1

Approach:
- The versions form a sorted (monotonic) sequence:
      Good Good Good Bad Bad Bad
- Use Binary Search to find the boundary where versions change
  from good to bad.
- If mid is bad, the first bad version is either mid or before it,
  so search the left half.
- Otherwise, search the right half.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

first_bad = 4

def isBadVersion(version):
    return version >= first_bad

def firstBadVersion(n: int) -> int:
    left = 1
    right = n

    while left < right:
        mid = left + (right - left) // 2

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left

print("Fetch the first bad numbers :", firstBadVersion(5))


"""
LeetCode 268 - Missing Number

Problem Statement:
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`,
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3, 0, 1]
Output: 2

Example 2:
Input: nums = [0, 1]
Output: 2

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8

Constraints:
- n == len(nums)
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All the numbers in nums are unique.

Follow-up:
Can you solve it using:
1. O(n) time and O(1) extra space?
2. A mathematical formula or bit manipulation?
"""
def missing_number(nums: List[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

print("Missing sum:", missing_number([0, 3, 2, 6, 4, 1]))