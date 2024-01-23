""" 198. House Robber
https://leetcode.com/problems/house-robber/description/

https://www.youtube.com/watch?v=73r3KWiEvyk
https://www.youtube.com/watch?v=VXqUQYGMnQg&t=676s


Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.


Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400 """


from typing import List


class Leet_198_HouseRobber:
    def rob(self, nums: List[int]) -> int:
        print(f"Nums = {nums}")
        rob1 = rob2 = 0
        # [rob1, rob2, n, n+1, n+2, ........]
        for n in nums: # iterate over house
            #print ("house has money:", n)
            temp = max (n + rob1, rob2)
            #print ("temp:", temp)
            rob1, rob2 = rob2, temp
        #return rob2
        return max(rob1, rob2)
    
    def rob_1(self, nums: List[int]) -> int:
        print(f"Nums = {nums}")
        length_nums = len(nums)
        if length_nums < 2:
            return nums[0]
        loot = []
        #print (nums[0])
        loot.insert(0,nums[0])
        loot.insert(1,max(nums[0],nums[1]))
        print(f"loot = {loot}")
        for i in range(length_nums):
            if i == 0 or i == 1:
                continue
            loot.insert(i,max(loot[i-2]+nums[i], loot[i-1]))
        print(f"loot = {loot}")
        return loot[length_nums-1] # subtract 1 to get the last index


#print(Leet_198_HouseRobber().rob([1,2,3,1]))
##print(Leet_198_HouseRobber().rob([2,7,9,3,1]))
print(Leet_198_HouseRobber().rob([2,7,3,1,4,2,1,8]))

#print(Leet_198_HouseRobber().rob_1([1,2,3,1]))
#print(Leet_198_HouseRobber().rob_1([2,7,9,3,1]))
print(Leet_198_HouseRobber().rob_1([2,7,3,1,4,2,1,8]))
