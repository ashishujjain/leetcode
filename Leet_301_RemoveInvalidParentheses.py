""" Leet_301_RemoveInvalidParentheses
https://www.youtube.com/watch?v=wtoNj0d-OEI&t=3s
https://www.youtube.com/watch?v=kAIklThnh-Q

https://www.geeksforgeeks.org/remove-invalid-parentheses/


Hard

Hint
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

Example 1:
    Input: s = "()())()"
    Output: ["(())()","()()()"]

Example 2:
    Input: s = "(a)())()"
    Output: ["(a())()","(a)()()"]

Example 3:
Input: s = ")("
Output: [""]
 
Constraints:
    1 <= s.length <= 25
    s consists of lowercase English letters and parentheses '(' and ')'.
    There will be at most 20 parentheses in s. 
"""

from typing import List
class Solution:
    # Method checks if character is parenthesis(open 
    # or closed) 
    def isParenthesis(self, c: str):
        #print (c)
        return ((c == '(') or (c == ')'))
    # method returns true if contains valid
    # parenthesis
    def isValidString(self, str: str):
        cnt = 0
        for i in range(len(str)):
            if (str[i] == '('):
                cnt += 1
            elif (str[i] == ')'):
                cnt -= 1
            if (cnt < 0):
                return False
        return (cnt == 0)
	
    # method to remove invalid parenthesis 
    #def removeInvalidParenthesis(str):
    #As we need to generate all possible output we will backtrack among all states by removing one opening or closing bracket and check if they are valid if invalid then add the removed bracket back and go for next state. We will use BFS for moving through states, use of BFS will assure removal of minimal number of brackets because we traverse into states level by level and each level corresponds to one extra bracket removal. Other than this BFS involve no recursion so overhead of passing parameters is also saved. Below code has a method isValidString to check validity of string, it counts open and closed parenthesis at each index ignoring non-parenthesis character. If at any instant count of close parenthesis becomes more than open then we return false else we keep update the count variable. 
    def removeInvalidParenthesis(self, str: str) -> List[str]:
        print (f"Provided string : {str}")
        if (len(str) == 0):
            return
        # visit set to ignore already visited 
        visit = set()
        # queue to maintain BFS
        q = []
        res = []
        temp = level =0
        # pushing given as starting node into queue
        q.append(str)
        visit.add(str)
        #print (f"Queue : {q} and Visit set : {visit}")
        while(len(q)):
            str = q[0]
            q.pop(0)
            if (self.isValidString(str)):
                #print(str)
                res.append(str)
                # If answer is found, make level true 
                # so that valid of only that level 
                # are processed. 
                level = True
            if (level):
                continue
            for i in range(len(str)):
                if (not self.isParenthesis(str[i])):
                    continue
                # Removing parenthesis from str and 
                # pushing into queue,if not visited already 
                temp = str[0:i] + str[i + 1:] 
                if temp not in visit:
                    q.append(temp)
                    visit.add(temp)
        return res
    



    def removeInvalidParenthesis_dfs(self, string: str) -> List[str]:
        print (f"Provided string : {string}") 
        
        self.longest_string = -1
        self.res = set()
        self.dfs(string, 0, [], 0, 0)
        return self.res
    
    def dfs(self, string, cur_index, cur_res, l_count, r_count):
        string_length = len(string)
        if cur_index >= string_length:
            if l_count == r_count:
                if len(cur_res) > self.longest_string:
                    self.longest_string = len(cur_res)

                    self.res = set()
                    self.res.add("".join(cur_res))
                elif len(cur_res) == self.longest_string:
                    self.res.add("".join(cur_res))
        else:
            cur_char = string[cur_index]

            if cur_char == "(":
                cur_res.append(cur_char)
                self.dfs(string, cur_index + 1, cur_res, l_count + 1, r_count)
                cur_res.pop()

                self.dfs(string, cur_index + 1, cur_res, l_count, r_count)
            elif cur_char == ")":
                self.dfs(string, cur_index + 1, cur_res, l_count, r_count)

                if l_count > r_count:
                    cur_res.append(cur_char)
                    self.dfs(string, cur_index + 1, cur_res, l_count, r_count + 1)
                    cur_res.pop()
            else:
                cur_res.append(cur_char)
                self.dfs(string, cur_index + 1, cur_res, l_count, r_count)
                cur_res.pop()


    

# Driver Code
if __name__ == "__main__" :
    expression = "()())()"
    print (f"Output = {Solution().removeInvalidParenthesis(expression)}")
    print (f"Output = {Solution().removeInvalidParenthesis_dfs(expression)}")
    print ("===============")
    expression = "()v)"
    print (f"Output = {Solution().removeInvalidParenthesis(expression)}")
    print (f"Output = {Solution().removeInvalidParenthesis_dfs(expression)}")
    print ("===============")
    expression = "(a)())())"
    print (f"Output = {Solution().removeInvalidParenthesis(expression)}")
    print (f"Output = {Solution().removeInvalidParenthesis_dfs(expression)}")
    print ("===============")
    expression = ")("
    print (f"Output = {Solution().removeInvalidParenthesis(expression)}")
    print (f"Output = {Solution().removeInvalidParenthesis_dfs(expression)}")
    
        