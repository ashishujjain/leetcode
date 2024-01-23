""" 213. House Robber II

https://leetcode.com/problems/house-robber-ii/description/

https://www.youtube.com/watch?v=rWAJCfYYOvM
https://www.youtube.com/watch?v=ucmqYGVGQK8&t=337s
Medium

Hint
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3 """


from typing import List
class Leet_213_HouseRobberII:
    def rob(self, nums: List[int]) -> int:
        print (f"nums = {nums}")
        skipfirst=nums[1:]
        print (f"skipfirst = {skipfirst}")
        skiplast=nums[:-1]
        print (f"skiplast = {skiplast}")
        return max(nums[0], self.rob_helper(skiplast), self.rob_helper(skipfirst))

    def rob_helper(self, nums: List[int]) -> int:
        rob1 = rob2 = 0
        # [rob1, rob2, n, n+1, n+2, ........]
        for n in nums:
            #print ("house has money:", n)
            temp = max (n + rob1, rob2)
            #print ("temp:", temp)
            rob1, rob2 = rob2, temp
        #return rob2
        return max(rob1, rob2)


print(Leet_213_HouseRobberII().rob([2,3,2]))
print(Leet_213_HouseRobberII().rob([1,2,3,1]))
print(Leet_213_HouseRobberII().rob([1,2,3]))
print(Leet_213_HouseRobberII().rob([1]))