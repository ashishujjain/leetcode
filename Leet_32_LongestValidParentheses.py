""" 32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".


Example 3:
Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'. 

"""

class leet32LongestValidParenteses:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]   # Mystery!!! To get the current length of the string: Consider case "(()())"
        longest = 0
        for i, n in enumerate(s):
            if n == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    longest = max(longest, i - stack[-1])
                else:
                    stack.append(i)

        return longest
    
print (leet32LongestValidParenteses().longestValidParentheses("(()"))
print (leet32LongestValidParenteses().longestValidParentheses(")()())"))
print (leet32LongestValidParenteses().longestValidParentheses(""))
        