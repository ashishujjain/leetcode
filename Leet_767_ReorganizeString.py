""" 767. Reorganize String | https://leetcode.com/problems/reorganize-string/description/

Youtube:
    https://www.youtube.com/watch?v=wZENBuWh-C0&t=329s
    https://www.youtube.com/watch?v=Kgb6E5maPIM
Medium

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:
    Input: s = "aab"
    Output: "aba"
Example 2:
    Input: s = "aaab"
    Output: ""
Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters. """

from collections import Counter
import heapq
class Solution:
    def getMaxCountChar(self, countarray):
        max = letter = 0
        for key, value in countarray.items():
            if value > max:
                max = value
                letter = key
        return letter, max

    def reorganizeString(self, s: str) -> str:
        s_count = Counter(s)
        stringLen = len(s)
        print (f"s_count {s_count}") 
        key, value = Solution().getMaxCountChar(s_count)
        #print (f"key : {key} and its freq is {value}")
        if value > (len(s) + 1)/2: return ""
        res = [None]*len(s)
        counter = 0
        while value:
            res[counter] = key
            counter += 2
            value -= 1
        s_count[key]=0
        print (f"s_count : {s_count} and res {res}")
        
        for key, value in s_count.items():
            print (f"s_count[{key}] : {value} ")
            while s_count[key] > 0:
                print (f"counter {counter} and stringLen {stringLen} ") 
                if counter >= stringLen:
                    counter = 1
                res[counter]=key
                counter += 2
                s_count[key] -= 1
                print (f"s_count : {s_count} and res {res}")
        return ''.join(res)
    
    def reorganizeString_heap(self, s: str) -> str:
        print (f"Given String is : {s}")
        count = Counter(s) # Hashmap, count each char # {'a': 3, 'b': 1}
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        print (f"maxHeap {maxHeap}") # maxHeap [[-3, 'x'], [-1, 'r'], [-1, 'w'], [-2, 'p']]
        heapq.heapify(maxHeap) # o(n) 
        print (f"after heapq.heapify(maxHeap) {maxHeap}") #after heapq.heapify(maxHeap) [[-3, 'x'], [-2, 'p'], [-1, 'w'], [-1, 'r']]
        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            # most frequent, except prev
            cnt, char = heapq.heappop(maxHeap)
            print (f"after heapq.heappop(maxHeap) {maxHeap}") #after heapq.heapify(maxHeap) [[-3, 'x'],
            res += char
            cnt += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res


if __name__=="__main__":
    leet = Solution()
    String = "xxxrwpp"
    Output = "xwxpxpr"
    result = leet.reorganizeString(String)
    if result == Output:
        print ("used reorganizeString and Output String:" ,result)
        print ("")
    else:
        print ("Wrong Answer, result is ", result)
    
    print ("==================================")
    String = "a"
    Output = "a"
    result = leet.reorganizeString(String)
    if result == Output:
        print ("used reorganizeString and Output String:" ,result)
        print ("")
    else:
        print ("Wrong Answer, result is ", result)
    
    print ("==================================")
    String = "aab"
    Output = "aba"
    result = leet.reorganizeString(String)
    if result == Output:
        print ("used reorganizeString and Output String:" ,result)
        print ("")
    else:
        print ("Wrong Answer, result is ", result)

    print ("==================================")
    String = "aaab"
    Output = ""
    result = leet.reorganizeString(String)
    if result == Output:
        print ("used reorganizeString and Output String:" ,result)
        print ("")
    else:
        print ("Wrong Answer, result is ", result)
    

    String = "a"
    Output = "a"
    result = leet.reorganizeString_heap(String)
    if result == result in Output:
        print ("used reorganizeString_heap and Output String:" ,result)
        print ("")
    else:
        print ("Wrong Answer, result is ", result)
    
    print ("==================================")
    String = "xxxrwpp"
    Output = "[xwxpxpr, xpxprwx]"
    result = leet.reorganizeString_heap(String)
    if result == result in Output:
        print ("used reorganizeString_heap and Output String:" ,result)
        print ("")
    else:
        print ("Wrong Answer, result is ", result)
    
    print ("==================================")
    String = "aab"
    Output = "aba"
    result = leet.reorganizeString_heap(String)
    if result == result in Output:
        print ("used reorganizeString_heap and Output String:" ,result)
        print ("")
    else:
        print ("Wrong Answer, result is ", result)

    print ("==================================")
    String = "aaab"
    Output = ""
    result = leet.reorganizeString_heap(String)
    if result == result in Output:
        print ("used reorganizeString_heap and Output String:" ,result)
        print ("")
    else:
        print ("Wrong Answer, result is ", result)

    String = "a"
    Output = "a"
    result = leet.reorganizeString_heap2(String)
    if result == result in Output:
        print ("used reorganizeString_heap2 and Output String:" ,result)
        print ("")
    else:
        print ("Wrong Answer, result is ", result)
    print ("==================================")

    String = "xxxrwpp"
    Output = "[xwxpxpr, xpxprwx]"
    result = leet.reorganizeString_heap2(String)
    if result == result in Output:
        print ("used reorganizeString_heap2 and Output String:" ,result)
        print ("")
    else:
        print ("Wrong Answer, result is ", result)
    
    print ("==================================")
    String = "aab"
    Output = "aba"
    result = leet.reorganizeString_heap2(String)
    if result == result in Output:
        print ("used reorganizeString_heap2 and Output String:" ,result)
        print ("")
    else:
        print ("Wrong Answer, result is ", result)

    print ("==================================")
    String = "aaab"
    Output = ""
    result = leet.reorganizeString_heap2(String)
    if result == result in Output:
        print ("used reorganizeString_heap2 and Output String:" ,result)
        print ("")
    else:
        print ("Wrong Answer, result is ", result)