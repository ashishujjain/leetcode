""" 
https://leetcode.com/problems/decode-string/description/
https://www.geeksforgeeks.org/decode-string-recursively-encoded-count-followed-substring/

https://www.youtube.com/watch?v=qB0zZpBJlh8
https://www.youtube.com/watch?v=E9qHRcQXmDk&t=715s


394. Decode String
Medium

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"

Example 2:
    Input: s = "3[a2[c]]"
    Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:
    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() # pop the opening bracket

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)

        return "".join(stack)
    

if __name__ == "__main__":
    print (Solution().decodeString("3[a]2[bc]"))
    print (Solution().decodeString("3[a2[c]]"))
    print (Solution().decodeString("2[abc]3[cd]ef"))
    print (Solution().decodeString("54[ab6[cd]]"))
    print (Solution().decodeString("2[a3[c2[x]]y]"))