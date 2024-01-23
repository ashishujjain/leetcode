""" 
3. Longest Substring Without Repeating Characters

https://www.youtube.com/watch?v=wiGpQwVHdE0

Medium



Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces. 
"""

class Leet_3_LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max (res, r - l + 1)
        return res
    
    def lengthOfLongestSubstring_1(self, s: str) -> int:
        maxLength = 0
        charPos = {}
        l, r = 0, 0
        while r<len(s):
            if s[r] in charPos and charPos[s[r]] >= l:
                l = charPos[s[r]] + 1
            maxLength = max(maxLength, r-l+1)
            charPos[s[r]] = r
            r+=1
        return maxLength
    
print (Leet_3_LongestSubstringWithoutRepeatingCharacters().lengthOfLongestSubstring("abcabcbb"))
print (Leet_3_LongestSubstringWithoutRepeatingCharacters().lengthOfLongestSubstring("bbbbb"))
print (Leet_3_LongestSubstringWithoutRepeatingCharacters().lengthOfLongestSubstring("pwwkew"))

print (Leet_3_LongestSubstringWithoutRepeatingCharacters().lengthOfLongestSubstring_1("abcabcbb"))
print (Leet_3_LongestSubstringWithoutRepeatingCharacters().lengthOfLongestSubstring_1("bbbbb"))
print (Leet_3_LongestSubstringWithoutRepeatingCharacters().lengthOfLongestSubstring_1("pwwkew"))
