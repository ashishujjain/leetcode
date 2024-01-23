""" 1963. Minimum Number of Swaps to Make the String Balanced
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

https://www.geeksforgeeks.org/minimum-swaps-to-balance-the-given-brackets-at-any-index/
https://www.geeksforgeeks.org/minimum-swaps-bracket-balancing/


https://www.youtube.com/watch?v=3YDBT9ZrfaU

Medium

Hint
You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced. 

Example 1:
    Input: s = "][]["
    Output: 1
    Explanation: You can make the string balanced by swapping index 0 with index 3.
    The resulting string is "[[]]".

Example 2:
    Input: s = "]]][[["
    Output: 2
    Explanation: You can do the following to make the string balanced:
    - Swap index 0 with index 4. s = "[]][][".
    - Swap index 1 with index 5. s = "[[][]]".
    The resulting string is "[[][]]".

Example 3:
    Input: s = "[]"
    Output: 0
    Explanation: The string is already balanced.

Example 4:
    input: s= “] ] ] ] [ ] [ [ [ [“
    Output: 2
    Explanation: first swap for brackets at position 2 and 5, second swap for brackets at position 0 and 7
 
Approach: 
    Given problem can be solved by iterating through the string and following the steps below:

    All the balanced brackets are removed as they do not require any swaps for balancing the string
    Since, the number of opening bracket ‘[‘ and closing bracket is same ‘]’, After removing balanced components , remaining string becomes like  ] ] ]…..[ [
    The optimal approach is to balance two sets of brackets in one swap
    For every two pairs of square brackets, a swap will make them balanced.
    If number of unbalanced pairs are odd, then one more swap is needed.
    If p is the number of unbalanced pairs then 
    
    minimum number of swaps = (p + 1) / 2 

Constraints:
    n == s.length
    2 <= n <= 106
    n is even.
    s[i] is either '[' or ']'.
    The number of opening brackets '[' equals n / 2, and the number of closing brackets ']' equals n / 2.
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        unbalancedPair = 0
        for i in range(len(s)) :
            if (unbalancedPair > 0 and s[i] == ']') :
                unbalancedPair -= 1
            elif (s[i] == '[') :
                unbalancedPair += 1
        return (unbalancedPair + 1) // 2
    
    def minSwaps_maxclose(self, s: str) -> int:
        close, maxclose = 0, 0
        for c in s:
            if c == '[':
                close -= 1
            else:
                close += 1
            maxclose = max(close, maxclose)
        return (maxclose + 1) // 2 # Floor division to return integer
    
    def minSwaps1(self, s: str) -> int:
        unbalancedPair = 0
        for c in s:
            if (unbalancedPair > 0 and c == ']') :
                unbalancedPair -= 1
            elif (c == '[') :
                unbalancedPair += 1
        return (unbalancedPair + 1) // 2
    
    def minSwaps2(self, s: str) -> int:
        unbalancedPair = 0
        for c in s:
            if c == '[' :
                unbalancedPair += 1
            elif unbalancedPair > 0 :
                unbalancedPair -= 1
        return (unbalancedPair + 1) // 2

if __name__ == "__main__" :
    s = "]]][[["
    print(Solution().minSwaps(s))
    print(Solution().minSwaps_maxclose(s))
    print(Solution().minSwaps1(s))
    print(Solution().minSwaps2(s))
    print ("======================================")
    s = "][]["
    print(Solution().minSwaps(s))
    print(Solution().minSwaps_maxclose(s))
    print(Solution().minSwaps1(s))
    print(Solution().minSwaps2(s))
    print ("======================================")
    s = "[]"
    print(Solution().minSwaps(s))
    print(Solution().minSwaps_maxclose(s))
    print(Solution().minSwaps1(s))
    print(Solution().minSwaps2(s))
    print ("======================================")
    s = "]]]][][[[["
    print(Solution().minSwaps(s))
    print(Solution().minSwaps_maxclose(s))
    print(Solution().minSwaps1(s))
    print(Solution().minSwaps2(s))
    print ("======================================")
    s = "]]]][[]][[[["
    print(Solution().minSwaps(s))
    print(Solution().minSwaps_maxclose(s))
    print(Solution().minSwaps1(s))
    print(Solution().minSwaps2(s))
