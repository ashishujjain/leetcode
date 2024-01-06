""" 621. Task Scheduler
Medium

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. 
Tasks could be done in any order. Each task is done in one unit of time. 
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100]. """


from collections import deque
import heapq
from typing import Counter, List


class Leet_621_TaskScheduler:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minmize idle time
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
    
    #
    def leastInterval_1(self, tasks: List[str], n: int) -> int:
        # define a frequency dictonary to have task and its frequency count
        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1
        print ("frequency=", freq)
        freq = [value for key, value in freq.items()]
        print ("Highest frequency=", freq)
        max_freq = max(freq)
        print ("Highest frequency count =", max_freq)
        
        max_freq_tasks = freq.count(max_freq)
        print ("Highest frequency task =", max_freq_tasks)
        
        # formula is as below
        leasttasktime = (max_freq - 1) * (n + 1) + max_freq_tasks
        tasklenght = len(tasks)

        print ("leasttasktime:", leasttasktime)
        print ("tasklenght:", tasklenght)

        return max(tasklenght, leasttasktime)

print (Leet_621_TaskScheduler().leastInterval(["A","A","A","B","B","B"], 2))
print (Leet_621_TaskScheduler().leastInterval(["A","A","A","B","B","B","B"], 2))
print (Leet_621_TaskScheduler().leastInterval(["A","A","A","B","B","B"], 0))
print (Leet_621_TaskScheduler().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
print ("")
print (Leet_621_TaskScheduler().leastInterval_1(["A","A","A","B","B","B"], 2))
print (Leet_621_TaskScheduler().leastInterval_1(["A","A","A","B","B","B","B"], 2))
print (Leet_621_TaskScheduler().leastInterval_1(["A","A","A","B","B","B"], 0))
print (Leet_621_TaskScheduler().leastInterval_1(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
        
