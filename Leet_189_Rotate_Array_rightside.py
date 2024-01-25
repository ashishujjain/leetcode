""" 189. Rotate Array
https://leetcode.com/problems/rotate-array/description/
https://www.youtube.com/watch?v=BHr381Guz3Y
https://www.youtube.com/watch?v=QOpU9-l5T7Y
https://www.youtube.com/watch?v=0-p-yzlWKUk
https://www.youtube.com/watch?v=ZNqWgwwpgLU
https://www.youtube.com/watch?v=viaha1SnpT4

Medium

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
    Explanation: 
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:
    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space? """

from typing import List
class Solution:

    def helper(self, nums: List[int], l, r: int):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l , r = l + 1, r -1
        return nums

    def rotateright(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print (f"Input Array : {nums} and rotate by {k}")
        k = k % len(nums)
        print (f"Rotate by {k}")
        Solution().helper(nums, 0, len(nums)-1)
        Solution().helper(nums, 0, k - 1)
        Solution().helper(nums, k, len(nums)-1)
        return nums
    
    def rotateleft(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #print (f"Input Array : {nums} and rotate left by {k}")
        k = k % len(nums)
        #print (f"Rotate by {k}")
        Solution().helper(nums, 0, k - 1)
        Solution().helper(nums, k, len(nums)-1)
        Solution().helper(nums, 0, len(nums)-1)
        return nums
    
    def rotateright1(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k = k % l
        n = l-k
        if n > 0:
            nums[:] = nums[n:] + nums[:n]
        return nums
    
    def rotateleft1(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k = k % l
        n = k
        if n > 0:
            nums[:] = nums[n:] + nums[:n]
        return nums
    
    def rotateright2(self, nums: List[int], k: int) -> None:
        if len(nums) < k:
            k = k % len(nums)
        last_k_elements = nums[-k:] # getting the last two element to a new list

        nums[k:] = nums[:-k] #move the array from starting to -k to k index.
        nums[:k] = last_k_elements # add the elements to the starting
        return nums
    
    def rotateleft2(self, nums: List[int], k: int) -> None:
        if len(nums) < k:
            k = k % len(nums)
        first_k_elements = nums[:k] # getting the last two element to a new list
        #print (first_k_elements)

        nums[:-k] = nums[k:] #move the array from starting to -k to k index.
        #nums[:] = nums[:] + first_k_elements # add the elements to the starting
        nums[-k:] = first_k_elements
        return nums

print (f"Output rotateright = {Solution().rotateright([1,2,3,4,5,6,7], 3)}")
print ("")
print (f"Output rotateright = {Solution().rotateright([-1,-100,3,99], 2)}")
print ("")
print (f"Output rotateright = {Solution().rotateright([1,2,3,4,5,6], 1)}")
print ("---------------------------------------------------")
print (f"Output rotateright1 = {Solution().rotateright1([1,2,3,4,5,6,7], 3)}")
print ("")
print (f"Output rotateright1 = {Solution().rotateright1([-1,-100,3,99], 2)}")
print ("")
print (f"Output rotateright1 = {Solution().rotateright1([1,2,3,4,5,6], 1)}")
print ("---------------------------------------------------")
print (f"Output rotateright2 = {Solution().rotateright2([1,2,3,4,5,6,7], 3)}")
print ("")
print (f"Output rotateright2 = {Solution().rotateright2([-1,-100,3,99], 2)}")
print ("")
print (f"Output rotateright2 = {Solution().rotateright2([1,2,3,4,5], 1)}")
print ("")
print ("---------------------------------------------------")
print (f"Output rotateleft2 = {Solution().rotateleft2([1,2,3,4,5], 1)}")
print ("")
print (f"Output rotateleft1 = {Solution().rotateleft1([1,2,3,4,5], 1)}")
print ("")
print (f"Output rotateleft = {Solution().rotateleft([1,2,3,4,5], 1)}")
print ("")
print (f"Output rotateleft2 = {Solution().rotateleft2([1,2,3,4,5,6,7], 2)}")
print ("")
print (f"Output rotateleft = {Solution().rotateleft([1,2,3,4,5,6,7], 2)}")
print ("")
print (f"Output rotateleft1 = {Solution().rotateleft1([1,2,3,4,5,6,7], 2)}")


        
        