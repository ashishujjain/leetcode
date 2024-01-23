""" 921. Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

youtube: https://www.youtube.com/watch?v=LzcyBJRMhSw


A parentheses string is valid if and only if:

It is the empty string, It can be written as AB (A concatenated with B), where A and B are valid strings, or It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

Example 1:
    Input: s = "())"
    Output: 1

Example 2:
    Input: s = "((("
    Output: 3 
"""

from inspect import stack

class MinAddToMakeValid:
    def minAddToMakeValid(self, s: str) -> int:
        print (f"String = {s}")
        stack = []
        for c in s:
            if c == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
        return len(stack)
    
    def minAddToMakereplace(self, s: str) -> int:
        print (f"String = {s}")
        while "()" in s:
            s = s.replace("()", "")
            print(f"String present {s}")
        return len(s)
    
    def minAddToMakeValid_pointer(self, s: str) -> int:
        print (f"String = {s}")
        l_count = r_count = added = 0 
        for char in s:
            if char == "(":
                l_count += 1
            else:
                if r_count < l_count:
                    r_count += 1
                else:
                    added += 1
        added += l_count - r_count
        return added
    
    def minAddToMakeValid_pointer1(self, s: str) -> int:
        print (f"String = {s}")
        l_count = r_count = 0
        for char in s:
            if char == "(":
                r_count += 1
            elif r_count > 0:
                r_count -= 1
            else:
                l_count += 1
        return l_count + r_count
    

print (MinAddToMakeValid().minAddToMakeValid("())"))
print (MinAddToMakeValid().minAddToMakeValid("((("))
print (MinAddToMakeValid().minAddToMakeValid("abc"))
print (MinAddToMakeValid().minAddToMakeValid("()"))
print (MinAddToMakeValid().minAddToMakeValid("()))(("))
print (MinAddToMakeValid().minAddToMakeValid("((()"))
print ("====================================================")
print (MinAddToMakeValid().minAddToMakeValid_pointer("())"))
print (MinAddToMakeValid().minAddToMakeValid_pointer("((("))
print (MinAddToMakeValid().minAddToMakeValid_pointer("abc"))
print (MinAddToMakeValid().minAddToMakeValid_pointer("()"))
print (MinAddToMakeValid().minAddToMakeValid_pointer("()))(("))
print (MinAddToMakeValid().minAddToMakeValid_pointer("((()"))
print ("====================================================")
print (MinAddToMakeValid().minAddToMakereplace("())"))
print (MinAddToMakeValid().minAddToMakereplace("((("))
print (MinAddToMakeValid().minAddToMakereplace("abc"))
print (MinAddToMakeValid().minAddToMakereplace("()"))
print (MinAddToMakeValid().minAddToMakereplace("()))(("))
print (MinAddToMakeValid().minAddToMakereplace("((()"))
print ("====================================================")
print (MinAddToMakeValid().minAddToMakeValid_pointer1("())"))
print (MinAddToMakeValid().minAddToMakeValid_pointer1("((("))
print (MinAddToMakeValid().minAddToMakeValid_pointer1("abc"))
print (MinAddToMakeValid().minAddToMakeValid_pointer1("()"))
print (MinAddToMakeValid().minAddToMakeValid_pointer1("()))(("))
print (MinAddToMakeValid().minAddToMakeValid_pointer1("((()"))
#print (MinAddToMakeValid().minAddToMakeValid_pointer1("][]["))