""" 
https://leetcode.com/problems/valid-parentheses/description/
LeetCode 20. valid-parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'. """


class Leet_20_ValidParentheses:
    def isValidParentheses(self, s: str) -> bool:
        #Define empty array list
        stack = []
        #Define a dictonary with the closing bracket as key and opening bracket as value
        closeToOpen = {")" : "(", "]" : "[", "}" : "{" }

        #for every bracket in the string we have the check the condition
        for c in s:
            # Check the string character is present in key, if so
            if c in closeToOpen:
                # Validate the last entered value in stack and compare with closeToopen key value and if matched pop is out from stack
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                #append to the stack
                stack.append(c)
        #Return true if stack is empty, else False
        return True if not stack else False
    

if __name__=="__main__":
    print (Leet_20_ValidParentheses().isValidParentheses("()"))
    print (Leet_20_ValidParentheses().isValidParentheses("()[]{}"))
    print (Leet_20_ValidParentheses().isValidParentheses("(]"))