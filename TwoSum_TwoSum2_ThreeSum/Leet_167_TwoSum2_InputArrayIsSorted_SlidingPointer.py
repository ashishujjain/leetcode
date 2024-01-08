""" 167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
https://www.youtube.com/watch?v=cQ1Oz4ckceM

Medium


Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution. """

from typing import List

class Leet_167_TwoSum2_InputArrayIsSorted:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        print ("")
        print (f"Provided array {numbers} and target is {target}.")
        numbers.sort()
        print (f"Sorted array {numbers} and target is {target}.")
        if len(numbers)==2:
            return[1,2]
        leftPointer , rightPointer = 0, len(numbers) - 1 # setting the leftPointer and rightPointer, leftPointer will start form zero and rightPointer is length of array -1
        while leftPointer < rightPointer: # check the condition for leftPointer and rightPointer
            curSum = numbers[leftPointer] +  numbers[rightPointer] # add the values based on index pointers

            if curSum > target: # if the curSum is greater than target
                rightPointer -=1 # reduce the rigthPointer by 1
            elif curSum < target:  # if the curSum is less than target
                leftPointer +=1 # increment the leftPointer by 1
            else:
                return [leftPointer + 1, rightPointer + 1] # return the leftPointer and right Pointer and add 1 to the index as nums index starts form 1, not from 0. This will be gauranteed solution.


print (Leet_167_TwoSum2_InputArrayIsSorted().twoSum([2,7,11,15], 9))
print (Leet_167_TwoSum2_InputArrayIsSorted().twoSum([3,2,4], 6))
print (Leet_167_TwoSum2_InputArrayIsSorted().twoSum([-1,0], -1))
print (Leet_167_TwoSum2_InputArrayIsSorted().twoSum([3,4,0], 3))
