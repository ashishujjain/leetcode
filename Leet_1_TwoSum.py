""" 1. Two Sum
Easy
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109 """

from typing import List

class Leet_1_TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    def twopasshashtbale(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, num in enumerate(nums):
            numMap[num] = i
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        return []
    
    def onepasshashtbale(self, nums, target):
        numMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return [numMap[complement], i]
            numMap[num] = i
        return []
    
# Time Complexity is O(n2)
print (Leet_1_TwoSum().twoSum([2,7,11,15], 9))
print (Leet_1_TwoSum().twoSum([3,2,4], 6))
print (Leet_1_TwoSum().twoSum([3,3], 6))

print ("# twopasshashtbale Time complexity is O(n)")
# twopasshashtbale Time complexity is O(n)
print (Leet_1_TwoSum().twopasshashtbale([2,7,11,15], 9))
print (Leet_1_TwoSum().twopasshashtbale([3,2,4], 6))
print (Leet_1_TwoSum().twopasshashtbale([3,3], 6))

print ("# onepasshashtbale Time complexity is O(n)")
# onepasshashtbale Time complexity is O(n)
print (Leet_1_TwoSum().onepasshashtbale([2,7,11,15], 9))
print (Leet_1_TwoSum().onepasshashtbale([3,2,4], 6))
print (Leet_1_TwoSum().onepasshashtbale([3,3], 6))

# https://medium.com/@AlexanderObregon/solving-the-two-sum-problem-on-leetcode-python-answer-s-walkthrough-f0c737fb3648
