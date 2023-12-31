# Given an array of integers nums, 
# a lucky integer is an integer which has a frequency in the array equal to its value.
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
# Example 1:
# Input: nums = [2,2,3,4]					
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:
# Input: nums = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

# Dylan's solution
from collections import Counter
def solution(arr):
    arr2 = Counter(arr)
    lucky_numbers = [val for key, val in arr2.items() if val == key]
    return -1 if len(lucky_numbers) == 0 else max(lucky_numbers)

print(solution([2,2,3,4]))


def solution(arr):
    lucky=[]
    for n in arr:
        if arr.count(n)==n:
            lucky.append(n)
    if lucky:
        return max(lucky)
    return -1