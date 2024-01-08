""" 
53. Maximum Subarray Kadane's Algorithm
https://leetcode.com/problems/maximum-subarray/description/
https://www.youtube.com/watch?v=5WZl3MMT0Eg

Medium

Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104 """


from typing import List


class Leet_53_MaximumSubarray_Kadanes_Algorithm:
    def maxSubArray_Kadanes_Algorithm(self, nums: List[int]) -> int:
        print ("")
        print (f"Provided array is {nums}.")
        maxSum = nums[0]
        curSum = 0
        maxL, maxR = 0, 0
        L = 0
        for R in range(len(nums)):
            if curSum < 0:
                curSum = 0
                L = R
            curSum += nums[R]
            if curSum > maxSum:
                maxSum = curSum
                maxL, maxR = L, R
        return ([maxL, maxR], nums[maxL:maxR+1], maxSum)
    
    def maxSubArray(self, nums: List[int]) -> int: # Sliding window technique
        print ("")
        print (f"Provided array is {nums}.")
        maxSub_Array = nums[0] # starts with the First element
        currentSum = 0 # Set a curSum variable
        for R in range(len(nums)): # iterate over the List
            if currentSum < 0:  # if curSum is negative discard the previous negative prefix value and set CurSum = 0
                currentSum = 0
            currentSum += nums[R] # Keep adding the values from the list
            maxSub_Array = max(maxSub_Array, currentSum) # max is required if you get the max midway of the list and later additions are small.
        return (maxSub_Array)                


print (Leet_53_MaximumSubarray_Kadanes_Algorithm().maxSubArray_Kadanes_Algorithm([-2,1,-3,4,-1,2,1,-5,4]))
print (Leet_53_MaximumSubarray_Kadanes_Algorithm().maxSubArray_Kadanes_Algorithm([1]))
print (Leet_53_MaximumSubarray_Kadanes_Algorithm().maxSubArray_Kadanes_Algorithm([5,4,-1,7,8]))


print (Leet_53_MaximumSubarray_Kadanes_Algorithm().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print (Leet_53_MaximumSubarray_Kadanes_Algorithm().maxSubArray([1]))
print (Leet_53_MaximumSubarray_Kadanes_Algorithm().maxSubArray([5,4,-1,7,8]))