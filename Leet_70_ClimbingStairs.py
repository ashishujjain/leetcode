""" 70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/description/

https://www.youtube.com/watch?v=UUaMrNOvSqg
https://www.youtube.com/watch?v=Y0lT9Fck7qI


Easy


Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45 """

class Leet_70_ClimbingStairs:
    def climbStairs(self, n: int) -> int:
        if n ==1: return 1
        one, two = 1, 1
        for i in range (n-1):
            temp = one
            one = one + two
            two = temp
        return one

print (Leet_70_ClimbingStairs().climbStairs(5))
print (Leet_70_ClimbingStairs().climbStairs(2))
print (Leet_70_ClimbingStairs().climbStairs(3))
print (Leet_70_ClimbingStairs().climbStairs(1))
print (Leet_70_ClimbingStairs().climbStairs(8))

