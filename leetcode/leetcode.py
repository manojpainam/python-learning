from typing import List
from collections import Counter


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


"""
LeetCode 205. Isomorphic Strings

Problem Statement:
Given two strings `s` and `t`, determine if they are isomorphic.

Two strings are isomorphic if the characters in `s` can be replaced to get `t`.

Rules:
1. Every character in `s` must map to exactly one character in `t`.
2. No two different characters in `s` can map to the same character in `t`.
3. A character can map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: True

Explanation:
e -> a
g -> d

The mapping is one-to-one, so the strings are isomorphic.

Example 2:
Input: s = "foo", t = "bar"
Output: False

Explanation:
'o' first maps to 'a', but later should map to 'r', which is not allowed.

Example 3:
Input: s = "paper", t = "title"
Output: True

Constraints:
- 1 <= s.length <= 5 * 10^4
- t.length == s.length
- s and t consist of any valid ASCII character.

Solution:
"""


def isIsomorphic(s: str, t: str) -> bool:
    # If the lengths are different, they cannot be isomorphic.
    if len(s) != len(t):
        return False

    # Dictionary to store mapping from s -> t
    s_to_t = {}

    # Dictionary to store reverse mapping from t -> s
    t_to_s = {}

    # Traverse both strings simultaneously.
    for c1, c2 in zip(s, t):

        # Check if c1 already has a mapping.
        if c1 in s_to_t:
            if s_to_t[c1] != c2:
                return False
        else:
            s_to_t[c1] = c2

        # Check if c2 already has a reverse mapping.
        if c2 in t_to_s:
            if t_to_s[c2] != c1:
                return False
        else:
            t_to_s[c2] = c1

    return True

print("Check isIsomorphic:" , isIsomorphic("add", "egg"))

'''
You are playing the following Nim Game with your friend:

Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

 

Example 1:

Input: n = 4
Output: false
Explanation: These are the possible outcomes:
1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
In all outcomes, your friend wins.
Example 2:

Input: n = 1
Output: true
Example 3:

Input: n = 2
Output: true
'''
def can_win_nim(n: int) -> bool:
    #Approach if the number multiple of 4 you will loose for sure
    return n % 4 != 0

print("can win nim:", can_win_nim(3))


'''
You are given a positive integer n.

Return the maximum product of any two digits in n.

Note: You may use the same digit twice if it appears more than once in n.

 

Example 1:

Input: n = 31

Output: 3

Explanation:

The digits of n are [3, 1].
The possible products of any two digits are: 3 * 1 = 3.
The maximum product is 3.
Example 2:

Input: n = 22

Output: 4

Explanation:

The digits of n are [2, 2].
The possible products of any two digits are: 2 * 2 = 4.
The maximum product is 4.
Example 3:

Input: n = 124

Output: 8

Explanation:

The digits of n are [1, 2, 4].
The possible products of any two digits are: 1 * 2 = 2, 1 * 4 = 4, 2 * 4 = 8.
The maximum product is 8.
'''
def maxProduct(n: int) -> int:
    max_product = 0
    str_num = str(n)

    for i in range(len(str_num)):
        for j in range(i+1, len(str_num)):
            product = int(str_num[i]) * int(str_num[j])
            if product > max_product:
                max_product = product

    return max_product

print("max_product", maxProduct(124))


'''
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

Note: January 1, 1971 was a Friday.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
'''

def day_of_the_week(day: int, month: int, year: int) -> str:
    weekdays = [
            "Friday",
            "Saturday",
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday"
        ]

    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

    def isLeap(year):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    total_days = 0

    # Count days for complete years
    for y in range(1971, year):
        total_days += 366 if isLeap(y) else 365

    # Count days for complete months
    for m in range(month - 1):
        total_days += month_days[m]
        if m == 1 and isLeap(year):   # February
            total_days += 1

    # Count days in current month
    total_days += day - 1

    return weekdays[total_days % 7]


print("Day is :", day_of_the_week(31, 12, 2025))

'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''
def binary_search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

nums = [-1, 2, 3, 4, 5, 6, 9, 25]
print("9 is at index:", binary_search(nums, 9))


'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"
 

Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
'''
def to_lower_case(s: str) -> str:
    result = []

    for char in s:
        if 'A' <= char <= 'Z':
            result.append(chr(ord(char) + 32))
        else:
            result.append(char)

    return "".join(result)

print("To lower case:", to_lower_case("HELLO"))

'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:
    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.
'''

