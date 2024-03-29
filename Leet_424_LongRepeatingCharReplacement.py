""" 
LeetCode 424. Longest Repeating Character Replacement

https://www.youtube.com/watch?v=gqXU1UyA8pk

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length """


from collections import defaultdict


class LongRepeatingCharReplacement:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        start = 0
        maxf = 0
        for end in range(len(s)):
            count [s[end]] = 1 + count.get(s[end], 0)
            maxf = max(maxf, count[s[end]])

            while (end - start + 1) - maxf > k:
                count[s[start]] -= 1
                start += 1
            
            result = max(result, end - start + 1 )
        return result
    
    def characterReplacement_1(self, s: str, k: int) -> int:
        count = {}
        maxf = 0
        l=0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(maxf, count[s[r]])
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
        return (r - l + 1)
    
    def characterReplacement_2(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        maxf = 0
        l = 0
        for r in range(len(s)):
          dic[s[r]] += 1
          if dic[s[r]] > maxf:
            maxf = dic[s[r]]
          if r - l + 1 - maxf > k:
            dic[s[l]] -= 1
            l += 1
        # print(r, l)
        return r - l + 1

    
print (LongRepeatingCharReplacement().characterReplacement("ABAB", 2))
print (LongRepeatingCharReplacement().characterReplacement("ABABBA", 2))
print (LongRepeatingCharReplacement().characterReplacement("AABABBA", 1))

print (LongRepeatingCharReplacement().characterReplacement_1("ABAB", 2))
print (LongRepeatingCharReplacement().characterReplacement_1("ABABBA", 2))
print (LongRepeatingCharReplacement().characterReplacement_1("AABABBA", 1))

