from typing import List


#boyer moore voting algorithm
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

print("Majority elelemt :", majorityElement([3, 4, 3, 4]))

def is_ugly(n):
    if n <= 0:
        return False
    for i in [2, 3, 5]:
        while n % i == 0:
            n //= i
    return n == 1

print("Ugly number :", is_ugly(8))


def maximum69Number (num: int) -> int:
    max = num
    modified_num = str(num)

    for i in range(len(str(modified_num))):
        if modified_num[i] == str(6):
            modified_num = modified_num[:i] + str(9) + modified_num[i+1:len(modified_num)]
        elif modified_num[i] == str(9):
            modified_num = modified_num[:i] + str(6) + modified_num[i+1:len(modified_num)]
            
        if int(modified_num) > int(max):
            max = modified_num
        modified_num = str(num)

    return int(max)

print("maxmim number ", maximum69Number(9669))



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

print("Adding strings : ", addStrings("89", "67"))



def findLucky(self, arr: List[int]) -> int:
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