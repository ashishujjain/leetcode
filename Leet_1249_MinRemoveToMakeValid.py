""" 1249. Minimum Remove to Make Valid Parentheses
https://www.youtube.com/watch?v=q_nOlpy_VSo
https://www.youtube.com/watch?v=sClFsx12VgM


Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter. """


class MinRemoveToMakeValid:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        N = len(s)
        S = list(s)
        for i in range(N):
            if S[i] == "(":
                stack.append(i)
            elif S[i] == ")":
                if stack:
                    stack.pop()
                else:
                    S[i] = ""
        #stack of ( index pop of
        for j in stack:
            S[j] = ""
        return "".join(S)
    
    def minRemoveToMakeStack(self, s: str) -> str:
        stack, opened, closed = [], 0 ,0
        for c in s:
            if c == "(":
                opened += 1
                stack.append(c)
            elif c == ')':
                if closed < opened:
                    closed += 1
                    stack.append(c)
            else:
                stack.append(c)
        res, opened, closed = "", 0 ,0
        while stack:
            c = stack.pop()
            if c == '(':
                if opened < closed:
                    opened += 1
                    res += c
            elif c == ')':
                closed += 1
                res += c
            else:
                res += c
        return res
    
    def minRemoveToMakeValid_1(self, s: str) -> str:
        stack = []
        final = list(s)
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    final[i] = ''
        for index in stack:
            final[index] = ''
        return ''.join(final)


print (MinRemoveToMakeValid().minRemoveToMakeValid("lee(t(c)o)de)"))
print (MinRemoveToMakeValid().minRemoveToMakeValid_1("lee(t(c)o)de)"))
print (MinRemoveToMakeValid().minRemoveToMakeStack("lee(t(c)o)de)"))
print ("=======================================================")
print (MinRemoveToMakeValid().minRemoveToMakeValid("a)b(c)d"))
print (MinRemoveToMakeValid().minRemoveToMakeValid_1("a)b(c)d"))
print (MinRemoveToMakeValid().minRemoveToMakeStack("a)b(c)d"))
print ("=======================================================")
print (MinRemoveToMakeValid().minRemoveToMakeValid("))(("))
print (MinRemoveToMakeValid().minRemoveToMakeValid_1("))(("))
print (MinRemoveToMakeValid().minRemoveToMakeStack("))(("))

