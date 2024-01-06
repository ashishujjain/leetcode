""" 242. Valid Anagram
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true


Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case? """

from collections import Counter


class Leet_242_ValidAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True

    def isAnagramcounter(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    def isAnagramsorted(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

print (Leet_242_ValidAnagram().isAnagram("anagram", "nagaram"))
print (Leet_242_ValidAnagram().isAnagram("rat", "car"))

print (Leet_242_ValidAnagram().isAnagram("annagram", "nagaram"))
print (Leet_242_ValidAnagram().isAnagram("rat", "car"))

#print (Leet_242_ValidAnagram().isAnagramcounter("anagram", "nagaram"))
#print (Leet_242_ValidAnagram().isAnagramcounter("rat", "car"))

#print (Leet_242_ValidAnagram().isAnagramsorted("anagram", "nagaram"))
#print (Leet_242_ValidAnagram().isAnagramsorted("rat", "car"))