def can_construct(ransomNote: str, maganize: str) -> bool:
    mapping = {}

    for char in maganize:
        mapping[char] = mapping.get(char, 0) + 1

    for char in ransomNote:
        if mapping.get(char, 0) == 0:
            return False
        mapping[char] -= 1

    return True

print("Can construct the word:", can_construct("aab", "baa"))


'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
'''

def merge(nums1, m, nums2, n):
    i = m - 1          # last valid element in nums1
    j = n - 1          # last element in nums2
    k = m + n - 1      # last position in nums1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)

print(nums1)

'''
###Search insert postion###
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''

def search_insert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left

print("Insert postion is :", search_insert([1, 2, 4, 5, 6], 3))


'''
###contains dupliactes###
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

def contains_duplicates(nums: List[int]) -> bool:
    #set len comparision
    return len(nums) != len(set(nums))

print("Contains dupliactes:", contains_duplicates([1, 2, 3, 4, 5, 4]))

'''
###Longest common prefix###
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
'''

def longest_common_prefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ""
    return prefix

print("Longest prefix is : ", longest_common_prefix(["manoj", "mango", "mangrooves"]))


'''
###414. Third Maximum Number###
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
'''

def third_max_element(nums: List[int]) -> int:
    first = second = third = None

    for num in nums:
        if first == num or second == num or third == num:
            continue

        if first is None or num > first:
            third = second
            second = first
            first = num
        elif second is None or num > second:
            third = second
            second = num
        else:
            third = num

    return first if third is None else third

print("Third maximum element is :", third_max_element([-1,2,3]))


'''
###Reverse vowels### 
'''
def reverse_vowels(s: str) -> str:
    left, right = 0, len(s) - 1
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    s = list(s)

    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return "".join(s)

print("after reversing vowels is:", reverse_vowels("manoj"))

'''
###Best time to buy stcoks###
'''
def maxProfit(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit

print("Best time to buy stock is:", maxProfit([67, 89, 23, 45, 67, 88, 58, 96, 46]))

'''
###Max peoducts of three numbers###

Approach : find the last three indexes product or find product of first two negative numbers and then multiply with last element
'''

def three_max_product(nums: List[int]) -> int:
    nums.sort()
    max_product = nums[-3] * nums[-2] * nums[-1]
    max_product_1 = nums[-1] * nums[0] * nums[1]
    return max(max_product, max_product_1)

print("max product :", three_max_product([-100, -99, 1, 2, 4, 3]))


'''
###intersection####

Approach using the sets
'''
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1).intersection(set(nums2)))

print("Intersection of the numbers:", intersection([4,9,5], [9,4,9,8,4]))

'''
###contains dupliactes ||###
'''
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
        last_seen = {}

        for i, num in enumerate(nums):
            if num in last_seen:
                if i - last_seen[num] <= k:
                    return True

            last_seen[num] = i

        return False

print("containes duplicates || :", containsNearbyDuplicate([1,2,3,1], 3))

'''
###summary range###
'''
def summaryRanges(nums: List[int]) -> List[str]:
        result = []

        if not nums:
            return result

        start = nums[0]

        for i in range(1, len(nums)):
            # Current number is not consecutive
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i - 1]}")

                start = nums[i]

        # Add the final range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")

        return result

print("summary range:", summaryRanges([0,2,3,4,6,8,9]))

'''
###Find disappearing numbers###
'''
def findDisappearedNumbers(nums: List[int]) -> List[int]:
    n = len(nums)
    counts = [0] * (n + 1)

    for num in nums:
        counts[num] = 1

    return [i for i in range(1, n + 1) if counts[i] == 0]

print("Disappeared number is :", findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))

def search_single_element(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if mid % 2 == 1:
            mid -= 1

        if nums[mid] == nums[mid+1]:
            left = mid + 2
        else:
            right = mid
    return nums[left]

print("search single element:", search_single_element([1, 1, 2, 3, 3, 4, 4, 5, 5]))


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    merged_arr = nums1 + nums2
    merged_arr.sort()

    low = 0
    high = len(merged_arr) - 1

    mid = low + (high - low) // 2
    if len(merged_arr) % 2 == 0:
        return (merged_arr[mid] + merged_arr[mid+1]) / 2
    return merged_arr[mid]

print("midean of sorted arrays is :", findMedianSortedArrays([1, 2], [3, 4]))

def commonChars(words: List[str]) -> List[str]:
        common = Counter(words[0])

        for word in words[1:]:
            current = Counter(word)

            for char in common:
                common[char] = min(common[char], current[char])

        result = []

        for char, count in common.items():
            result.extend([char] * count)

        return result

print("common chars is :", commonChars(["bella","label","roller"]))