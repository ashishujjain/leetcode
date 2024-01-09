""" 
https://www.youtube.com/watch?v=jzZsG8n2R9A
https://leetcode.com/problems/3sum/description/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105 """

from typing import List

class ThreesumLeetcode15:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() # Sorting is good refer TwoSum|| for reasons, Sorting helps to eleminate the duplicates.
        # Using TwoSum2 logic to solve the problem
        for index, value in enumerate(nums): #iterate over the list and get the index and value
            if index > 0 and value == nums[index - 1]: # we don't want to the use the same value in the same position twice.
                continue # checking for index to be greater than zero and compare the value and value at the index -1, if same continue.
            # Solve via TwoSum2
            leftPointer , rightPointer = index + 1, len(nums) - 1 # here we are taking TwoSum2 login of defining the pointers.
            while leftPointer < rightPointer:
                threeSum = value + nums[leftPointer] + nums [rightPointer] # here we have taken the value from the for loop.
                if threeSum > 0:
                    rightPointer -= 1 # decrement the pointer
                elif threeSum < 0:
                    leftPointer += 1 # increment the pointer
                else:
                    result.append([value, nums[leftPointer], nums[rightPointer]]) #storing value in the result array.
                    leftPointer += 1 # Incrementing the leftpointer
                    while nums[leftPointer] == nums[leftPointer -1] and leftPointer < rightPointer: # checking the duplicate value and incremeting the leftpointer
                        leftPointer +=1
        return result

print (ThreesumLeetcode15().threeSum([-1,0,1,2,-1,-4]))
print (ThreesumLeetcode15().threeSum([0,1,1]))
print (ThreesumLeetcode15().threeSum([0,0,0]))
