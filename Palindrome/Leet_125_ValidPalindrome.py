""" 125. Valid Palindrome

https://leetcode.com/problems/valid-palindrome/


https://www.youtube.com/watch?v=jJXJ16kPFWg

Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters. """


class Leet_125_ValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        newStr = "" # defining a new string valraible, can we do without this?
        for c in s:
            if c.isalnum():  # what if isalnum function is not allowed to be used
                newStr += c.lower()
        reversenewStr = newStr[::-1]
        print (f"Original string [{s}], modifified string [{newStr}], reversed string [{reversenewStr}]")
        return newStr == reversenewStr # reversing the string
    
    #left and right Pointer solution
    def isPalindrome_1(self, s: str) -> bool:
        l , r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            #print (s[l].lower(), s[r].lower())
            if s[l].lower() != s[r].lower():
                return False
            l , r = l + 1, r - 1
        return True
    
    def alphaNum(self, c):
        res = (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        #print (res)
        return res

if (Leet_125_ValidPalindrome().isPalindrome("A man, a plan, a canal: Panama")):
    print("Yes")
else:
    print("No")
 
if (Leet_125_ValidPalindrome().isPalindrome("race a car")):
    print("Yes")
else:
    print("No")

if (Leet_125_ValidPalindrome().isPalindrome("")):
    print("Yes")
else:
    print("No")
if (Leet_125_ValidPalindrome().isPalindrome("12344321")):
    print("Yes")
else:
    print("No")
if (Leet_125_ValidPalindrome().isPalindrome("rotator")):
    print("Yes")
else:
    print("No")


print ("========================================================================")
#print (Leet_125_ValidPalindrome().isPalindrome_1("A man, a plan, a canal: Panama"))
if (Leet_125_ValidPalindrome().isPalindrome_1("A man, a plan, a canal: Panama")):
    print("Yes")
else:
    print("No")
 
if (Leet_125_ValidPalindrome().isPalindrome_1("race a car")):
    print("Yes")
else:
    print("No")

if (Leet_125_ValidPalindrome().isPalindrome_1("")):
    print("Yes")
else:
    print("No")
if (Leet_125_ValidPalindrome().isPalindrome_1("12344321")):
    print("Yes")
else:
    print("No")
if (Leet_125_ValidPalindrome().isPalindrome_1("rotator")):
    print("Yes")
else:
    print("No")